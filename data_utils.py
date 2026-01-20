"""
Data utilities for loading and cleaning text data
"""

import json
import re

def load_profiles(file_path):
    """Load JSON profiles from file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def clean_text(text):
    """Clean text by lowercasing, removing punctuation, and extra spaces"""
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation and special characters
    text = re.sub(r'[^\w\s]', ' ', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text