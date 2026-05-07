# Compulsory-Assignment-2

## Setup instructions

To setup the project, you need to follow the instructions below:

1. Clone the repository using 'git clone https://github.com/Claus0200/Compulsory-Assignment-2.git'
2. Download the dependencies using 'pip install -r requirements.txt'
3. Setup up API key through an enviroment variable called 'MISTRAL_API_KEY'
4. Run the program using ```python main.py``` in root folder

The steps are more detailed below


## Dependency installation

To install the necessary dependencies, run 'pip install -r requirements.txt'.
This will install the following:

```
autogen-agentchat @ git+https://github.com/patrickstolc/autogen.git@0.2#egg=autogen-agentchat
autogen==0.3.1
mistralai==1.2.3
ollama==0.3.3
fix-busted-json==0.0.18
pyautogen==0.5.3
```


## How to configure the API key

To configure the API Key, you need to setup an environment variable either through you IDE, cli or .env file.

The variable you need to set is 'MISTRAL_API_KEY'. Example: 'MISTRAL_API_KEY=kgiwadiga08enga12'

For OpenAlex there is currently no need for an API Key.


## How the run the agent

To run the agent, you need to run the program using ```python main.py``` in the root folder. 

If you wish to run the agent with an external judge, and specific test prompts, then use ```python test_agent.py```

## Evaluation results

The evaluation results have been moved to a seperate .md file, called evaluation.md, which is located in the root folder.

## Group member contributions

This project was made by me, Claus Peter Jørgensen


# Reflection

## What worked well?

What worked well was that the agent was reliable enough to use the tool functions correctly. It very rarely used them incorrectly.

## What failed or was unreliable?

The unreliable part of the agent was the papers it found. Most of the time, it did not follow the specific constraints, such as finding a paper published before 2020. Instead it would sometimes return papers from 2025.

## How often did the agent need tool calls?

The agent always needed tool calls since it relies on retrieving data from external sources and then presenting the response to the user in a better format.

## Did the LLM ever hallucinate?

Yes, many times it hallucinated. Most often, this happened when asking for something specific related to AI. It would sometimes ignore the rules, fail to use the tool for external sources, and instead make up information.

## How did you prevent incorrect answers?

It is not possible to completely prevent incorrect answers, and it also varies depending on the user’s request. Most of the effort went into structuring what the agent was capable of and defining the rules it needed to follow. If there was too many rules, it would often miss some of them. It also helped to follow a clear structure describing what it needed to do and what output it should provide.

## What would you improve with more time?

I would probably continue refining the requirements and rules the agent should follow until it consistently produced much better responses. This process is very time-consuming. I would also explore implementing an internal evaluation system, where a different agent provides feedback to the research agent back and forth before returning the paper to the external judge agent.