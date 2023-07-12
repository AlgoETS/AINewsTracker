# -*- coding: utf-8 -*-
import logging

import pytest

from app.core.logging import Logger


@pytest.fixture(autouse=True)
def reset_logger_level():
    logger_instance = Logger(log_level=logging.INFO)
    yield
    logger_instance.set_level(logging.INFO)

def test_logger_singleton():
    logger1 = Logger(log_level=logging.INFO)
    logger2 = Logger(log_level=logging.INFO)

    assert logger1 is logger2, "Logger is not a singleton"


def test_logger_level():
    logger_instance = Logger(log_level=logging.INFO)  # get the Logger instance
    std_logger = logger_instance.get_std_logger()  # get the standard logger
    assert (
        std_logger.getEffectiveLevel() == logging.INFO
    ), "Logger default level is not INFO"

    logger_instance.set_level(logging.DEBUG)
    assert (
        std_logger.getEffectiveLevel() == logging.DEBUG
    ), "Logger level is not properly set"


@pytest.mark.parametrize(
    "level",
    [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL],
)
def test_logger_level_parameterized(level):
    logger_instance = Logger()
    logger_instance.set_level(level)
    std_logger = logger_instance.get_std_logger()  # get the standard logger
    assert (
        std_logger.getEffectiveLevel() == level
    ), f"Logger level is not properly set for level: {level}"
