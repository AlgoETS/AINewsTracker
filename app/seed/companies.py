# -*- coding: utf-8 -*-
import csv
from typing import List

import httpx

from app.config import Settings
from app.core.repo.company import create_companies
from app.models.company import Company
import os

class CompanySeeder:
    settings = Settings()

    API_KEY = settings.FMP_API_KEY
    SP500_URL = (
        f"https://financialmodelingprep.com/api/v3/sp500_constituent?apikey={API_KEY}"
    )
    @staticmethod
    def generate_csv(companies: List[Company], filename: str):
        with open(filename, "w", newline="") as csvfile:
            fieldnames = [
                "id",
                "name",
                "ticker",
                "description",
                "website",
                "industry",
                "sector",
                "country",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for company in companies:
                writer.writerow(company.dict())

    @classmethod
    async def get_sp500_data(cls):
        async with httpx.AsyncClient() as client:
            response = await client.get(cls.SP500_URL)
        return response.json()

    @staticmethod
    def create_companies(data: List[dict]) -> List[Company]:
        companies = []
        for company_data in data:
            company = Company(**company_data)
            companies.append(company)
        return companies

    @classmethod
    async def get_companies_and_save_to_csv(cls, filename: str):
        data = await cls.get_sp500_data()
        companies = cls.create_companies(data)
        cls.generate_csv(companies, filename)

    @classmethod
    async def seed_companies(cls):
        data = await cls.get_sp500_data()
        companies = cls.create_companies(data)
        await create_companies(companies)
