# -*- coding: utf-8 -*-
from app.models import Company


def test_company_model():
    """Test the Company model"""
    company = Company(
        id="1",
        name="Test Company",
        ticker="TCO",
        description="This is a test company",
        website="https://testcompany.com",
        industry="Technology",
        sector="Software",
        country="USA",
    )

    assert company.id == "1"
    assert company.name == "Test Company"
    assert company.ticker == "TCO"
    assert company.description == "This is a test company"
    assert company.website == "https://testcompany.com"
    assert company.industry == "Technology"
    assert company.sector == "Software"
    assert company.country == "USA"
