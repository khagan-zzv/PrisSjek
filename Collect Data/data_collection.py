import json
import time
import requests
from bs4 import BeautifulSoup

#delay added to avoid getting blocked by the website
def scrape_finn(search_query, max_pages=3, delay=15):
    jsonl_data = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    for page in range(1, max_pages + 1):
        url = f"https://www.finn.no/recommerce/forsale/search?page={page}&q={search_query}"
        print(f"Scraping page {page}/{max_pages}")

        try:
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            listings = soup.select("article")
            print(f"Found {len(listings)} listings on page {page}")

            for listing in listings:
                ad_name_tag = listing.select_one("h2 a")
                image_tag = listing.select_one("img")

                if ad_name_tag and image_tag and "src" in image_tag.attrs:
                    ad_name = ad_name_tag.text.strip()
                    image_url = image_tag["src"]

                    # Create JSONL entry
                    entry = {
                        "messages": [
                            {"role": "system", "content": "You are an assistant that identifies product name."},
                            {"role": "user", "content": "What product is this?"},
                            {
                                "role": "user",
                                "content": [
                                    {
                                        "type": "image_url",
                                        "image_url": {"url": image_url}
                                    }
                                ]
                            },
                            {"role": "assistant", "content": ad_name}
                        ]
                    }
                    jsonl_data.append(entry)

            print("Waiting before next request...")
            time.sleep(delay)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page}: {e}")
            break

    print(f"Scraping completed. Collected {len(jsonl_data)} entries total.")
    return jsonl_data


def save_to_jsonl(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for entry in data:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"Data saved to '{filename}'")


def main():
    search_query = "iPhone"
    max_pages = 3
    output_file = f"finn_listings_{search_query.lower()}.jsonl"
    scraped_data = scrape_finn(search_query, max_pages)
    save_to_jsonl(scraped_data, output_file)


if __name__ == "__main__":
    main()