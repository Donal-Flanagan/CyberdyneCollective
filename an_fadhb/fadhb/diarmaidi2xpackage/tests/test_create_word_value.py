import os
import unittest

from diarmaidi2xpackage import create_word_value as cwv


class TestTus(unittest.TestCase):
    fileName = "testfile"

    def write_file(self, list_of_words):
        string_to_write = ""

        for i in range(0, len(list_of_words)):
            string_to_write = string_to_write + list_of_words[i] + " "

        file_object = open(self.fileName, 'w')
        file_object.write(string_to_write)
        file_object.close()

    def remove_file(self):
        os.remove(self.fileName)

    def test_get_all_words_in_order(self):
        words_in_order = ['one', 'two', 'three']
        expected = ['one', 'two', 'three']

        self.write_file(words_in_order)
        gotten = cwv.get_lemitized_words_in_order('testFile')
        self.remove_file()

        self.assertEquals(expected, gotten)

    def test_get_key_words_and_values(self):
        words = ['one', 'two', 'three']
        expected = {}
        expected['one'] = 1.0
        expected['two'] = 1.0
        expected['three'] = 1.0
        expected['one two'] = 3.0
        expected['two three'] = 3.0
        expected['one two three'] = 5.0
        gotten = cwv.get_keywords_and_values(words)

        self.assertEquals(expected, gotten)

    def test_create_words_and_values(self):
        words = ['one', 'two', 'three']

        self.write_file(words)
        expected = {}
        expected['one'] = 1.0
        expected['two'] = 1.0
        expected['three'] = 1.0
        expected['one two'] = 3.0
        expected['two three'] = 3.0
        expected['one two three'] = 5.0
        gotten = cwv.create_words_and_values(self.fileName)
        self.remove_file()

        self.assertEquals(expected, gotten)
