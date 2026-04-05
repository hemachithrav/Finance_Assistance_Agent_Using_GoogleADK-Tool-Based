from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool
from investment_plan_agent.agent import investment_plan_agent
from typing import Dict

# Add custom tools below is a custom function which has user personal details likeweise in real scenarios we can integrate with DB

def get_user_personal_finance_details() -> Dict:
    """
    Gets user's personal finance details like salary, expense and savings capacity.
    """
    return {
        "salary": 50000,
        "expense": {
            "EMI_Expense": 25000,
            "Essentials": 5000,
            "Entertainment": 5000,
            "Shopping and Travel": 5000
        },
        "savings": 10000
    }
    #Always mention the return type for agentic codes
#Always use a docstring in agentic codes for custom functions

finance_assistance_agent=LlmAgent(
    name="finance_assistance_agent",
    model='gemini-2.5-flash',
    description="A simple finance assistance that helps with user's finance goals,", #For other agents to know what this agent do
    instruction="""You are a friendly finance assistant. 
                You can help answer users' generic questions on finance and help plan their finance goals. 
                Be more friendly and positive. 
                
                You have two tools to use to complete your task: 
                1.  get_user_personal_finance_details  - This tool will give you the user's current finance information. 
                2.  investment_plan_agent  - This tool can perform Google search to get any 
                   latest information from the websites and will be able to ask more details from the user and plan their savings goals. 
                   Always use the Investment Plan Agent with Google search tool when asked about stock prices, market data, any question.


                Always use the google_search tool when asked about:
                --Stock prices(e.g, "Tesla Stock Prices","TSLA Latest price")
                --Market data, financial news,or company information
                --Any question containing words like "latest","current","today","now",recent

                After searching provide the financial data from the search results with specific numbers
                """,
    tools=[AgentTool(investment_plan_agent),get_user_personal_finance_details] # Will do google search 
    
    # Constraints of ADK: 1. Can't pass one custom and one inbuild tool,many custom tools can be passed.
    #2. Only 1 inbuild tool can be used
    #3. So we using Agent tool library built an agent separately and calling it here

   
)

root_agent = finance_assistance_agent 
#First which agent starts while running in google adk.Note:Always assign a root_agent to run.