from autogen import AssistantAgent, UserProxyAgent, register_function

from research_agent.config import LLM_CONFIG
from research_agent.tools.research_tool import search_papers


assistant = AssistantAgent(
    name="ResearchAgent",
    llm_config=LLM_CONFIG,
    system_message="""
You are a research assistant.

Your job is to:
1. Understand research paper requests
2. Extract constraints:
   - topic
   - year constraints
   - citation constraints
3. Use the provided tool
4. Never invent citation counts
5. Reject papers that do not satisfy constraints
6. Return structured answers
"""
)

user_proxy = UserProxyAgent(
    name="UserProxy",
    human_input_mode="NEVER",
    code_execution_config=False,
)

# Register tool
register_function(
    search_papers,
    caller=assistant,
    executor=user_proxy,
    name="search_papers",
    description="Search for research papers by topic",
)