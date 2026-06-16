from playwright.sync_api import  Playwright, Page, expect
from helpers import *
from helpers import user_actions


def test_e2e_purchase(page:Page):
    user_actions.user_registration(page)
    user_actions.add_multiple_items(page)
    user_actions.remove_item(page)
    user_actions.payment_process(page)
