# Pris Sjek

## Overview

PrisSjek is a Proof of Concept (POC) application that allows users to easily check the average price of an item by
simply uploading a picture. The system extracts the product name from the image and searches FINN.no for its average
price, presenting the results to the user.

## Process Flow
1. User Uploads an Image: The user takes a picture of an item and submits it. 
2. Product Recognition: AI extracts the product name from the image. 
3. Automated Price Lookup: OpenAI Agent searches for similar items on FINN.no.
4. Average Price Calculation: Agent calculates the average price of the item based on search results.
5. Results Displayed: The user sees the estimated price.

## Technologies
The project uses OpenAI's latest tools: Agents SDK and Responses API.
* Agent is being used for calling product recognition which would return product name and look up average price on FINN.no.
* Responses API is being used for analyzing the image and returning the product name.

## Limitations 
Responses API does not always return most accurate results which is due to data it's trained.
In order to improve its responses we need to fine-tune model with more data. \
One of the ways to get more data to train model is scraping data from finn.no and using it. Main idea is
to get product name and product image from already published ads on finn.no and save them in jsonl format. \
This has been done in datacollection.py file and below is example of line which can be used to fine-tine model.
```json lines
{
  "messages": [
    {
      "role": "system",
      "content": "You are an assistant that identifies product name."
    },
    {
      "role": "user",
      "content": "What product is this?"
    },
    {
      "role": "user",
      "content": [
        {
          "type": "image_url",
          "image_url": {
            "url": "https://images.finncdn.no/dynamic/480w/2024/4/vertical-5/25/8/350/185/338_ab0018a6-5d0c-4015-ac83-b7cb847dba1a.jpg"
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": "Nesten ny iPhone med 2 års garanti & 1-3 dagers levering"
    }
  ]
}

```
Later the file should be uploaded to OpenAI and can be used:
```python
image_to_product = img_recgonizer.responses.create(
        model="gpt-4o-mini",
        fine_tuning=name_of_file
        input=...
```


