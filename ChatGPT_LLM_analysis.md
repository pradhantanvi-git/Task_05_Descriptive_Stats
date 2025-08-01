# 📌 IPL 2022 Cricket Dataset - LLM Prompt Analysis / CHAT GPT strategy

This README explains the approach used to analyze the IPL 2022 dataset using Python and pandas. The analysis answers 5 research questions about match results, top players, and team performances.

---

## 🧠 General Strategy

As an LLM with Python and data analysis capabilities, I processed the CSV file using the following steps:

1. Load the dataset using pandas.
2. Inspect dataset columns (e.g., `winner`, `player_of_the_match`, `toss_winner`, `match_winner`, `won_by`, `won_by_runs`, `won_by_wickets`, `team1`, `team2`).
3. Filter, group, and aggregate data to compute results.
4. Derive insights from the dataset similar to how a human analyst would work in Excel or Python.

---

## 🔍 Breakdown of Each Question

### **Q1: Which team won the most matches in IPL 2022?**

**Logic:**

- Count frequency of each team in the `winner` column.
- Identify the team with the highest count.

```python
team_with_most_wins = df['winner'].value_counts().idxmax()
```

---

### **Q2: Who was most often named Player of the Match?**

**Logic:**

- Count occurrences of each name in the `player_of_the_match` column.
- Return the top player.

```python
top_player = df['player_of_the_match'].value_counts().head(1)
```

---

### **Q3: How often did the toss winner also win the match?**

**Logic:**

- Compare `toss_winner` and `winner` for each match.
- Calculate the proportion where they match.

```python
same_winner_ratio = (df['toss_winner'] == df['winner']).sum() / len(df)
```

---

### **Q4: For Gujarat, how many matches did they win by chasing vs. batting first?**

**Logic:**

- Filter rows where `winner == 'Gujarat'`.
- Use `won_by_runs` and `won_by_wickets` columns:
  - If `won_by_runs > 0` → batting first.
  - If `won_by_wickets > 0` → chasing.

```python
gujarat_wins = df[df['winner'] == 'Gujarat']
chasing = (gujarat_wins['won_by_wickets'] > 0).sum()
batting_first = (gujarat_wins['won_by_runs'] > 0).sum()
```

---

### **Q5: Which 3 players had the highest individual scores in matches where they were awarded Player of the Match?**

**Logic:**

- Filter rows where `player_of_the_match == top_scorer`.
- Sort by `top_score` and select the top 3 players.

```python
pom_scores = df[df['player_of_the_match'] == df['top_scorer']]
top_3 = pom_scores.sort_values('top_score', ascending=False).head(3)
```

---

## ✅ Output

The above steps provide clear, data-driven answers to each research question based on the IPL 2022 dataset.

