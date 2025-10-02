def get_interactions_prompt(flow_name: str, interactions: list) -> str:
    """Generate prompt for identifying user interactions"""
    import json
    
    return f"""Analyze these user interactions from a screen recording and convert them into clear, human-readable actions.

Flow Title: {flow_name}

Interactions:
{json.dumps(interactions, indent=2)}

For each interaction, create a single, clear sentence describing what the user did.
Use past tense and be concise.
Format as a numbered list.

Example format:
1. Clicked on the search bar
2. Searched for "protein powder"
3. Selected the Leanbakers protein powder from results
"""
