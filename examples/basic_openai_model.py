from agentforge.tool.Tool import Tool
from agentforge.tool.llm.llm import llm
from agentforge.tool.llm.openai_llm import openai_llm

tool = Tool('001')
llm_model = llm(model='gpt-4o')
model = openai_llm(api_key="your-api-key")

print(model)