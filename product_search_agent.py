from agents import WebSearchTool, ModelSettings, Agent
import product_recognaizer
from price_model import PriceModel

product_search_Agent = Agent(
    name="Web Search Agent",
    instructions=f"You are an intellegent AI which estimates price of the products."
                 f"You should first call product_recognaizer.get_product, pass image path to it and that will return you the final_product_name"
                 f"You should then go to this website: https://www.finn.no/recommerce/forsale/search?q= and append final_product_name to the end of the query. Estimate the average price of the product based on listings in the marketplace. "
          "Ignore listings with missing or clearly incorrect prices (e.g., 0 NOK, unusually low values, or incomplete data). "
          "Focus on extracting realistic selling prices by considering multiple listings or searching in the web and avoid extreme outliers. "
          "Calculate the average price based on the most relevant listings in the FINN marketplace. "
          "Return only the estimated average price in NOK as a number (e.g., 4390.50) without any extra text.",
    tools=[WebSearchTool() ,product_recognaizer.get_product],
    output_type=PriceModel,
    model_settings=ModelSettings(temperature=0.0)
)