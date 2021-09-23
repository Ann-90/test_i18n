def test_check_add_basket_btn(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.implicitly_wait(5)
    browser.get(link)

    add_basket_btn = browser.find_element_by_css_selector(
        "#add_to_basket_form button")

    assert add_basket_btn, 'There is no add_basket button'

    add_basket_btn.click()
