#!/usr/bin/env python3
# coding: utf8

import unittest

def calculate_age_average(people_dict):
    """Function to calculate the average age. people_dict is expected to be a dictionary with sub-dictionaries which contains 'Age'."""
    sumOfAllAges = 0
    if isinstance(people_dict, dict) == False or len(people_dict) == 0: return 0
    # Iterate over all gang members.
    for key, value in people_dict.items():
        sumOfAllAges += int(float(value["Age"]))
    return sumOfAllAges / len(people_dict)

class TestCalculateAverage(unittest.TestCase):
    def test_when_empty_then_zero(self):
        self.assertEqual(calculate_age_average({}), 0.0)

    def test_when_none_then_zero(self):
        self.assertEqual(calculate_age_average(None), 0.0)

    def test_when_all_integer_1_then_one(self):
        self.assertEqual(calculate_age_average({'a':{'Age':1}, 'b':{'Age':1}, 'b':{'Age':1}}), 1.0)

    def test_when_all_float_1_then_one(self):
        self.assertEqual(calculate_age_average({'a':{'Age':1.0}, 'b':{'Age':1.0}, 'b':{'Age':1.0}}), 1.0)

    def test_when_all_string_1_then_one(self):
        self.assertEqual(calculate_age_average({'a':{'Age':'1'}, 'b':{'Age':'1'}, 'b':{'Age':'1'}}), 1.0)

    def test_when_all_string_1pt0_then_one(self):
        self.assertEqual(calculate_age_average({'a':{'Age':'1.0'}, 'b':{'Age':'1.0'}, 'b':{'Age':'1.0'}}), 1.0)
    
    def test_when_average_is_2_then_2(self):
        self.assertEqual(calculate_age_average({'a':{'Age':1}, 'b':{'Age':2}, 'b':{'Age':3}}), 2.0)


if __name__ == '__main__':
    unittest.main()
