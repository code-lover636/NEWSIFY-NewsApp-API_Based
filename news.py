import requests


def getnews(**kwargs):
    """
    Get news from newsapi.org
    """
    headlines = "https://newsapi.org/v2/top-headlines?"
    everything = "https://newsapi.org/v2/everything?"
    url = headlines
    params = {
        "language": "en",
        "apiKey": "df1128eacb9b41939638e53ca9478925",
    }
    if "q" in params:   url = everything
    for key, value in kwargs.items():   params[key] = value 
    print(url,params)
    results = requests.get(url, params=params)
    response = results.json()
    data = []
    for n in range(len(response["articles"])):
        try:
            data.append({
                "title": response['articles'][n]["title"],
                "author": response['articles'][n]["author"],
                "source": response['articles'][n]["source"]["name"],
                "url": response['articles'][n]["url"],
                "image": response['articles'][n]["urlToImage"],
                "date": response['articles'][n]["publishedAt"][:10],
                "description": response['articles'][n]["description"],
                "content": response['articles'][n]["content"][:-14],
            })
        except KeyError:
            return{"error": "No news found"}
        except TypeError:
            continue
    
    return data if data!=[] else {"error": "No news found"}

    

if __name__ == "__main__":
    data = getnews(q="adfasdf")
    print(data)