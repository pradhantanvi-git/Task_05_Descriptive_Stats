# 📊 Error & Failure Analysis

## ⚠️ Error & Failure Analysis (Basic Q5 from 1st analysis phase)

NOTE: On re-running the same question and dataset file on CHAT GPT the answer changed and did not match the python validation for Q5. 

### Q5: Which 3 players had the highest individual scores in matches where they were Player of the Match?
- **LLM Answer:**  
  - Jos Buttler — 116  
  - KL Rahul — 103*  
  - Quinton de Kock — 140*  

- **Python Validation:**  
  - Quinton de Kock — 140*  
  - Jos Buttler — 116   
  - Rajat Patidar — 112  

- **Error Analysis:** The LLM replaced Rajat Patidar (112) with KL Rahul (103*), despite Rahul’s score being lower.  
  - This shows a tendency to prioritize well-known players (KL Rahul) over statistically correct results (Patidar).  
  - It highlights the importance of validation when exact ranking is required.  

---
## ⚠️ Error & Failure Analysis (Advanced Q6–Q8)
Q6: Did teams win more by defending or chasing?

LLM Answer:
Chasing wins: 40
Defending wins: 34
Conclusion: Chasing slightly more successful.
Python Validation:
Chasing wins: 37
Defending wins: 37
Conclusion: Exactly balanced.
Error Analysis: The LLM inflated chasing wins by +3 and reduced defending by -3. This is a clear example of the LLM generating a “plausible” but statistically incorrect distribution.

Q7: Batting-friendly & Chase-friendly venues
LLM Answer:
Batting-friendly: Brabourne (~176 avg first inns)
Chase-friendly: DY Patil (62% chase wins)
Python Validation:
Batting-friendly: Brabourne (avg 177.2, n=16) ✅ (LLM correct here)
Chase-friendly: Wankhede (13/21 = 61.9%) ❌ (LLM wrongly picked DY Patil)
Error Analysis: The LLM correctly identified Brabourne but failed on chase-friendly venue. This shows that when multiple venues have close percentages, LLMs may “guess” rather than calculate precisely.

Q8: Who handled close games the best?
LLM Answer:
Rajasthan (67%), Gujarat (60%), RCB (50%)
Python Validation:
Gujarat — 2/3 (66.7%) ✅
Lucknow — 2/3 (66.7%) ❌ (LLM missed this)
Mumbai — 1/3 (33.3%) ❌
Kolkata — 0/4 (0%) ❌
Error Analysis: The LLM invented Rajasthan/RCB numbers not supported by the dataset and ignored Lucknow. This demonstrates hallucination, where it introduces incorrect but “believable” teams.

✅ Key Takeaways for Research

- LLM Tendency: Prefers plausible storytelling (famous teams/players, close percentages) rather than strict accuracy.
- Validation Value: Without Python validation, these errors would go unnoticed.
- Bias Insight: LLM leaned towards popular/high-profile teams (Rajasthan, RCB) while ignoring smaller but correct ones (Lucknow).
- Research Contribution: Documenting these mismatches strengthens the research goal — showing where LLMs fail and why human+script validation is necessary.