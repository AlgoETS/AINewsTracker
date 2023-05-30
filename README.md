# AINewsTracker
AINewsTracker


- Google News https://newsapi.org/s/google-news-api

**`gnews.io`** API to search for current and historic news articles published by over 60,000 sources

```python
apikey = 'API_KEY'
url = 'https://gnews.io/api/v4/search?q=example&lang=en&country=us&max=10&apikey=' + apikey

response = requests.get(url)
data = response.json()
articles = data['articles']

for article in articles:
    print("Title: ", article['title'])
    print("Description: ", article['description'])
```


http://www.plantuml.com/plantuml/dpng/ZLBDRjim3BxhAJYVzeCUTlMfGuTX1RPiYDC7K6oc5MPBWKXb2uQz-qXBQHr3Xruaalg-Zp_KBR6DdARHlE4dd13sOy9ZT9wDwKTB1Cq3OMp04YGnuAy1-70_G0kA0RYvaMDZXTa2iH0VpRzdQXTIx74cqso-XWxmiFssTEyiusE8vwjOI9ubL4cwxRelYCESzI16DUSwHwvq0TAkB-v2_5Daru-v9PljklxEyOZN5Nj6pn9Y_AEmpvOLCCWbdfPSoTVr8PO1gbNFrOckc-HGj6eUnc3rjLHRqRqBqz7wyoxQ_jSit-V0AnTK7yu6VzEFlRoToey9nScgwQYzldqdl5Dmmuge0-WuwgxFkU7YPF81kNzIt1L__fBDnqRAXEPza_VTGfVsr4UtHreZBdqAQEwTJFwO5P6VCPpS81BgBzylUs_ddLhdoLn21QKNbLryjMHAqhh8TzrUy9BZtXjbBMKMzMvnj8m4kx2kw6NEBMm2kuDRLItNopXRNH-PM_H3ciR_

![DB](https://github.com/AlgoETS/AINewsTracker/assets/13888068/7d054b2b-218a-4be8-a3d0-dd366b3f044b)

| Source | Pays | Catégorie | Lien RSS/API | Lien du journal |
| --- | --- | --- | --- | --- |
| Yahoo Finance | International | Finance | https://finance.yahoo.com/rss/ | https://finance.yahoo.com/ |
| Reuters | International | Finance | https://www.reuters.com/tools/rss | https://www.reuters.com/ |
| http://investing.com/ | International | Finance | https://www.investing.com/rss/news.rss | https://www.investing.com/ |
| MarketWatch | International | Finance | https://www.marketwatch.com/rss/ | https://www.marketwatch.com/ |
| Financial Times | International | Finance | https://www.ft.com/ | https://www.ft.com/ |
| The Wall Street Journal | International | Finance | https://www.wsj.com/ | https://www.wsj.com/ |
| La Presse - Affaires | Canada (Québec) | Finance | https://www.lapresse.ca/rss/4084.xml | https://www.lapresse.ca/ |
| Le Journal de Montréal - Argent | Canada (Québec) | Finance | https://www.journaldemontreal.com/rss/argent.xml | https://www.journaldemontreal.com/ |
| Radio-Canada - Économie | Canada (Québec) | Finance | https://ici.radio-canada.ca/rss/4118 | https://ici.radio-canada.ca/ |
| TVA Nouvelles - Argent | Canada (Québec) | Finance | https://www.tvanouvelles.ca/rss/argent.xml | https://www.tvanouvelles.ca/ |
| CBC News - Business | Canada | Finance | https://rss.cbc.ca/lineup/business.xml | https://www.cbc.ca/news/business |
| The Globe and Mail - Business | Canada | Finance | https://www.theglobeandmail.com/ | https://www.theglobeandmail.com/ |
| Financial Post | Canada | Finance | https://financialpost.com/feed/ | https://financialpost.com/ |
| BNN Bloomberg | Canada | Finance | https://www.bnnbloomberg.ca/ | https://www.bnnbloomberg.ca/ |
| TSX | Canada | Finance | https://www.tsx.com/rss | https://www.tsx.com/ |
| Les Affaires | Canada (Québec) | Finance | https://www.lesaffaires.com/rssI | https://www.lesaffaires.com/ |

```
Source,Pays,Catégorie,Lien RSS/API,Lien du journal
Yahoo Finance,International,Finance,https://finance.yahoo.com/rss/,https://finance.yahoo.com/
Reuters,International,Finance,https://www.reuters.com/tools/rss,https://www.reuters.com/
Investing.com,International,Finance,https://www.investing.com/rss/news.rss,https://www.investing.com/
MarketWatch,International,Finance,https://www.marketwatch.com/rss/,https://www.marketwatch.com/
Financial Times,International,Finance,https://www.ft.com/,https://www.ft.com/
The Wall Street Journal,International,Finance,https://www.wsj.com/,https://www.wsj.com/
La Presse - Affaires,Canada (Québec),Finance,https://www.lapresse.ca/rss/4084.xml,https://www.lapresse.ca/
Le Journal de Montréal - Argent,Canada (Québec),Finance,https://www.journaldemontreal.com/rss/argent.xml,https://www.journaldemontreal.com/
Radio-Canada - Économie,Canada (Québec),Finance,https://ici.radio-canada.ca/rss/4118,https://ici.radio-canada.ca/
TVA Nouvelles - Argent,Canada (Québec),Finance,https://www.tvanouvelles.ca/rss/argent.xml,https://www.tvanouvelles.ca/
CBC News - Business,Canada,Finance,https://rss.cbc.ca/lineup/business.xml,https://www.cbc.ca/news/business
The Globe and Mail - Business,Canada,Finance,https://www.theglobeandmail.com/,https://www.theglobeandmail.com/
Financial Post,Canada,Finance,https://financialpost.com/feed/,https://financialpost.com/
BNN Bloomberg,Canada,Finance,https://www.bnnbloomberg.ca/,https://www.bnnbloomberg.ca/
TSX,Canada,Finance,https://www.tsx.com/rss,https://www.tsx.com/
Les Affaires,Canada (Québec),Finance,https://www.lesaffaires.com/rss,https://www.lesaffaires.com/
```
