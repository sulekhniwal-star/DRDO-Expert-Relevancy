"""
Scoring functions for DRDO RAC expert matching
"""

from embedding_utils import get_embedding, cosine_sim

def subject_matching_score(expert_text, subject_text, model):
    """Compute matching score between expert domain and interview subject"""
    expert_emb = get_embedding(expert_text, model)
    subject_emb = get_embedding(subject_text, model)
    return cosine_sim(expert_emb, subject_emb)

def profile_matching_score(expert_text, candidate_text, model):
    """Compute matching score between expert profile and candidate profile"""
    expert_emb = get_embedding(expert_text, model)
    candidate_emb = get_embedding(candidate_text, model)
    return cosine_sim(expert_emb, candidate_emb)

def experience_score(years_experience):
    """Compute normalized experience score"""
    return min(1.0, years_experience / 25.0)