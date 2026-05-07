test_prompts = [
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
]