from newsapi import NewsApiClient

# Initialize the News API client
newsapi = NewsApiClient(api_key="99d70feeab2d40b1826e49db65fb1ef4")  # Replace with your actual API key

keywords = 'weather OR air quality'




def fetchnews():
    # Fetch news articles based on the keywords
    articles = newsapi.get_everything(q=keywords)
    # print(articles['articles'][0])
    matrix = []
    news1 = articles['articles'][0]
    news1title = news1['title']
    news1url = news1['url']
    matrix.append((news1title,news1url))
    news2 = articles['articles'][1]
    news2title = news2['title']
    news2url = news2['url']
    matrix.append((news2title,news2url))
    print(matrix)
    # Print the titles and descriptions of the articles
    # for article in articles['articles']:
    #     print('Title:', article['title'])
    #     print('Description:', article['description'])
    #     print('Source:', article['source']['name'])
    #     print('URL:', article['url'])
    #     print('Published At:', article['publishedAt'])
    #     print('---')

fetchnews()