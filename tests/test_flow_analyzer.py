import pytest
import os
from src.utils import load_flow_data, extract_user_interactions, get_flow_name
from src.steps import identify_user_interactions, generate_human_friendly_summary

@pytest.fixture
def flow_data():
    """Fixture to load flow data once for all tests"""
    return load_flow_data()

def test_load_flow_data(flow_data):
    """Test that flow data loads correctly"""
    assert flow_data is not None
    assert 'steps' in flow_data
    assert 'name' in flow_data

def test_extract_user_interactions(flow_data):
    """Test that interactions are extracted from flow data"""
    interactions = extract_user_interactions(flow_data)
    
    assert len(interactions) > 0
    assert all('page_title' in i for i in interactions)
    assert all('element_clicked' in i for i in interactions)
    assert all('hotspot_hint' in i for i in interactions)

def test_get_flow_name(flow_data):
    """Test that flow name is extracted correctly"""
    flow_name = get_flow_name(flow_data)
    
    assert flow_name is not None
    assert len(flow_name) > 0
    assert flow_name != 'Untitled Flow'

def test_identify_user_interactions_format(flow_data):
    """Test that interaction text is properly formatted"""
    interactions_text = identify_user_interactions(flow_data)
    
    assert interactions_text is not None
    assert len(interactions_text) > 0
    # Should be numbered list
    assert '1.' in interactions_text

def test_generate_summary_format(flow_data):
    """Test that summary is generated and formatted properly"""
    flow_name = get_flow_name(flow_data)
    raw_interactions = extract_user_interactions(flow_data)
    
    summary = generate_human_friendly_summary(flow_name, raw_interactions)
    
    assert summary is not None
    assert len(summary) > 100  # Should be substantial
    assert len(summary.split('\n\n')) >= 2  # Should have multiple paragraphs

def test_output_files_exist():
    """Test that output files exist after running main"""
    assert os.path.exists('REPORT.md'), "REPORT.md should exist"
    assert os.path.exists('social_media_image.png'), "social_media_image.png should exist"

def test_report_content():
    """Test that REPORT.md has expected structure"""
    with open('REPORT.md', 'r') as f:
        content = f.read()
        assert '## User Interactions' in content
        assert '## Summary' in content
        assert '## Social Media Image' in content
        assert 'social_media_image.png' in content

def test_image_file_valid():
    """Test that generated image is a valid PNG file"""
    assert os.path.exists('social_media_image.png')
    
    with open('social_media_image.png', 'rb') as f:
        # Check PNG magic number
        header = f.read(8)
        assert header[:4] == b'\x89PNG'