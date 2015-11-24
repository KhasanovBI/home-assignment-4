import sys
import unittest
from tests.catalog_page_test import AlphabeticalCatalogCheck
from tests.reviews_page_test import AddReviewButtonCheck

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(AlphabeticalCatalogCheck),
        unittest.makeSuite(AddReviewButtonCheck)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
