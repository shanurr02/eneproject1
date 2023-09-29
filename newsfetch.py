from newsapi import NewsApiClient

# Initialize the News API client with your API key
newsapi = NewsApiClient(api_key="99d70feeab2d40b1826e49db65fb1ef4")  # Replace with your actual API key

def fetch_news(num_articles=2):
    keywords = 'weather OR air quality'
    """
    Fetches news articles based on provided keywords.

    Args:
        num_articles (int): Number of articles to fetch (default is 2).

    Returns:
        list: List of tuples containing (title, url) for each news article.
    """
    # Fetch news articles based on the keywords
    articles = newsapi.get_everything(q=keywords)

    # Extract titles and URLs for the specified number of articles
    news_list = []
    for article in articles['articles'][:num_articles]:
        news_list.append((article['title'], article['url']))

    return news_list

if __name__ == "__main__":
    # Fetch and print the latest news
    news_articles = fetch_news(num_articles=2)
    for index, (title, url) in enumerate(news_articles, start=1):
        print(f"News {index}:")
        print(f"Title: {title}")
        print(f"URL: {url}")
        print("---")
