import pytest
from datetime import date, datetime
from app.models import User, UserDTO

def test_user_model():
    """Test the User model"""
    user = User(
        id="1",
        nom_famille="Doe",
        prenom="John",
        courriel="john@example.com",
        telephone="1234567890",
        anniversaire=date.today(),
        adresse="123 Main St",
        ville="New York",
        province="NY",
        code_postal="10001",
        password="password",
        forfait="Gold",
        credit_id=1,
        points=1000,
        solde=100.00,
        friends=[2, 3],
        last_login=date.today(),
        last_logout=datetime.now(),
    )

    assert user.id == "1"
    assert user.nom_famille == "Doe"
    assert user.prenom == "John"
    assert user.courriel == "john@example.com"
    assert user.telephone == "1234567890"
    assert user.anniversaire == date.today()
    assert user.adresse == "123 Main St"
    assert user.ville == "New York"
    assert user.province == "NY"
    assert user.code_postal == "10001"
    assert user.password == "password"
    assert user.forfait == "Gold"
    assert user.credit_id == 1
    assert user.points == 1000
    assert user.solde == 100.00
    assert user.friends == [2, 3]
    assert user.last_login == date.today()
    assert isinstance(user.last_logout, datetime)


def test_userdto_model():
    """Test the UserDTO model"""
    user_dto = UserDTO(name="John Doe")

    assert user_dto.name == "John Doe"
