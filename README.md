<p align="center">
    <img width="50%" src="./AINewsTracker_transparent.svg" alt="AINewsTracker"/>
    <h1 align="center">AINewsTracker </h1>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" alt="License MIT"/>
    <img src="https://img.shields.io/badge/-FastAPI-009681?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
    <img src="https://img.shields.io/badge/-MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB"/>
    <img src="https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
    <img src="https://img.shields.io/badge/-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
</p>

## What is AINewsTracker?

AINewsTracker is a powerful web application dedicated to backtesting the influence of financial news on the stock market. Leveraging AI to sort, filter, and analyze financial news from various reliable international and regional sources, it enables users to observe and predict potential impacts on market trends.

## How to use

1. Setup and activate the Python environment of your choice.
2. Run the following command to install the required dependencies:

```shell
pip install -r requirements.txt
```

3. Run the following command to launch FastAPI in development mode:

```shell
uvicorn app.main:app --reload
```

## Features

- **Real-time tracking of financial news**: Get up-to-date news articles from over 60,000 sources.
- **AI-based analysis**: Leverage artificial intelligence for sentiment analysis, trend prediction, and anomaly detection.
- **Backtesting capabilities**: Explore the influence of past news on market behavior and verify your predictive models.
- **Versatile data sources**: Gain insights from a wide range of international and regional news providers.

## News Sources

AINewsTracker aggregates financial news from multiple trusted sources globally and regionally. Below is a list of these sources:

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


## File Structure

```
├── AINewsTracker.svg
├── AINewsTracker_transparent.svg
├── Dockerfile
├── LICENSE
├── README.md
├── Test-AI.ipynb
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── database
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── db.py
│   ├── favicon.ico
│   ├── main.py
│   ├── models
│   │   ├── RSSFeed.py
│   │   ├── __init__.py
│   │   ├── article.py
│   │   ├── company.py
│   │   ├── score.py
│   │   └── users.py
│   ├── routers
│   │   ├── RSSFeed.py
│   │   ├── __init__.py
│   │   ├── article.py
│   │   ├── company.py
│   │   └── users.py
│   └── services
│       ├── __init__.py
│       ├── article.py
│       ├── company.py
│       ├── crypto.py
│       ├── rss.py
│       ├── sentiments.py
│       └── summary.py
├── deploy
│   ├── README.md
│   └── docker-compose.yml
├── docker-compose.yml
├── monitoring
├── pyproject.toml
├── requirements-dev.txt
├── requirements.txt
├── tests
│   ├── __init__.py
│   └── test_app.py
└── wiki
    ├── CODE_OF_CONDUCT.md
    ├── ISSUES.md
    └── WORKFLOW.md
```