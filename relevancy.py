"""
Relevancy score computation for DRDO RAC expert selection
"""

def compute_relevancy_score(subject_matching_score, profile_matching_score, experience_score, w1=0.4, w2=0.4, w3=0.2):
    """
    Compute final relevancy score for expert suitability prediction
    
    Args:
        subject_matching_score: Expert-subject domain match (0-1)
        profile_matching_score: Expert-candidate profile match (0-1)
        experience_score: Experience score (0-1)
        w1: Weight for subject matching (default: 0.4)
        w2: Weight for profile matching (default: 0.4)
        w3: Weight for experience (default: 0.2)
    
    Returns:
        Relevancy score for suitability prediction (0-1)
    """
    return w1 * subject_matching_score + w2 * profile_matching_score + w3 * experience_score