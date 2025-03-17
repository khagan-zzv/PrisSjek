import base64

#Can be used to decode image from local path to base64 and then use it in OpenAI Responses API
def decode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")