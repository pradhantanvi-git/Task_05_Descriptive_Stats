# 📊 Claude Error & Failure Analysis

This document highlights errors observed when using **Claude** on the IPL 2022 dataset. Claude sometimes produced **different results in its narrative text vs. structured validation output**, and in other cases gave **plausible but incorrect statistics**.

---

## ⚠️ Case Study: Q6 — Wins by Defending vs. Chasing

**Question:** *Overall, did teams win more by defending or by chasing in IPL 2022?*

### Claude Narrative Output (Chat Text)
- Chasing wins: **41 (55.4%)**  
- Defending wins: **33 (44.6%)**  
- *Answer: Teams won more by chasing.*

### Claude Structured Output (Validation Card)
- Defending wins: **37 (50.0%)**  
- Chasing wins: **37 (50.0%)**  
- *Answer: Exactly balanced between chasing and defending.*

**Error Analysis:**  
- Contradiction between narrative and validation output.  
- Narrative “hallucinated” a 41–33 split, but validated output shows perfect balance (37–37).  
- This shows a **narrative vs validation gap**.

---

## ⚠️ Case Study: Q7 — Batting-Friendly & Chase-Friendly Venues

**Question:** *Which venues were most batting-friendly and most chase-friendly (≥5 matches)?*

### Claude Narrative Output
- Batting-friendly: **DY Patil Stadium (~175 runs)**  
- Chase-friendly: **Brabourne Stadium (~60% chases won)**  

### Python Validation
- Batting-friendly: **Brabourne Stadium (avg 177.2, n=16)** ✅  
- Chase-friendly: **Wankhede Stadium (13/21 = 61.9%)** ❌ (Claude picked Brabourne/DY Patil incorrectly)

**Error Analysis:**  
- Claude misattributed venues, mixing DY Patil and Brabourne.  
- Shows a **tendency to guess when multiple venues are close** rather than calculate exactly.

---

## ⚠️ Case Study: Q8 — Handling Close Games

**Question:** *Who handled close games the best (≤10 runs or ≤3 wickets)?*

### Claude Narrative Output
- Rajasthan Royals — **67% (4 wins of 6)**  
- Gujarat Titans — **60% (3 wins of 5)**  
- RCB — **50% (3 wins of 6)**  

### Python Validation
- Gujarat — **2/3 (66.7%)** ✅  
- Lucknow — **2/3 (66.7%)** ❌ (Claude ignored Lucknow)  
- Mumbai — **1/3 (33.3%)** ❌  
- Kolkata — **0/4 (0%)** ❌  

**Error Analysis:**  
- Claude **invented numbers** for Rajasthan and RCB not supported by dataset.  
- Ignored Lucknow, which actually performed as well as Gujarat.  
- Demonstrates **hallucination** — generating “believable” but false stats.

---

## ✅ Key Takeaways

- **Narrative vs Validation Gap:** Claude sometimes contradicted its own tool output.  
- **Hallucination of Stats:** It produced realistic-looking numbers (Rajasthan, RCB) that were not in the dataset.  
- **Bias Toward Prominent Teams:** Similar to GPT, Claude favored well-known teams/venues over the statistically correct ones.  
- **Importance of Validation:** Without Python checks, these errors would remain undetected.  
- **Research Contribution:** Documenting Claude’s failures alongside GPT strengthens the study’s conclusion: *LLMs cannot yet be trusted for precise statistical reporting without external validation*.
