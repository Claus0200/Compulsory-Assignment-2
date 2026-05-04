import requests

def search_papers(query: str, limit: int = 10):
    url = "https://api.openalex.org/works"

    params = {
        "search": query,
        "per-page": limit
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return []

    data = response.json().get("results", [])

    papers = []

    for item in data:
        papers.append({
            "title": item.get("display_name"),
            "authors": [
                a["author"]["display_name"]
                for a in item.get("authorships", [])
                if "author" in a
            ],
            "year": item.get("publication_year"),
            "citationCount": item.get("cited_by_count", 0),
            "url": item.get("id"),
            "doi": item.get("doi"),
            "abstract": item.get("abstract_inverted_index")  # optional raw form
        })

    return papers