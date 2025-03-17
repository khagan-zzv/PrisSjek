from agents import Runner
import asyncio
from product_search_agent import product_search_Agent

image_pat = "https://images.finncdn.no/dynamic/1600w/00/000c52ac-7ede-4d20-a135-490537552ebe"
async def main():
    result = await Runner.run(product_search_Agent, f"What's average price of the {image_pat}?")
    print(f"Average price for is around: {result.final_output.prices} NOK")



if __name__ == "__main__":
   asyncio.run(main())