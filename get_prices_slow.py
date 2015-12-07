# -*- coding: utf-8 -*-


from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait



def print_prices():
    driver = Firefox()

    driver.get("https://cars.mail.ru/sale/msk/all/?order=price&dir=asc")

    elements = [None] * 20
    for i in range(0, 20):
        print 'finding by xpath', i
        elements[i] = WebDriverWait(driver, 10).until(lambda d: d.find_element_by_xpath('(//span[@class="offer-card__price__value"])[%d]' % (i + 1,)))

    for i in range(0, 20):
        print 'text', elements[i].text

    driver.quit()

print_prices()
print_prices()
print_prices()
print_prices()
print_prices()
