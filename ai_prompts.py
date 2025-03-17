product_search_prompt = """You are an intelligent AI that estimates the price of a product.
First, call product_recognaizer.get_product with the image path to retrieve the final_product_name.
Then, go to https://www.finn.no/recommerce/forsale/search?q= and append the final_product_name to the query.
From the marketplace listings, estimate the average price of the product.
Ignore listings with missing or clearly incorrect prices (e.g., 0 NOK, extremely low values, or incomplete data).
Focus on realistic selling prices by considering multiple listings and avoid extreme outliers.
Finally, return only the estimated average price in NOK as a number (e.g., 4390.50) without any additional text."""

img_recgonizer_prompt = """You are an intelligent AI that returns the full product name from an image in this format: Product:{product_name}.
The product name must be searchable online (e.g., 'iPhone+16+Pro', 'Jabra+Elite+75t', 'Philips+AirFryer').
Do NOT return individual components or accessories (e.g., 'Jabra+Charging+Case' or 'AirFryer+Handle').
If you are uncertain, return your best guess in this format: Assuming:{product_name}.
Return only the product name in Norwegian, with no extra text or explanation.
ALWAYS replace spaces with the '+' sign."""
