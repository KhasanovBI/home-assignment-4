from element import *
from locators import BuyPageLocators
from page_objects.base_page_object import Page


class BuyPage(Page):
    OfferCardsXpath = '//span[@class="offer-card"]'
    JS_CARDS_SCRIPT = """
    prices = document.querySelectorAll('.offer-card .offer-card__price__value');
    titles = document.querySelectorAll('.offer-card .offer-card__title');
    regions = document.querySelectorAll('.offer-card .offer-card__contacts .offer-card__contacts__item_dotted');
    t = [];
    for (var i = 0; i < titles.length; ++i) {
        t[i] = {"price": prices[i].textContent, "title": titles[i].textContent,
            "region": regions[i].textContent};
    }
    return t;"""

    def __init__(self, driver):
        super(BuyPage, self).__init__(driver)
        self.price_sort_btn = ClickableElement(BuyPageLocators.PRICE_SORT_BTN, self)
        self.region_btn = ClickableElement(BuyPageLocators.REGION_SELECT_BTN, self)
        self.region_input = InputElement(BuyPageLocators.REGION_INPUT, self)
        self.city_first_result = ClickableElement(BuyPageLocators.CITY_ITEM, self)
        self.apply_filter_lnk = ClickableElement(BuyPageLocators.APPLY_FILTER, self)
        self.submit_region_btn = ClickableElement(BuyPageLocators.SUBMIT_REGION, self)
        self.init_cards()


    def init_cards(self):
        n_cards = len(BuyPageLocators.OFFER_CARDS.locate(self.driver))
        self.cards = [OfferCard(BuyPageLocators.OfferCardLocator(i), self) for i in range(0, n_cards)]
        # js_result = self.driver.execute_script(self.JS_CARDS_SCRIPT)
        # cards = [OfferCard(int(x['price']), x['title'], x['region']) for x in js_result]
        # return cards



class OfferCard():
    def __init__(self, locator, page):
        self.price = BaseElement(BuyPageLocators.OfferCardPriceLocator(locator), page)
        # self.title = title
        # self.region = region
