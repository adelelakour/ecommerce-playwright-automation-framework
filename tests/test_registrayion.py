from playwright.sync_api import  Playwright, Page, expect
import re


def test_register_user(page:Page):
    page.goto("https://automationexercise.com/")

    # Verify homepage is loaded successfully
    expect(page).to_have_title("Automation Exercise")
    expect(page.locator(".title", has_text="Features Items")).to_be_visible()

    # Click Signup/Login and register/logic
    page.get_by_role("link", name="Signup / Login").click()  #I will continue later / website is heavy loaded at the moment