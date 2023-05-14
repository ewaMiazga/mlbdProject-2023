import pandas as pd
import lightgbm as lgb



def create_timeseries(users, events, subtasks):
    events_and_substasks = events.reset_index().merge(subtasks.reset_index(), how='left', on=['event_id','user_id'], suffixes=('_event', '_subtask'))
    events_and_substasks['date'] = pd.to_datetime(events_and_substasks['start'])
    events_and_substasks[['Year', 'Week', 'Day']] = events_and_substasks['date'].dt.isocalendar()
    events_and_substasks['year_week'] = (events_and_substasks['Year'] - 2015) * 53 + events_and_substasks['Week']
    events_and_substasks['week'] = events_and_substasks.groupby('user_id')['year_week'].apply(lambda x: x - x.iat[0]) +1
    events_and_substasks = events_and_substasks.merge(users['country'], on='user_id')
    task_events = events_and_substasks.query('type_event == "task" & correct != "nan"')
    task_events['correct'] = task_events['correct'].astype(int)
    return task_events

def create_train_test_split(df, features, target_feature, cat_features):
    train = df.query('user_id < 600')[features]
    y_train = df.query('user_id < 600')[target_feature]

    val = df.query('600 <= user_id < 800')[features]
    y_val = df.query('600 <= user_id < 800')[target_feature]

    test = df.query('user_id >= 800')[features]
    y_test = df.query('user_id >= 800')[target_feature]
    
    lgb_train = lgb.Dataset(train, y_train, categorical_feature = cat_features, free_raw_data=False)
    lgb_eval = lgb.Dataset(val, y_val, categorical_feature = cat_features, free_raw_data=False)
    lgb_test = lgb.Dataset(test, y_test, categorical_feature = cat_features, free_raw_data=False, reference=lgb_train)
    
    return lgb_train, lgb_eval, lgb_test


def create_uniform_train_test_split(df, features, target_feature, cat_features, users):
    train_user_ids = []
    valid_user_ids = []
    test_user_ids = []
    for c in users.country.unique():
        train_user_ids.extend(list(users.query(f'country == "{c}"').index[:150]))
        valid_user_ids.extend(list(users.query(f'country == "{c}"').index[150:200]))
        test_user_ids.extend(list(users.query(f'country == "{c}"').index[200:]))
        
    train_df = df[df["user_id"].isin(train_user_ids)]
    valid_df = df[df["user_id"].isin(valid_user_ids)]
    test_df = df[df["user_id"].isin(test_user_ids)]
    
    train = train_df[features]
    y_train = train_df[target_feature]
    val = valid_df[features]
    y_val = valid_df[target_feature]
    test = test_df[features]
    y_test = test_df[target_feature]
    
    lgb_train = lgb.Dataset(train, y_train, categorical_feature = cat_features, free_raw_data=False)
    lgb_eval = lgb.Dataset(val, y_val, categorical_feature = cat_features, free_raw_data=False)
    lgb_test = lgb.Dataset(test, y_test, categorical_feature = cat_features, free_raw_data=False, reference=lgb_train)
    
    return lgb_train, lgb_eval, lgb_test