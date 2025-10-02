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

def get_summary_prompt(flow_name: str, interactions: str) -> str:
    """Generate prompt for creating a human-friendly summary"""
    return f"""
Create a clear, engaging summary of what the user accomplished in this workflow.

Flow Title: {flow_name}

User Actions:
{interactions}

Write a 2-3 paragraph summary that:
- Explains the overall goal
- Highlights key steps
- Focuses on the outcome
- Uses friendly, accessible language

Write in past tense as if describing what happened.
"""

def get_system_prompt(task_type: str) -> str:
    """Get system prompt based on task type"""
    system_prompts = {
        'interactions': "You are a helpful assistant that analyzes user interactions and describes them clearly.",
        'summary': "You are a helpful assistant that creates clear, engaging summaries of user workflows.",
        'image': "You are a creative assistant that generates professional images for marketing materials."
    }
    return system_prompts.get(task_type, "You are a helpful assistant.")

def get_image_generation_prompt(flow_name: str, summary: str) -> str:
    """Generate prompt for DALL-E image generation"""
    # Keep summary brief (first 200 chars)
    brief_summary = summary[:200] + "..." if len(summary) > 200 else summary
    
    return f"""
A modern, professional illustration representing: {flow_name}

Context: {brief_summary}

Style: Clean, minimalist, vibrant gradient colors, isometric perspective.
Digital/tech aesthetic with abstract shapes and flowing elements.
Professional but engaging and eye-catching for social media.
NO text, letters, or words in the image.
"""