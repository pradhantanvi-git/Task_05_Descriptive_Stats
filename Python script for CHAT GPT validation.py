import pandas as pd

# Load the dataset
df = pd.read_csv("ipl_2022_cricket_match_dataset.csv")

# Q6: Overall wins by defending vs chasing
won_by_counts = df['won_by'].value_counts()
runs_wins = won_by_counts.get("Runs", 0)
wickets_wins = won_by_counts.get("Wickets", 0)
total_matches = df.shape[0]

print("Q6: Did teams win more by defending or chasing?")
print(f"A6: Runs (defending): {runs_wins} ({runs_wins/total_matches*100:.2f}%)")
print(f"    Wickets (chasing): {wickets_wins} ({wickets_wins/total_matches*100:.2f}%)\n")

# Q7: Venue tendencies (min 5 matches)
venue_stats = (
    df.groupby("venue")
      .agg(matches=("venue", "size"),
           avg_first=("first_ings_score", "mean"),
           chase_rate=("won_by", lambda s: (s == "Wickets").mean()))
      .reset_index()
)

venues_5plus = venue_stats[venue_stats["matches"] >= 5]

batting_venue = venues_5plus.sort_values("avg_first", ascending=False).iloc[0]
chase_venue = venues_5plus.sort_values("chase_rate", ascending=False).iloc[0]

chase_rows = df[df["venue"] == chase_venue["venue"]]
chase_wins_here = (chase_rows["won_by"] == "Wickets").sum()
matches_here = chase_venue["matches"]

print("Q7: Which venues were most batting-friendly and most chase-friendly?")
print(f"A7.1: Most batting-friendly → {batting_venue['venue']} "
      f"(avg 1st inns {batting_venue['avg_first']:.1f}, n={int(batting_venue['matches'])})")
print(f"A7.2: Most chase-friendly → {chase_venue['venue']} "
      f"({chase_wins_here}/{int(matches_here)} = {chase_venue['chase_rate']*100:.1f}% wins by chasing)\n")

# Q8: Close-game performance (≤10 runs OR ≤3 wickets)
def is_close(row):
    if pd.isna(row["margin"]):
        return False
    if row["won_by"] == "Runs":
        return row["margin"] <= 10
    if row["won_by"] == "Wickets":
        return row["margin"] <= 3
    return False

df["close_game"] = df.apply(is_close, axis=1)

teams = pd.unique(df[["team1", "team2"]].values.ravel())

records = []
for team in teams:
    played = df[((df["team1"] == team) | (df["team2"] == team)) & df["close_game"]]
    total_close = len(played)
    won_close = (played["match_winner"] == team).sum()
    if total_close >= 3:
        win_rate = round(won_close / total_close * 100, 2)
        records.append((team, total_close, won_close, win_rate))

records = sorted(records, key=lambda x: (-x[3], -x[2], -x[1]))

print("Q8: Who handled close games (≤10 runs or ≤3 wickets) the best?")
for team, total_close, won_close, win_rate in records:
    print(f"A8: {team} — {won_close}/{total_close} close games won ({win_rate}%)")
