import requests


def test_get_books():
    response = requests.get(
        "https://demoqa.com/BookStore/v1/Books",
        timeout=15,
    )
    assert response.status_code == 200
    body = response.json()
    books = body["books"]
    assert len(books) > 0
