"""
Relevancy computation using weighted scoring
"""

def compute_relevancy(subject_score, profile_score, experience_score, w1=0.4, w2=0.4, w3=0.2):
    """
    Compute final relevancy score using weighted combination
    
    Args:
        subject_score: Expert-subject similarity (0-1)
        profile_score: Expert-candidate similarity (0-1)
        experience_score: Experience score (0-1)
        w1: Weight for subject score (default: 0.4)
        w2: Weight for profile score (default: 0.4)
        w3: Weight for experience score (default: 0.2)
    
    Returns:
        Final relevancy score (0-1)
    """
    return w1 * subject_score + w2 * profile_score + w3 * experience_score