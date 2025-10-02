from src.utils import load_flow_data, get_flow_name, extract_user_interactions, save_markdown_report
from src.steps import identify_user_interactions, generate_human_friendly_summary, create_social_media_image

def main():
    flow_data = load_flow_data()
    flow_name = get_flow_name(flow_data)

    # NOTE: Using raw interaction data for summary generation based on eval results
    # Raw data provides better completeness and accuracy than a chained llm call
    raw_interactions = extract_user_interactions(flow_data)
    
    # Identify user interactions (for display purposes)
    interactions_text = identify_user_interactions(flow_data)
    print("User Interactions:")
    print(interactions_text)
    print("\n" + "="*50 + "\n")
    
    # Generate summary using raw data
    summary = generate_human_friendly_summary(flow_name, raw_interactions)
    print("Summary:")
    print(summary)
    print("\n" + "="*50 + "\n")
    
    # Create social media image
    print("Generating social media image...")
    image_path = create_social_media_image(flow_name, summary)
    print(f"✅ Image created: {image_path}")
    print("\n" + "="*50 + "\n")
    
    # Generate report
    print("Generating markdown report...")
    save_markdown_report(interactions_text, summary, image_path)
    
    
    print("\n✅ All done!")

if __name__ == "__main__":
    main()