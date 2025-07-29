### FILE: processor/ranker.py

from sentence_transformers import SentenceTransformer, util
import numpy as np

# Load sentence transformer model (lightweight for Docker)
model = SentenceTransformer("all-MiniLM-L6-v2")

def rank_sections(sections, persona, job):
    # Combine persona and job to form the query
    query = f"{persona.strip()} needs to: {job.strip()}"
    query_embedding = model.encode(query, convert_to_tensor=True)

    ranked = []
    for section in sections:
        combined_text = f"{section.get('section_title', '')}.\n{section.get('text', '')}"
        section_embedding = model.encode(combined_text, convert_to_tensor=True)
        score = util.pytorch_cos_sim(query_embedding, section_embedding).item()
        section_with_score = dict(section)
        section_with_score["score"] = float(score)
        ranked.append((score, section_with_score))

    # Sort sections by score descending
    ranked.sort(key=lambda x: x[0], reverse=True)

    # Attach importance rank
    final_output = []
    for i, (score, sec) in enumerate(ranked):
        sec["importance_rank"] = i + 1
        final_output.append(sec)

    return final_output

