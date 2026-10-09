from uuid import uuid4

import pytest
import requests


@pytest.fixture
def api_user():
    username = f"QAStudent_{uuid4().hex}"
    payload = {
        "userName": username,
        "password": "Practice123!",
    }

    response = requests.post(
        "https://demoqa.com/Account/v1/User",
        json=payload,
        timeout=15,
    )
    assert response.status_code == 201
    body = response.json()
    user_id = body["userID"]

    token_response = requests.post(
        "https://demoqa.com/Account/v1/GenerateToken",
        json=payload,
        timeout=15,
    )
    assert token_response.status_code == 200
    token_body = token_response.json()
    assert token_body["status"] == "Success"
    token = token_body["token"]
    assert isinstance(token, str) and token

    headers = {
        "Authorization": f"Bearer {token}",
    }
    user_data = {
        "user_id": user_id,
        "headers": headers,
        "username": username,
    }

    try:
        assert body["username"] == username
        yield user_data
    finally:
        delete_response = requests.delete(
            f"https://demoqa.com/Account/v1/User/{user_id}",
            headers=headers,
            timeout=15,
        )
        assert delete_response.status_code == 204
