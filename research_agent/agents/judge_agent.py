from autogen import AssistantAgent
from research_agent.config import LLM_CONFIG

judge_agent = AssistantAgent(
    name="judge_agent",
    llm_config=LLM_CONFIG,
    system_message="""
You are evaluating a research-paper agent.

Return STRICT JSON only.

Fields:
- relevance (1-5)
- constraint_satisfaction (1-5)
- factual_accuracy (1-5)
- source_validity (1-5)
- explanation_quality (1-5)
- feedback (string)

Evaluation rules:

1. relevance
Does the paper match the requested topic?

2. constraint_satisfaction
Does it satisfy year and citation constraints?

3. factual_accuracy
Does the answer avoid hallucinations?

4. source_validity
Does it include valid DOI or URL?

5. explanation_quality
Is the explanation useful and clear?
"""
)
