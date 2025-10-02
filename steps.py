import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from utils import extract_user_interactions, get_flow_name
from prompts import get_interactions_prompt, get_system_prompt, get_summary_prompt

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_KEY)

def identify_user_interactions(flow_data: dict) -> str:
    """Identify User Interactions: List out the actions the user did in a human readable format"""
    # TODO: Extract more data points for additional context, using IMAGE steps only for now
    interactions = extract_user_interactions(flow_data)
    flow_name = get_flow_name(flow_data)
    prompt = get_interactions_prompt(flow_name, interactions)
    # TODO: replace this with structured output, using naive approach for MVP and sake of time
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": get_system_prompt('interactions')},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    result = response.choices[0].message.content
    # TODO: Implement retry logic for model calls
    if result is None:
        raise ValueError("OpenAI API returned None for user interactions")
    return result

def generate_human_friendly_summary(flow_name: str, interactions: list | str) -> str:
    """Generate Human-Friendly Summary: Create a clear, readable summary of what the user was trying to accomplish"""
    if isinstance(interactions, list):
        interactions = interactions = json.dumps(interactions, indent=2)
    prompt = get_summary_prompt(flow_name, interactions)
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": get_system_prompt('summary')},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7 
    )
    
    result = response.choices[0].message.content
    
    if result is None:
        raise ValueError("OpenAI API returned None for summary")
    
    return result

def create_social_media_image() -> None:
    """Create a Social Media Image: Generate a creative image suitable for sharing on social platforms"""
    pass