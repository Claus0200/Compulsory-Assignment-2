import json
from statistics import mean

from research_agent.agents.research_agent import (
    research_agent,
    user_proxy
)

from research_agent.agents.judge_agent import judge_agent

from research_agent.evaluation.test_prompts import test_prompts


def evaluate_prompt(prompt: str):

    print("\n==============================")
    print("PROMPT:")
    print(prompt)
    print("==============================\n")

    # RUN RESEARCH AGENT
    chat_result = user_proxy.initiate_chat(
        research_agent,
        message=prompt,
        max_turns=2
    )

    # EXTRACT FINAL ANSWER
    final_answer = chat_result.chat_history[-1]["content"]

    print("FINAL ANSWER:\n")
    print(final_answer)

    # BUILD JUDGE PROMPT
    judge_prompt = f"""
    User request:
    {prompt}

    Agent response:
    {final_answer}

    Evaluate the response.

    Return STRICT JSON only.
    """

    # RUN JUDGE
    judge_response = judge_agent.generate_reply(
        messages=[
            {
                "role": "user",
                "content": judge_prompt
            }
        ]
    )

    print("\nJUDGE EVALUATION:\n")

    try:
        scores = json.loads(judge_response["content"])

        print(json.dumps(scores, indent=2))

        # RETURN RESULTS
        return {
            "prompt": prompt,
            "final_answer": final_answer,
            "judge_scores": scores
        }

    except Exception:
        print(judge_response)

        return {
            "prompt": prompt,
            "final_answer": final_answer,
            "judge_scores": {}
        }


def main():

    results = []

    # RUN ALL PROMPTS
    for prompt in test_prompts:
        result = evaluate_prompt(prompt)
        results.append(result)

    # CALCULATE AVERAGES
    def avg(metric: str):

        valid_scores = [
            r["judge_scores"][metric]
            for r in results
            if metric in r["judge_scores"]
        ]

        if not valid_scores:
            return 0

        return mean(valid_scores)

    print("\n==============================")
    print("SUMMARY")
    print("==============================")

    print(f"Average relevance:                {avg('relevance'):.2f}")
    print(f"Average constraint satisfaction:  {avg('constraint_satisfaction'):.2f}")
    print(f"Average factual accuracy:         {avg('factual_accuracy'):.2f}")
    print(f"Average source validity:          {avg('source_validity'):.2f}")
    print(f"Average explanation quality:      {avg('explanation_quality'):.2f}")


if __name__ == "__main__":
    main()