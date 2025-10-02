import os
from dotenv import load_dotenv
from utils import load_flow_data, extract_user_interactions
from prompts import get_interactions_prompt

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")

# steps to accomplish
# Identify User Interactions: List out the actions the user did in a human readable format (i.e. "Clicked on checkout", "Search for X")
def identify_user_interactions() -> str:
    flow_data = load_flow_data()
    interactions = extract_user_interactions(flow_data)
    prompt = get_interactions_prompt(flow_data.get('name', 'Unknown Flow'), interactions)

    pass
# Generate Human-Friendly Summary: Create a clear, readable summary of what the user was trying to accomplish
def generate_human_friendly_summary() -> None:
    pass
# Create a Social Media Image: Generate an creative image suitable for sharing on social platforms that represents the flow and would drive engagement
def create_social_media_image() -> None:
    pass

identify_user_interactions()