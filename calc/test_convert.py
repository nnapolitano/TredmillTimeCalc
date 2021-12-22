from unittest import TestCase
import convert


class Test(TestCase):
    def test_mph_to_mile_time(self):
        self.assertEquals(convert.mph_to_mile_time(10.1), 10 / 60)


class Test(TestCase):
    def test_mile_time_to_mph(self):
        self.assertEquals(convert.mile_time_to_mph(600), 10)
