from research_agent.agents.research_agent import (
    research_agent,
    user_proxy
)


def main():
    user_proxy.initiate_chat(
        research_agent,
        message="""
            Find a recent paper about ChatGPT and summarize it in a few sentences.
        """,
        max_turns=2
    )


if __name__ == "__main__":
    main()
