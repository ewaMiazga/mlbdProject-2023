# Imports
# data
import numpy as np
import pandas as pd
import re

# graph
import networkx as nx
from networkx.drawing.nx_agraph import read_dot

# Get nodes that fits the pattern based on skill_id and game_name
def get_nodes(G, first_word, last_word):

    # Create the regular expression pattern
    pattern = r"\b" + first_word + r"\b(.*?)" + last_word.split()[0] + r"\b(.*)"

    nodes = list(G.nodes())

    matches = [re.search(pattern, node).group() for node in nodes if re.search(pattern, node)]
    return matches

# Get the skill_id ranks of the game
def get_skill_id_ranks(G, game):

    all_matches = get_nodes(G, '', game)

    skill_ranks = [s.split()[0] for s in all_matches]
    return set(skill_ranks)

# Find the ranking for skill_id
def choose_ranking(G, game, skill_id):

    rankings = list(get_skill_id_ranks(G, game))

    upper_limits = np.array([int(rank.split("-")[1]) for rank in rankings])
    if not upper_limits.any():
        return ''
    is_rank = skill_id < upper_limits

    if not is_rank.any():
        max_index = np.argmin(upper_limits)
    else:
        min_limit = np.min(upper_limits[is_rank])
        max_index = np.where(upper_limits == min_limit)[0][0]

    return rankings[max_index]

# Find the name of game in names of games from graph
def find_word_in_list(word, string_list):
    for string in string_list:
        if str(word) in string:
            return True
    return False

# Calculate mastery level
def calculate_mastery_level(G, user_subtasks, week, game, skill_id):

    # Find ranking of skill
    skill_rank = choose_ranking(G, game, skill_id)

    # Get nodes that matches the game and skill id 
    skill_nodes = get_nodes(G, skill_rank, game)

    # If the game is not in skills graph
    if not skill_nodes:
        games = [game]
    # Find the ancestors of the node
    else:
        skill_node = skill_nodes[0]
        ancestors = nx.ancestors(G, skill_node)
        games = [ancestors, skill_nodes[0]]

    # Check if the event was previous than the subtask
    user_subtasks = user_subtasks[user_subtasks['week_number'] <= week]
    answers = []

    for idx, subtask in user_subtasks.iterrows():
        answers.append(find_word_in_list(subtask['game_name'], games) and subtask['correct'])

    if not answers:
        return 0.0
    return sum(answers) / len(answers)

# Find the records corresponding to the chosen user_id
def find_user_subtasks(subtasks, user_id):
    user_subtasks = subtasks.loc[subtasks['user_id_x'] == user_id]
    user_subtasks = user_subtasks.copy()

    user_subtasks['subtask_finished_timestamp'] = pd.to_datetime(user_subtasks['subtask_finished_timestamp'])
    user_subtasks = user_subtasks.dropna(subset=['subtask_finished_timestamp'])

    # Group by week and assign week number
    week_groups = user_subtasks.groupby(pd.Grouper(key='subtask_finished_timestamp', freq='W-MON', closed='left'))
    user_subtasks['week_number'] = week_groups.ngroup() + 1
    return user_subtasks

# Choose rows with not only 0 values (users that did not play the game)
def get_random_ids(df, how_many, game, col):
    print("a")
    user_ids = df.index.levels[0]
    random_user_ids = []
    
    for user in user_ids:
        print(user)
        print(df.loc[(user, game), col].sum())
        if float(df.loc[(user, game), col].sum()) != 0.0:
            random_user_ids.append(user)

    if len(random_user_ids) < how_many:
        return random_user_ids
    return np.array(random_user_ids)[: how_many]

def convert_to_csv(df, name):
    df.to_csv(f'{name}')


def load_from_csv(name):
    return pd.read_csv(f'{name}', index_col=[0,1,2])
