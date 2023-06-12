# -*- coding: utf-8 -*-
from datetime import date, datetime

from app.models import User, UserDTO


def test_user_model():
    """Test the User model"""
    user = User(
        id="1",
        last_name="Doe",
        first_name="John",
        email="john@example.com",
        phone="1234567890",
        birthday=date.today(),
        address="123 Main St",
        city="New York",
        province="NY",
        postal_code="10001",
        password="password",
        plan="Gold",
        credit_id=1,
        points=1000,
        balance=100.00,
        friends=[2, 3],
        last_login=date.today(),
        last_logout=datetime.now(),
    )

    assert user.id == "1"
    assert user.last_name == "Doe"
    assert user.first_name == "John"
    assert user.email == "john@example.com"
    assert user.phone == "1234567890"
    assert user.birthday == date.today()
    assert user.address == "123 Main St"
    assert user.city == "New York"
    assert user.province == "NY"
    assert user.postal_code == "10001"
    assert user.password == "password"
    assert user.plan == "Gold"
    assert user.credit_id == 1
    assert user.points == 1000
    assert user.balance == 100.00
    assert user.friends == [2, 3]
    assert user.last_login == date.today()
    assert isinstance(user.last_logout, datetime)


def test_userdto_model():
    """Test the UserDTO model"""
    user_dto = UserDTO(email="john@example.com")

    assert user_dto.email == "john@example.com"
