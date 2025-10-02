import json
from typing import Dict, List, Any
from constants import flow_file_path

def load_flow_data(filepath: str = flow_file_path) -> Dict[str, Any]:
    """Load the flow file"""
    with open(filepath, 'r') as f:
        return json.load(f)
    
def get_flow_name(flow_data: Dict[str, Any]) -> str:
    """Get the flow name from flow data"""
    return flow_data.get('name', 'Untitled Flow')

def extract_user_interactions(flow_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Extract user interactions from flow data"""
    interactions = []

    for step in flow_data['steps']:
        if step['type'] == 'IMAGE' and step.get('clickContext'):
            interaction = {
                'page_title': step['pageContext'].get('title', 'Unknown page'),
                'page_url': step['pageContext'].get('url', ''),
                'element_clicked': step['clickContext'].get('text', ''),
                'element_type': step['clickContext'].get('elementType', ''),
                'hotspot_hint': step['hotspots'][0]['label'] if step.get('hotspots') else ''
            }
            interactions.append(interaction)
    
    return interactions

def save_markdown_report(interactions: str, summary: str, image_path: str, output_path: str = 'REPORT.md') -> None:
    """Generate and save the final markdown report"""
    
    markdown = f"""# Arcade Flow Analysis Report

## User Interactions

{interactions}

## Summary

{summary}

## Social Media Image

![Social Media Image]({image_path})

---
*Generated using OpenAI API*
"""
    
    with open(output_path, 'w') as f:
        f.write(markdown)
    
    print(f"Report saved to: {output_path}")