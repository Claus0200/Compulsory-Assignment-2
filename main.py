from research_agent.agents.agent import assistant, user_proxy


def main():
    user_proxy.initiate_chat(
        assistant,
        message=
        """
            Find a paper about LLM agents for software engineering
            published after 2022 with at least 100 citations.
        """,
        max_turns=5
    )


if __name__ == "__main__":
    main()
