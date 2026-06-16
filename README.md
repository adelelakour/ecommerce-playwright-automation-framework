# Automation Exercise UI Test Suite

This repository contains end-to-end UI tests for [Automation Exercise](https://automationexercise.com/) using Python, `pytest`, and Playwright.

The suite exercises common storefront flows including authentication, contact form submission, cart behavior, checkout, and one end-to-end purchase journey.

## Tech Stack

- Python
- `pytest`
- `playwright`
- `pytest-playwright`

## Project Structure

```text
.
├── conftest.py
├── helpers/
│   ├── __init__.py
│   └── user_actions.py
├── images/
│   └── shirt.jpg
├── pytest.ini
├── README.md
├── requirements.txt
└── tests/
    ├── test_auth.py
    ├── test_cart.py
    ├── test_checkout.py
    ├── test_contact_form.py
    ├── test_end_to_end_user_journey.py
    └── test_verify_pages.py
```

## What Is Covered

### Authentication

[`tests/test_auth.py`](/home/adelelakour/automation-exercise-playwright-python/tests/test_auth.py)

- Register a new user with a randomized email address
- Attempt signup with an existing email
- Login with valid credentials
- Verify invalid login handling
- Logout

### Cart

[`tests/test_cart.py`](/home/adelelakour/automation-exercise-playwright-python/tests/test_cart.py)

- Add multiple products to the cart
- Update product quantity before adding to cart
- Remove a product from the cart

### Checkout

[`tests/test_checkout.py`](/home/adelelakour/automation-exercise-playwright-python/tests/test_checkout.py)

- Login through a shared fixture
- Add a product to the cart
- Proceed through checkout
- Submit payment details through a shared payment fixture

### Contact Form

[`tests/test_contact_form.py`](/home/adelelakour/automation-exercise-playwright-python/tests/test_contact_form.py)

- Open the Contact Us page
- Fill the form
- Upload `images/shirt.jpg`
- Accept the browser dialog triggered on submission

### End-to-End Purchase Flow

[`tests/test_end_to_end_user_journey.py`](/home/adelelakour/automation-exercise-playwright-python/tests/test_end_to_end_user_journey.py)

- Register a new user
- Add multiple items
- Remove one item
- Complete checkout and payment

### Navigation and Product Pages

[`tests/test_verify_pages.py`](/home/adelelakour/automation-exercise-playwright-python/tests/test_verify_pages.py)

- Verify the Test Cases page
- Verify the Products page and product details view
- Verify product search

## Shared Test Utilities

[`conftest.py`](/home/adelelakour/automation-exercise-playwright-python/conftest.py)

- `login` fixture logs in with a fixed demo account
- `payment` fixture fills the payment form during checkout

[`helpers/user_actions.py`](/home/adelelakour/automation-exercise-playwright-python/helpers/user_actions.py)

- Reusable helper functions for registration, cart manipulation, and payment
- Used by the end-to-end journey test

## Setup

1. Create and activate a virtual environment.
2. Install dependencies.
3. Install Playwright browser binaries.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
```

## Running The Tests

Run the full suite:

```bash
pytest
```

Run a single file:

```bash
pytest tests/test_checkout.py
```

Run tests matching a name:

```bash
pytest -k "login"
```

Run in headed mode:

```bash
pytest --headed
```

## Assumptions And Limitations

- The suite targets the live public site, so failures can come from site changes, latency, or temporary downtime.
- Several tests use hard-coded demo credentials and payment values.
- The registration flow generates a random email address to reduce collisions.
- `pytest.ini` is currently empty.
- Some test modules contain duplicated test function names; in Python, the last definition wins inside that file.

## Dependencies

[`requirements.txt`](/home/adelelakour/automation-exercise-playwright-python/requirements.txt)

```text
playwright
pytest
pytest-playwright
```
