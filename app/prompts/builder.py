# app/prompts/builder.py
from typing import List, Dict, Any

def build_helpdesk_prompt(
    user_query: str,
    classification: Dict[str, Any],
    snippets: List[Dict[str, str]]
) -> str:
    lines: List[str] = []
    
    # System prompt
    lines.append("You are an expert IT help desk assistant. Provide clear, concise, step-by-step guidance. Remove any ** from the response.")

    # Classification summary
    label = classification.get("label")
    confidence = classification.get("confidence")
    escalate = classification.get("escalate")
    lines.append(f"Category: {label} (confidence={confidence:.2f})")
    if escalate:
        lines.append("Note: This request may need escalation to a human agent.")
    lines.append("")

    # Retrieved context
    if snippets:
        lines.append("Context from knowledge base:")
        for i, s in enumerate(snippets, 1):
            lines.append(f"[{i}] (source: {s['id']}): {s['text']}")
        lines.append("")

    # User query
    lines.append(f"User Request: {user_query}")
    lines.append("Provide a helpful and complete response based on the above context.")
    
    return "\n".join(lines)
