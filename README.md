# DemoQA API Tests — Lesson 14

REST API tests for the DemoQA Book Store application using Python,
pytest, and requests.

## Test coverage

- Retrieve a nonempty list of books.
- Retrieve a book by ISBN and verify its ISBN and title.
- Verify the status and error details for an unknown ISBN.
- Create a user, generate a token, retrieve the user, delete the user,
  and verify the response after deletion.
- Add a book to a user's collection, verify it, remove it,
  and verify that the collection is empty.

Usernames are generated uniquely for each test.
Protected requests use Bearer Token authorization.

## Setup

Install Python 3.13 or later and uv, then run:

```bash
uv sync
```

## Run tests

```bash
uv run pytest -v
```

Run individual test files:

```bash
uv run pytest tests/test_books.py -v
uv run pytest tests/test_users.py -v
uv run pytest tests/test_user_books.py -v
```

Tests send real requests to https://demoqa.com and require internet access.

## Project structure

- `tests/test_books.py` — public book endpoints.
- `tests/test_users.py` — user lifecycle and authorization.
- `tests/test_user_books.py` — book collection lifecycle.
- `conftest.py` — user fixture with cleanup after the test.

## Cleanup limitation

User cleanup runs after the token has been obtained and the test begins.
A failure during user creation or token setup may require manual cleanup.

## Verified result

The latest full local run completed with 5 tests passed.