from unittest import TestCase
import convert


class Test(TestCase):
    def test_mph_to_mile_time(self):
        self.assertEquals(convert.mph_to_mins_per_mile(10.1), 10 / 60)


class Test(TestCase):
    def test_mins_per_mile_to_mph(self):
        self.assertEquals(convert.mins_per_mile_to_mph(601), "0:10:01")
