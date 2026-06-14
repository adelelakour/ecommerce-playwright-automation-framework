from playwright.sync_api import  Playwright, Page, expect
import re

def test_buy_item(page:Page):

    page.goto("https://automationexercise.com/")
    page.get_by_role("link", name="Signup / Login").click()
    page.locator("input[data-qa=login-email]").fill("adel.elakour@gmail.com")
    page.locator("input[data-qa=login-password]").fill("123456789")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("link",name="View Product").first.click()
    page.get_by_role("button",name="Add to cart").first.click()
    page.get_by_role("link",name="View Cart").click()
    # page.get_by_role("link", name="Proceed To Checkout").click(no_wait_after=True)
    page.locator(".btn.btn-default.check_out").click()
    expect(page).to_have_url(re.compile(r".*/checkout"))
    page.get_by_role("link",name="Place Order").click()

    #fill payment data
    page.locator("input[name='name_on_card']").fill("Adel")
    page.locator("input[name='card_number']").fill("5555850419296000")
    page.locator("input[name='cvc']").fill("180")
    page.locator("input[name='expiry_month']").fill("02")
    page.get_by_placeholder("YYYY").fill("2028")
    page.get_by_role("button", name="Pay and Confirm").click()
