# tests/conftest.py
import sys
import os
from fastapi.testclient import TestClient

# Add root project dir to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app

import pytest

@pytest.fixture
def client():
    return TestClient(app)
