from research_agent.agents.agent import assistant, user_proxy


def main():
    user_proxy.initiate_chat(
        assistant,
        message=
        """
            Find a research paper about LLM agents for software engineering that was published after 2022 and has at least 100 citations. Explain why the paper is relevant and provide the source of the citation count.
        """,
        max_turns=2
    )


if __name__ == "__main__":
    main()
