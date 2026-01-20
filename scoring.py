"""
Scoring functions for expert relevancy computation
"""

from embedding_utils import get_embedding, cosine_sim

def subject_score(expert_text, subject_text, model):
    """Compute similarity between expert profile and interview subject"""
    expert_emb = get_embedding(expert_text, model)
    subject_emb = get_embedding(subject_text, model)
    return cosine_sim(expert_emb, subject_emb)

def profile_score(expert_text, candidate_text, model):
    """Compute similarity between expert and candidate profiles"""
    expert_emb = get_embedding(expert_text, model)
    candidate_emb = get_embedding(candidate_text, model)
    return cosine_sim(expert_emb, candidate_emb)

def experience_score(years_experience):
    """Compute experience score normalized to [0, 1]"""
    return min(1.0, years_experience / 25.0)