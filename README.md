# AINewsTracker
AINewsTracker

# AINewsTracker

AINewsTracker is a powerful web application dedicated to backtesting the influence of financial news on the stock market. Leveraging AI to sort, filter, and analyze financial news from various reliable international and regional sources, it enables users to observe and predict potential impacts on market trends. 

## Features

- **Real-time tracking of financial news**: Get up-to-date news articles from over 60,000 sources.
- **AI-based analysis**: Leverage artificial intelligence for sentiment analysis, trend prediction, and anomaly detection.
- **Backtesting capabilities**: Explore the influence of past news on market behavior and verify your predictive models.
- **Versatile data sources**: Gain insights from a wide range of international and regional news providers.
  
## API Usage

We are utilizing the `gnews.io` API to search for current and historic news articles. Here is an example Python code snippet for API usage:

```python
import requests

apikey = 'API_KEY'
url = 'https://gnews.io/api/v4/search?q=example&lang=en&country=us&max=10&apikey=' + apikey

response = requests.get(url)
data = response.json()
articles = data['articles']

for article in articles:
    print("Title: ", article['title'])
    print("Description: ", article['description'])
```
This code retrieves the top 10 English news articles from the US related to the query 'example'.

## Database Structure

![DB](https://github.com/AlgoETS/AINewsTracker/assets/13888068/7d054b2b-218a-4be8-a3d0-dd366b3f044b)

## News Sources

AINewsTracker aggregates financial news from multiple trusted sources globally and regionally. Below is a list of these sources:

- International: Yahoo Finance, Reuters, Investing.com, MarketWatch, Financial Times, The Wall Street Journal.
- Canada (Québec): La Presse - Affaires, Le Journal de Montréal - Argent, Radio-Canada - Économie, TVA Nouvelles - Argent, Les Affaires.
- Canada: CBC News - Business, The Globe and Mail - Business, Financial Post, BNN Bloomberg, TSX.

Visit our [News Sources](https://www.ainewstracker.com/news-sources) page for more information on each source, including RSS/API links and the website URL.

## Start the application on local mode

First of all, you have to install all the dependecies :
```
pip install -r requirements.txt
```
Create a `.env` file where you copy the content of the `.env.example` file (make sure to replace the link by your own mongodb link)

Start the server with this command :
```
uvicorn app.main:app --reload
```

Then you can tryout the api by clicking [here](http://127.0.0.1:8000/docs) .





