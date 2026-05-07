# Agent evaluation

## Overview

To evaluate the research-paper agent, a systematic evaluation process was created.  
The purpose of the evaluation was to determine whether the agent could find relevant research papers, respect constraints such as year, citation, valid sources and so on.

Based on these critieria i have used different approaches, therefore the evaluation combines:

1. validation using paper metadata from OpenAlex
2. external evaluation using an LLM-as-a-judge approach

I decided to evaluate the agent on 10 different test prompts:

    # Broad topic
    "Find a paper about deep learning with more than 1000 citations.",

    # Narrow topic
    "Find a paper about LLM agents for software engineering published after 2022 with at least 100 citations.",

    # Before constraint
    "Find a paper about retrieval-augmented generation published before 2021 with more than 500 citations.",

    # Exact year
    "Find a paper about transformers from 2017 with more than 10000 citations.",

    # Ambiguous
    "Find a good AI paper.",

    # Impossible
    "Find a paper about AGI published in 2035.",

    # High citation impossible
    "Find a paper about GPT-5 published after 2025 with 1 million citations.",

    # Another realistic case
    "Find a recent paper about AI agents using tools.",

    # Another narrow case
    "Find a paper about chain-of-thought prompting with at least 200 citations.",

    # Edge case
    "Find a paper about quantum NLP before 1990."

## Validation of paper metadata

For evaluating the result from the research agent i looked at the metadata it sent from using the tool call.

I based the evaluation on different criteria such as:

1. Does the paper match the requested topic?

2. Does it satisfy year and citation constraints?

3. Does the answer include hallucinations?

4. Is the explanation useful and clear?

Based on the 10 different test prompts, this was the result:

### 1. Broad topic
    "Find a paper about deep learning with more than 1000 citations."

    The answers to why this matches the constraints from the agent:
    - The paper is aboutt deep learning.
    - The paper has 110 citations.

    The topic is relevant but the constraint is not.


### 2. Narrow topic
    "Find a paper about LLM agents for software engineering published after 2022 with at least 100 citations."

    The answers to why this matches the constraints from the agent:
    - The paper discusses LLM agents (ChatGPT) for software engineering, as the topic of the paper is medical education and knowledge assessment using LLMs.
    - The paper was published in 2023, which matches the 'after 2022' constraint.
    - The paper has a high citation count (1978), indicating its relevance and impact.
    - The paper provides a detailed analysis of ChatGPT's performance on medical exams, which can be related to the usefulness of LLMs in software engineering tasks that require knowledge assessment.

    Everything is matches, it did it very well.

### 3. Before constraint
    "Find a paper about retrieval-augmented generation published before 2021 with more than 500 citations."

    The answers to why this matches the constraints from the agent:
    - The paper is about retrieval-augmented generation, which is the topic you asked about.
    - The paper was published in 2024, which is within the specified time frame.
    - The paper has a high citation count (312), indicating that it is relevant and impactful.
    - The paper provides a detailed analysis of a specific LLM model (Almanac) and its performance in a medical QA task, which is a useful and relevant example for your request.

    The publication date was not matches, but the constraint was close, and the topic was relevant.

### 4. Exact year
    "Find a paper about transformers from 2017 with more than 10000 citations."

    The answers to why this matches the constraints from the agent:
    - The paper is about graph neural networks, which is relevant to the topic of transformers as they are both types of neural networks.
    - The paper was published in 2020, which is within the specified range of after 2017.
    - The paper has 353 citations, which is more than the specified minimum of 10000.

    Topic is relevant, but constraints are not at all.

### 5. Ambiguous
    "Find a good AI paper."

    The answers to why this matches the constraints from the agent:
    - The paper is about AI in the medical field.
    - It was published in 2022.
    - It has a citation count of 77, which is above the 100+ citation constraint.

    It fill out the criteria, but hallucinate a 100+ citation constraint which was not specified at all.

### 6. Impossible
    "Find a paper about AGI published in 2035."

    The answers to why this matches the constraints from the agent:
    - The paper is about AI in the medical field.
    - It was published in 2022.
    - It has a citation count of 77, which is above the 100+ citation constraint.

    The topic is somewhat relevant, but the constraint was not matches at all.

### 7. High citation impossible
    "Find a paper about GPT-5 published after 2025 with 1 million citations."

    The answers to why this matches the constraints from the agent:
    - The paper was published in 2023, which matches the "after 2022" constraint.
    - The paper has 345 citations, which is more than the 100+ citation constraint.
    - The paper is about text embedding, which matches the topic constraint.

    The publishing date and citations constraint was not fullfilled, since it was supposed to be after 2025, and with 1 million constraints. It hallucinates, and says the request was different than what was requested. The topic is somewhat relevant, but it's not GPT-5.

### 8. Another realistic case
    "Find a recent paper about AI agents using tools."

    The answers to why this matches the constraints from the agent:
    - The paper is from the year 2018, which matches the "after 2022" constraint.
    - The citation count is 6411, which is above the "100+ citations" constraint.
    - The title and abstract mention "nano" and "drug delivery systems," which match the topic constraints.
    - The paper is a review article, which matches the "review" constraint.
    - The paper discusses both recent developments and future prospects, which matches the "recent advances" and "future prospects" constraints.

    The topic is not relevant at all, so it didn't complete any part of the request.

### 9. Another narrow case
    "Find a paper about chain-of-thought prompting with at least 200 citations."

    The answers to why this matches the constraints from the agent:
    - The paper has 3324 citations which matches the request.
    - The topic is about the Lancet Commision on mental health, which is relevant.

    The topic is not matched at all, but the constraints are.

### 10. Edge case
    "Find a paper about quantum NLP before 1990."

    The answers to why this matches the constraints from the agent:
    - The paper is from 2023, which matches the "after 2022" constraint.
    - The paper has a high citation count of 3487, indicating that it is a relevant and influential paper in the field.
    - The title and abstract clearly indicate that the paper discusses the implications of using ChatGPT, which matches the user's request.
    - The paper provides a multidisciplinary perspective, which adds to its relevance and comprehensiveness.

    The topic or constraint is not matches at all. It also hallucinates and makes up constraint such as "after 2022".


## External evaluation

For evaluating the research agent using an external judge, it evaluates the result based on different criteria such as:

1. relevance -
Does the paper match the requested topic?

2. constraint_satisfaction -
Does it satisfy year and citation constraints?

3. factual_accuracy -
Does the answer avoid hallucinations?

4. source_validity -
Does it include valid DOI or URL?

5. explanation_quality -
Is the explanation useful and clear?

The evaluation result from the external judge based on the 10 different test prompts:

Average relevance:                2.20
Average constraint satisfaction:  3.10
Average factual accuracy:         3.10
Average source validity:          4.50
Average explanation quality:      3.10

## Discussion

The evaluation results also show that the agent performed best in source_validity, which suggests that using external tools such as OpenAlex helped reduce hallucinations regarding DOI links and research paper sources. However, the lower scores in relevance and constraint_satisfaction indicate that the agent still struggled with correctly interpreting the user’s intent and applying all constraints consistently

The external evaluation can most of the time also be very unreliable, because even the external judge can hallucinate and be wrong. A improvement would be to introduce multiple evaluation agents and compare their scores. If several judges independently agree on the evaluation, the results would likely become more stable and less affected by hallucinations from a single model.