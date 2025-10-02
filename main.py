from utils import load_flow_data, get_flow_name
from steps import identify_user_interactions, generate_human_friendly_summary, create_social_media_image

def main():
    flow_data = load_flow_data()
    flow_name = get_flow_name(flow_data)
    
    # Identify user interactions
    interactions = identify_user_interactions(flow_data)
    print("User Interactions:")
    print(interactions)
    print("\n" + "="*50 + "\n")
    
    # Generate summary
    summary = generate_human_friendly_summary(flow_name, interactions)
    print("Summary:")
    print(summary)
    print("\n" + "="*50 + "\n")
    
    # Create social media image

    
    # Generate report
    
    print("\n✅ All done!")

if __name__ == "__main__":
    main()