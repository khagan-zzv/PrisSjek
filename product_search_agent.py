from agents import WebSearchTool, ModelSettings, Agent
import product_recognaizer
from ai_prompts import product_search_prompt
from price_model import PriceModel

product_search_Agent = Agent(
    name="Web Search Agent",
    instructions=f"{product_search_prompt}",
    tools=[WebSearchTool() ,product_recognaizer.get_product],
    output_type=PriceModel,
    model_settings=ModelSettings(temperature=0.0)
)