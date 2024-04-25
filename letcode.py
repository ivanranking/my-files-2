import cloudscraper

def fetch_leetcode_information(query=""):
    """
    Fetches leetcode information from a given API based on the query parameter.

    Args:
    query (str): The query to filter the results, defaults to an empty string.

    Returns:
    dict: Key-value pairs extracted from the fetched JSON data.
    """
    base_url = "https://mukesh-api.vercel.app/leetcode"
    if query:
        url = f"{base_url}?query={query}"
    else:
        query = input("Please enter a query: ")
        url = f"{base_url}?query={query}"

    scraper = cloudscraper.create_scraper()
    response = scraper.get(url).json()
    return response.get("results", {})


# example 
query = "noob-mukesh"
data = fetch_leetcode_information(query)

for key, value in data.items():
    print(f"{key}: {value}")
