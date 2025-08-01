# 📌 CHAT GPT 4 prompt - 5 Research Questions & Answers

This README presents the answers derived from analyzing the IPL 2022 dataset (`ipl_2022_cricket_match.csv`) using Python and pandas. The analysis focuses on five specific research questions related to match results, top players, and team performance trends.

---

## 🧠 Approach
- The dataset was loaded and inspected for relevant columns (winner, player_of_the_match, toss_winner, won_by, won_by_runs, won_by_wickets, top_scorer, top_score, etc.).
- Data was filtered, grouped, and aggregated to derive insights.
- Python (pandas) was used for all computations.

---

## 🔍 Research Questions and Answers

### **Q1: Which team won the most matches in IPL 2022?**
**Answer:** Gujarat (Gujarat Titans) — **12 wins** (out of 74 matches in the dataset).
- Next best: Rajasthan 10, Bangalore 9, Lucknow 9.

---

### **Q2: Who was most often named Player of the Match?**
**Answer:** Kuldeep Yadav — **4 awards**.
- Next: Jos Buttler with 3; several players had 2 awards.

---

### **Q3: How often did the toss winner also win the match?**
**Answer:** 36 of 74 matches — **48.65%** of the time, the team that won the toss also won the match.

---

### **Q4: For Gujarat, how many matches did they win by chasing versus batting first?**
**Answer:**
- **Chasing (won by wickets): 8 matches**
- **Batting first (won by runs): 4 matches**

---

### **Q5: Which 3 players had the highest individual scores in matches where they were awarded Player of the Match?**
**Answer:** (Player of the Match was also the top scorer in these cases)
- Quinton de Kock — **140 runs**
- Jos Buttler — **116 runs**
- Rajat Patidar — **112 runs**

---

## ✅ Summary
This analysis provides data-driven answers to the research questions using IPL 2022 match data. Python's pandas library was instrumental in filtering and aggregating the results quickly and accurately.

