#!/usr/bin/env python3
"""
DRDO Expert Relevancy Matching System
Main execution script
"""

from data_utils import load_profiles, clean_text
from embedding_utils import load_model, get_embedding
from scoring import subject_score, profile_score, experience_score
from relevancy import compute_relevancy

def main():
    print("DRDO Expert Relevancy Matching System")
    print("=" * 50)
    
    # Load data
    experts = load_profiles('experts.json')
    candidates = load_profiles('candidates.json')
    
    with open('subject.txt', 'r', encoding='utf-8') as f:
        subject_text = f.read().strip()
    
    # Load embedding model
    model = load_model()
    
    # Clean texts
    subject_clean = clean_text(subject_text)
    candidate_clean = clean_text(candidates[0]['profile_text'])
    
    print(f"Subject: {subject_text[:100]}...")
    print(f"Candidate: {candidates[0]['name']}")
    print("\nExpert Relevancy Rankings:")
    print("-" * 80)
    
    # Compute scores for each expert
    expert_scores = []
    
    for expert in experts:
        expert_clean = clean_text(expert['profile_text'])
        
        # Calculate individual scores
        subj_score = subject_score(expert_clean, subject_clean, model)
        prof_score = profile_score(expert_clean, candidate_clean, model)
        exp_score = experience_score(expert['years_experience'])
        
        # Calculate final relevancy
        relevancy = compute_relevancy(subj_score, prof_score, exp_score)
        
        expert_scores.append({
            'name': expert['name'],
            'subject_score': subj_score,
            'profile_score': prof_score,
            'experience_score': exp_score,
            'relevancy_score': relevancy
        })
    
    # Sort by relevancy score (descending)
    expert_scores.sort(key=lambda x: x['relevancy_score'], reverse=True)
    
    # Print top 5 experts
    for i, expert in enumerate(expert_scores[:5], 1):
        print(f"{i}. {expert['name']}")
        print(f"   Subject Match:    {expert['subject_score']:.3f}")
        print(f"   Profile Match:    {expert['profile_score']:.3f}")
        print(f"   Experience Score: {expert['experience_score']:.3f}")
        print(f"   Final Relevancy:  {expert['relevancy_score']:.3f}")
        print()

if __name__ == "__main__":
    main()