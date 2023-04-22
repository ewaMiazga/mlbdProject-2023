import pandas as pd
import lightgbm as lgb



def create_timeseries(events, subtasks):
    events_and_substasks = events.reset_index().merge(subtasks.reset_index(), how='left', on=['event_id','user_id'], suffixes=('_event', '_subtask'))
    events_and_substasks['date'] = pd.to_datetime(events_and_substasks['start'])
    events_and_substasks[['Year', 'Week', 'Day']] = events_and_substasks['date'].dt.isocalendar()
    events_and_substasks['year_week'] = (events_and_substasks['Year'] - 2015) * 53 + events_and_substasks['Week']
    events_and_substasks['week'] = events_and_substasks.groupby('user_id')['year_week'].apply(lambda x: x - x.iat[0]) +1
    task_events = events_and_substasks.query('type_event == "task" & correct != "nan"')
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


def train_model(lgb_train, lgb_eval):
    params = {'objective': 'binary',
          'metric': 'auc',
          'seed': 0,
          'learning_rate': 0.1, #default
          "boosting_type": "gbdt" #default
          # 'num_leaves': 200,
          # 'feature_fraction': 0.75,
          # 'bagging_freq': 10,
          # 'bagging_fraction': 0.80
         }
    model = lgb.train(
        params, lgb_train,
        valid_sets=[lgb_train, lgb_eval],
        verbose_eval=50,
        num_boost_round=10000,
        early_stopping_rounds=8,
        keep_training_booster=True
    )
    return model