# Summary Generation Evaluation Results

**Date:** 2025-10-02 12:04:13  
**Flow:** Add a Scooter to Your Cart on Target.com

## Evaluation Summary

We compared two approaches for generating summaries:
1. **Approach 1:** Using AI-formatted interaction text as input
2. **Approach 2:** Using raw interaction data (list of dicts) as input

## Results

### Approach 1: Formatted Interactions Input
**Average Score:** 4.25/5.0

| Criterion | Score | Reason |
|-----------|-------|--------|
| Completeness | 4/5 | The summary captures most of the major steps, including searching for the scooter, selecting a model, choosing colors, adding to cart, and declining coverage. However, it misses the final step of visiting the cart to review items. |
| Clarity | 5/5 | The summary is clear and easy to understand, providing a straightforward narrative of the user's actions in the workflow. |
| Conciseness | 4/5 | The summary is mostly concise, but it includes some embellishments like 'excited by its features and style' that are not necessary for understanding the workflow. |
| Accuracy | 4/5 | The summary is mostly accurate but includes minor inaccuracies, such as the user 'settling on the vibrant Blue' when they actually clicked on both Blue and Pink. Additionally, it suggests the user entered 'scooter' into the search bar, which is not explicitly shown in the interaction data. |

### Approach 2: Raw Data Input
**Average Score:** 4.50/5.0

| Criterion | Score | Reason |
|-----------|-------|--------|
| Completeness | 5/5 | The summary captures all major steps in the workflow, including searching for the scooter, selecting a color, adding it to the cart, declining coverage, and reviewing the cart. |
| Clarity | 5/5 | The summary is clear and easy to understand, providing a logical sequence of actions that someone unfamiliar with the flow can follow. |
| Conciseness | 4/5 | The summary is mostly concise, but it includes some embellishments like 'making a step towards a fun new ride' which could be considered unnecessary. |
| Accuracy | 4/5 | The summary is mostly accurate, but it slightly embellishes the user's experience by describing it as 'engaging' and 'confidently' clicking, which are subjective interpretations not directly supported by the data. |

## Conclusion

**Winner:** Approach 2

Approach 2 (raw data input) was selected for implementation because it provides:
- Better completeness in capturing all workflow steps
- Higher accuracy without introducing hallucinations
- Direct access to original data for the AI model

---
*Evaluation performed using GPT-4 as a judge*
