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


def test_get_book_by_isbn():
    response = requests.get(
        "https://demoqa.com/BookStore/v1/Book",
        params={"ISBN": "9781449325862"},
        timeout=15,
    )
    assert response.status_code == 200
    body = response.json()
    assert body["isbn"] == "9781449325862"
    assert body["title"] == "Git Pocket Guide"


def test_get_book_with_unknown_isbn():
    response = requests.get(
        "https://demoqa.com/BookStore/v1/Book",
        params={"ISBN": "0000000000000"},
        timeout=15,
    )
    assert response.status_code == 400
    body = response.json()
    assert body["code"] == "1205"
    expected_message = "ISBN supplied is not available in Books Collection!"
    assert body["message"] == expected_message
