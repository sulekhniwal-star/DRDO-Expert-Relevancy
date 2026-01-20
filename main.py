#!/usr/bin/env python3
"""
DRDO RAC Expert Matching System
For interview board expert selection
"""

from data_utils import load_profiles, clean_text
from embedding_utils import load_model, get_embedding
from scoring import subject_matching_score, profile_matching_score, experience_score
from relevancy import compute_relevancy_score

def main():
    print("DRDO RAC Expert Matching System")
    print("=" * 50)
    
    # Load data
    experts = load_profiles('experts.json')
    candidates = load_profiles('candidates.json')
    
    with open('subject.txt', 'r', encoding='utf-8') as f:
        subject_text = f.read().strip()
    
    # Load model
    model = load_model()
    
    # Clean texts
    subject_clean = clean_text(subject_text)
    candidate_clean = clean_text(candidates[0]['profile_text'])
    
    print(f"Interview Subject: {subject_text[:80]}...")
    print(f"Candidate Profile: {candidates[0]['name']}")
    print("\nExpert Suitability Analysis:")
    print("-" * 80)
    
    # Compute matching and relevancy scores
    expert_results = []
    
    for expert in experts:
        expert_clean = clean_text(expert['profile_text'])
        
        # Calculate matching scores
        subject_match = subject_matching_score(expert_clean, subject_clean, model)
        profile_match = profile_matching_score(expert_clean, candidate_clean, model)
        exp_score = experience_score(expert['years_experience'])
        
        # Calculate relevancy score
        relevancy = compute_relevancy_score(subject_match, profile_match, exp_score)
        
        expert_results.append({
            'name': expert['name'],
            'subject_matching_score': subject_match,
            'profile_matching_score': profile_match,
            'experience_score': exp_score,
            'relevancy_score': relevancy
        })
    
    # Sort by relevancy score
    expert_results.sort(key=lambda x: x['relevancy_score'], reverse=True)
    
    # Display results
    for i, expert in enumerate(expert_results, 1):
        print(f"{i}. {expert['name']}")
        print(f"   Subject Matching Score:  {expert['subject_matching_score']:.3f}")
        print(f"   Profile Matching Score:  {expert['profile_matching_score']:.3f}")
        print(f"   Experience Score:        {expert['experience_score']:.3f}")
        print(f"   Relevancy Score:         {expert['relevancy_score']:.3f}")
        
        # Suitability prediction
        if expert['relevancy_score'] >= 0.7:
            suitability = "Highly Suitable"
        elif expert['relevancy_score'] >= 0.5:
            suitability = "Suitable"
        else:
            suitability = "Less Suitable"
        
        print(f"   Suitability:             {suitability}")
        print()

if __name__ == "__main__":
    main()