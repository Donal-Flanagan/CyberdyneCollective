import os
import unittest
import pickle
from collections import Counter

from diarmaidi2xpackage import compare_word_with_corpus as cw


class test_compare_word_value(unittest.TestCase):
    file_name = "testfile.pickle"
    compare_file = "testfile.txt"

    def remove_file(self):
        os.remove(self.file_name)
        os.remove(self.compare_file)

    def setUp(self):
        expected = {}
        expected['one'] = 1.0
        expected['two'] = 1.0
        expected['three'] = 1.0
        expected['one two'] = 3.0
        expected['two three'] = 3.0
        expected['one two three'] = 5.0

        pickle.dump(expected, open(self.file_name, 'wb'))

        self.write_compare_file()

    def tearDown(self):
        self.remove_file()

    def write_compare_file(self):
        #
        #Our words for this file are one (4), two(1), one one (6), one two(3), two one(3), one two one (5), two one one(5) and one one one(5). Total
        #is 32, making expected result
        # one: 4/32 , one two =3/32 , two =1/32 , and 0 for all others

        string_to_write = 'one two one one one'

        file_object = open(self.compare_file, 'w')

        file_object.write(string_to_write)

        file_object.close()

    def test_get_n_values(self):

        gotten = cw.get_top_values(self.file_name, 3)

        # top values are 5,3 and 3.

        expected =['one two three','one two','two three']

        self.assertListEqual(expected,gotten)

    def test_compare_single_file(self):

        words_in = ['one two three', 'one two', 'two three']

        expected = {}
        expected['one two three'] = 0.0
        expected['one two'] = 3.0/32.0*100  # returns percentage
        expected['two three'] = 0.0

        gotten = cw.compare_single_file(words_in, self.compare_file)

        expected=Counter(expected)

        self.assertEquals(expected, gotten)

    def test_compare_file_list(self):

        words_in = ['one two three', 'one two', 'two three']

        single_expected = {}
        single_expected['one two three'] = 0.0
        single_expected['one two'] = 3.0/32.0*100  # returns percentage
        single_expected['two three'] = 0.0

        expected = [('one two', 3.0/32.0*100), ('one two three', 0.0), ('two three', 0.0)]

        file_list = [self.compare_file]
        overall_values, file_values = cw.compare_file_list(words_in, file_list)
        single_expected=Counter(single_expected)

        self.assertEquals(expected, overall_values)
        self.assertEquals(expected, file_values.get(self.compare_file))

    def test_compare_file_list_with_two_files(self):

        words_in = ['one two three', 'one two', 'two three']

        second_string = 'Another string with no values'
        file = open("secondTestFile", 'w')
        file.write(second_string)
        file.close()

        files = ["secondTestFile", self.compare_file]

        expected = [('one two', 3.0/32.0*100), ('one two three', 0.0), ('two three', 0.0)]
        # two files, second contributes 0
        overall_expected =[('one two', 3.0/32.0*100/2), ('one two three', 0.0), ('two three', 0.0)]

        overall_values, file_values = cw.compare_file_list(words_in, files)

        self.assertEquals(overall_expected, overall_values)
        self.assertEquals(expected, file_values.get(self.compare_file))




