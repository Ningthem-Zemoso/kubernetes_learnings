#!/usr/bin/env python3
"""
Script to fetch comments from JSONPlaceholder API and save to JSON file
"""
import requests
import json
import os
from datetime import datetime

def fetch_comments():
    """Fetch comments from JSONPlaceholder API and save to JSON file"""
    try:
        print(f"[{datetime.now()}] Starting to fetch comments from API...")
        
        # Make GET request to the API
        response = requests.get('https://jsonplaceholder.typicode.com/comments')
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse JSON response
        comments = response.json()
        print(f"[{datetime.now()}] Successfully fetched {len(comments)} comments")
        
        # Prepare output data with metadata
        output_data = {
            "fetch_timestamp": datetime.now().isoformat(),
            "total_comments": len(comments),
            "comments": comments
        }
        
        # Create output directory if it doesn't exist
        output_dir = "/workspace/output"
        os.makedirs(output_dir, exist_ok=True)
        
        # Save to JSON file with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"{output_dir}/comments_{timestamp}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        
        print(f"[{datetime.now()}] Comments saved to {output_file}")
        print("Daily comments fetch job completed successfully!")
        
    except requests.exceptions.RequestException as e:
        print(f"[{datetime.now()}] Error fetching data: {e}")
        exit(1)
    except json.JSONDecodeError as e:
        print(f"[{datetime.now()}] Error parsing JSON: {e}")
        exit(1)
    except Exception as e:
        print(f"[{datetime.now()}] Unexpected error: {e}")
        exit(1)

if __name__ == "__main__":
    fetch_comments()
