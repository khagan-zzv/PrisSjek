from openai import OpenAI
from agents import function_tool

from image_decoder import decode_image


@function_tool
def get_product(prdct_img: str) -> str:
    print(prdct_img)
    img_recgonizer = OpenAI()
    image_to_product = img_recgonizer.responses.create(
        model="gpt-4o-mini",
        #fine_tuning=name_of_file
        input=[
            {
                "role": "user",
                "content": [
                    { "type": "input_text", "text": "You are an intelligent AI that returns the full product name from an image in this format: Product:{product_name}. "
              "The product name should be something a user can search for online, such as 'iPhone 16 Pro', 'Jabra Elite 75t', or 'Philips AirFryer'. "
              "Do NOT return individual components or accessories (e.g., 'Jabra Charging Case' or 'Airfryer Handle'). "
              "If you are uncertain, return your best guess in this format: Assuming:{product_name}. "
              "Return only the product name in norwegian. Do not include any extra text or explanations." +
                                                    " ALWAYS FILL SPACES WITH + SIGN" },
                    {
                        "type": "input_image",
                        "image_url": f"{prdct_img}"
                    },
                ],
            }
        ],
    )
    #converting name to be able to user in search query
    final_product_name=image_to_product.output_text.split(":",1)[1].strip()
    print(f"Product is: {final_product_name}")
    return final_product_name