import json
from typing import Dict, List, Any
from constants import flow_file_path

def load_flow_data(filepath: str = flow_file_path) -> Dict[str, Any]:
    """Load the flow file"""
    with open(filepath, 'r') as f:
        return json.load(f)