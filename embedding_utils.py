"""
Simple text similarity without external dependencies
"""

import math
from collections import Counter

def load_model():
    """Return None - using simple text similarity instead"""
    return None

def get_embedding(text, model=None):
    """Convert text to simple word frequency vector"""
    words = text.lower().split()
    return Counter(words)

def cosine_sim(vec1, vec2):
    """Compute cosine similarity between two word frequency vectors"""
    # Get intersection of words
    intersection = set(vec1.keys()) & set(vec2.keys())
    
    # Calculate dot product
    dot_product = sum([vec1[word] * vec2[word] for word in intersection])
    
    # Calculate magnitudes
    magnitude1 = math.sqrt(sum([vec1[word]**2 for word in vec1]))
    magnitude2 = math.sqrt(sum([vec2[word]**2 for word in vec2]))
    
    # Avoid division by zero
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    
    return dot_product / (magnitude1 * magnitude2)