from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setattr("src.app.activities", deepcopy(activities))
    with TestClient(app) as test_client:
        yield test_client