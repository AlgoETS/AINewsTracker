# -*- coding: utf-8 -*-
import unittest

from app.config import Settings


class TestSettings(unittest.TestCase):
    def setUp(self):
        Settings.reset()

    def test_singleton(self):
        """Test if Settings class is a singleton."""
        settings1 = Settings(".env")
        settings2 = Settings(".env")
        self.assertEqual(settings1, settings2)

    def test_default_values(self):
        """Test if default values are used when environment variable is not set."""
        env = {"ENVIRONMENT": "test"}
        settings = Settings(".env", env=env)

        # These should use default values
        self.assertEqual(settings.HOST, "0.0.0.0")
        self.assertEqual(settings.PORT, 8000)
        self.assertEqual(settings.ENVIRONMENT, "test")

    def test_env_variables(self):
        """Test if environment variables are read correctly."""
        env = {"HOST": "127.0.0.1", "PORT": "9000", "ENVIRONMENT": "test"}
        settings = Settings(".env", env=env)

        self.assertEqual(settings.HOST, "127.0.0.1")
        self.assertEqual(settings.PORT, 9000)
        self.assertEqual(settings.ENVIRONMENT, "test")


if __name__ == "__main__":
    unittest.main()
