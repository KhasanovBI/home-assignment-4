import sys
import unittest

from tests.buy_page_test import BuyPageTest
from tests.catalog_page_test import AlphabeticalCatalogCheck
from tests.reviews_page_test import AddReviewButtonCheck
from tests.review_page_test import ReviewPageTest, StarsCalculationTest

if __name__ == '__main__':
    test_classes_to_run = [
        AlphabeticalCatalogCheck,
        AddReviewButtonCheck,
        ReviewPageTest,
        StarsCalculationTest,
    ]
    # test_classes_to_run = [ReviewPageTest]
    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    result = runner.run(big_suite)
    sys.exit(not result.wasSuccessful())