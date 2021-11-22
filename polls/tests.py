import unittest
import models
from django.core.management import *
from cookingFinal import settings
from django.test import TestCase


# Create your tests here.
class TestMyModule(unittest.TestCase):

    def test_sum(self):
        self.assertTrue(89 < 100)


if __name__ == "__main__":
    unittest.main()
