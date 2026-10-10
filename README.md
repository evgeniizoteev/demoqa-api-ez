# DemoQA API Tests — Lessons 14–15

Educational REST API test project for the DemoQA Book Store application
using Python, pytest, and requests.

## Test coverage

The project contains seven tests:

- Retrieve a nonempty list of books.
- Retrieve a book by ISBN and verify its ISBN and title.
- Verify HTTP status and error details for an unknown ISBN.
- Create a user, generate a token, retrieve and delete the user,
  and verify the response after deletion.
- Retrieve a user created by the shared fixture and verify its ID
  and username.
- Add a book to a user's collection, verify it, remove it,
  and verify that the collection is empty.
- Verify that creating a user with an empty password returns HTTP 400,
  error code "1200", and "UserName and Password required."

Each test that creates a user generates a unique username.
Protected requests use Bearer Token authorization.

## Setup

Install Python 3.13 or later and uv, then run:

```bash
uv sync --locked
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
Results depend on the availability and behavior of this external service.

## Code quality

```bash
uvx black --check conftest.py tests
uvx flake8 conftest.py tests
```

## Continuous integration

The workflow `.github/workflows/api-checks.yml` runs on:

- Pull request creation and updates.
- Manual execution through GitHub Actions.
- A daily schedule at 08:17 UTC.

The workflow checks out the repository, installs uv and Python,
installs dependencies from the lockfile, runs Flake8, and runs pytest
on an Ubuntu runner.

Pytest generates `reports/pytest-results.xml`.
The workflow uploads it as the `pytest-results` artifact, including
when tests fail. If an earlier step prevents pytest from running,
the report may not exist.

Uploading an artifact does not turn a failed test run into a successful job.
Generated reports are excluded from Git.

## Project structure

- `tests/test_books.py` — public book endpoints.
- `tests/test_users.py` — user lifecycle, retrieval, and empty-password checks.
- `tests/test_user_books.py` — book collection lifecycle.
- `conftest.py` — shared user fixture with cleanup.
- `.github/workflows/api-checks.yml` — CI checks and report upload.

## Test data and cleanup

The `api_user` fixture creates a user, obtains a token, and passes the
user ID, username, and authorization headers to the test.

Cleanup is performed in `finally` after `yield`, including when test
assertions fail. A failure before entering the cleanup-protected block,
such as during token setup, may leave a user requiring manual cleanup.
Deletion also depends on the API being available.

## AI-assisted practice

Cursor proposed the empty-password test from a prompt specifying
the request and expected response observed in Postman.

The proposed code was reviewed before being added to the project.
Syntax and style checks, the individual test, and the full suite
were run locally. The pull request also passed CI.

A passing test alone does not establish that its assertions correctly
cover a requirement. Expected results must be checked against the
requirements or API documentation.

## Verified results

- Latest full local run: 7 passed in 27.50 seconds.
- PR #8: GitHub Actions API checks completed successfully.

These results describe recorded runs, not a guarantee of future results.
