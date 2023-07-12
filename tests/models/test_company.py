from app.models.company import Company


def test_company_model():
    """Test the Company model"""
    company = Company(
        symbol="TCO",
        name="Test Company",
        sector="Software",
        subSector="Technology",
        headQuarter="USA",
        dateFirstAdded="2023-07-11",
        cik="0000000000",
        founded="2000",
    )

    assert company.symbol == "TCO"
    assert company.name == "Test Company"
    assert company.sector == "Software"
    assert company.subSector == "Technology"
    assert company.headQuarter == "USA"
    assert company.dateFirstAdded == "2023-07-11"
    assert company.cik == "0000000000"
    assert company.founded == "2000"
