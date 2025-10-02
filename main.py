import os
from dotenv import load_dotenv
from openai import OpenAI
from utils import load_flow_data, extract_user_interactions, get_flow_name
from prompts import get_interactions_prompt, get_system_prompt, get_summary_prompt

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_KEY)

# steps to accomplish
# Identify User Interactions: List out the actions the user did in a human readable format (i.e. "Clicked on checkout", "Search for X")
def identify_user_interactions(flow_data: dict) -> str:
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

# Generate Human-Friendly Summary: Create a clear, readable summary of what the user was trying to accomplish
def generate_human_friendly_summary(flow_name: str, raw_interactions: list) -> str:
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

# Create a Social Media Image: Generate an creative image suitable for sharing on social platforms that represents the flow and would drive engagement
def create_social_media_image() -> None:
    pass

flow_data = load_flow_data()
flow_name = get_flow_name(flow_data)
interactions = identify_user_interactions(flow_data)
# identify_user_interactions()
summary = generate_human_friendly_summary(flow_name, interactions)
