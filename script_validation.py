import pandas as pd

# Load the dataset
df = pd.read_csv("ipl_2022_cricket_match_dataset.csv")

# Q1: Which team won the most matches?
most_wins_team = df['match_winner'].value_counts().idxmax()
most_wins_count = df['match_winner'].value_counts().max()

# Q2: Who was most often named Player of the Match?
top_player = df['player_of_the_match'].value_counts().idxmax()
top_player_count = df['player_of_the_match'].value_counts().max()

# Q3: How often did the toss winner also win the match?
toss_and_match_win = df[df['toss_winner'] == df['match_winner']].shape[0]
toss_win_rate = round((toss_and_match_win / df.shape[0]) * 100, 2)

# Q4: For Gujarat Titans, how many wins by chasing vs batting first?
gujarat_wins = df[df['match_winner'] == 'Gujarat']
gujarat_win_by = gujarat_wins['won_by'].value_counts().to_dict()
gujarat_chase_wins = gujarat_win_by.get("Wickets", 0)
gujarat_defend_wins = gujarat_win_by.get("Runs", 0)

# Q5 (Revised): Top 3 players with highest individual scores in POTM matches
potm_matches = df[df['player_of_the_match'].notnull() & (df['highscore'] > 0)]
top_individual_scores = (
    potm_matches[['player_of_the_match', 'highscore']]
    .sort_values(by='highscore', ascending=False)
    .drop_duplicates()
    .head(3)
)

# Print labeled output
print("Q1: Which team won the most matches?")
print(f"A1: {most_wins_team} ({most_wins_count} wins)\n")

print("Q2: Who was most often named Player of the Match?")
print(f"A2: {top_player} ({top_player_count} times)\n")

print("Q3: How often did the toss winner also win the match?")
print(f"A3: {toss_and_match_win} of {df.shape[0]} matches ({toss_win_rate}%)\n")

print("Q4: For Gujarat, how many wins by chasing vs batting first?")
print(f"A4: {gujarat_chase_wins} by chasing (Wickets), {gujarat_defend_wins} by defending (Runs)\n")

print("Q5: Top 3 individual high scores in Player of the Match games:")
for i, row in top_individual_scores.iterrows():
    print(f"A5.{i+1}: {row['player_of_the_match']} – {row['highscore']} runs")
