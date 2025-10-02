import json
from typing import Dict, List, Any
from constants import flow_file_path

def load_flow_data(filepath: str = flow_file_path) -> Dict[str, Any]:
    """Load the flow file"""
    with open(filepath, 'r') as f:
        return json.load(f)
    
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