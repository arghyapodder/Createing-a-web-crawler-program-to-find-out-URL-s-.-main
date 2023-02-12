import requests
from bs4 import BeautifulSoup
import csv

def web_crawler(category, subcategory, geography, date_range):
    # Replace with a list of websites to search
    websites = [
        "https://www.example1.com",
        "https://www.example2.com"
    ]
    urls = []
    for website in websites:
        page = requests.get(website)
        soup = BeautifulSoup(page.content, "html.parser")
        for link in soup.find_all("a"):
            url = link.get("href")
            # Check if the URL meets the criteria (category, subcategory, geography, date_range)
            if (
                # Add your own conditions to check the URL
                url.startswith("http")
                and "category" in url
                and "subcategory" in url
                and "geography" in url
                and "date_range" in url
            ):
                urls.append(url)

    # Write the output to a CSV file
    with open("output.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["URL"])
        for url in urls:
            writer.writerow([url])

if _name_ == "_main_":
    web_crawler("Medical Journal", "Orthopedic", "India", "2022")