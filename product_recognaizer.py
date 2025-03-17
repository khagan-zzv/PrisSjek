from openai import OpenAI
from agents import function_tool

from ai_prompts import img_recgonizer_prompt


@function_tool
def get_product(prdct_img: str) -> str:
    print(prdct_img)
    img_recgonizer = OpenAI()
    image_to_product = img_recgonizer.responses.create(
        model="gpt-4o-mini",
        # fine_tuning=name_of_file
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": f"{img_recgonizer_prompt}"},
                    {
                        "type": "input_image",
                        "image_url": f"{prdct_img}"
                    },
                ],
            }
        ],
    )
    # converting name to be able to user in search query
    final_product_name = image_to_product.output_text.split(":", 1)[1].strip()
    print(f"Product is: {final_product_name}")
    return final_product_name
