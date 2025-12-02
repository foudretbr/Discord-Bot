import requests
import os
import random
from pexels_api import API
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv("PEXELS_API_KEY")
api = API(API_KEY)
api.search("koala")
print("Total results: ", api.total_results)
# Loop all the pages
for i in range(1):
    # Get all photos in the page
    photos = api.get_entries()
    # For each photo print its properties
    for photo in photos:
        print("-----------------------------------------------")
        # print("Photo id: ", photo.id)
        # print("Photo width: ", photo.width)
        # print("Photo height: ", photo.height)
        # print("Photo url: ", photo.url)
        # print("Photographer: ", photo.photographer)
        # print("Photo description: ", photo.description)
        # print("Photo extension: ", photo.extension)
        # print("Photo sizes:")
        print("\toriginal: ", photo.original)
        # print("\tcompressed: ", photo.compressed)
        # print("\tlarge2x: ", photo.large2x)
        # print("\tlarge: ", photo.large)
        # print("\tmedium: ", photo.medium)
        # print("\tsmall: ", photo.small)
        # print("\ttiny: ", photo.tiny)
        # print("\tportrait: ", photo.portrait)
        # print("\tlandscape: ", photo.landscape)
    # If there is no next page print the last page and end the loop
    if not api.has_next_page:
        print("Last page: ", api.page)
        break
    # Search next page
    api.search_next_page()

class API_CLASS():
    def __init__(self):
        self.key = API_KEY

# def main():
#     response = requests.get(
#         "https://api.github.com/search/repositories",
#         params={"q": "language:python", "sort": "stars", "order": "desc"},
#     )

#     json_response = response.json()
#     popular_repositories = json_response["items"]
#     for repo in popular_repositories[:3]:
#         print(f"Name: {repo['name']}")
#         print(f"Description: {repo['description']}")
#         print(f"Stars: {repo['stargazers_count']}\n")

# main()

