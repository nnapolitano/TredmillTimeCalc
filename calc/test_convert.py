from unittest import TestCase
import convert

class Test(TestCase):
    def test_mph_to_mins_per_mile(self):
        self.assertEqual(356, convert.mph_to_mins_per_mile(10.1))

    def test_minutes_to_seconds(self):
        self.assertEqual(330, convert.minutes_to_seconds(5,30))

    def test_seconds_formatter(self):
        self.assertEqual("0:05:56", convert.seconds_formatter(356))
