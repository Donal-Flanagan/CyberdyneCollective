import os
import unittest

from diarmaidi2xpackage import create_word_value as cwv


class TestTus(unittest.TestCase):
    fileName="testfile"

    def write_file(self,list):
        string_to_write=""

        for i in range(0,len(list)):
            string_to_write=string_to_write+list[i]+" "

        file = open(self.fileName, 'w')

        file.write(string_to_write)

        file.close()

    def remove_file(self):
        os.remove(self.fileName)


    def test_get_all_words_in_order(self):
        list = ['one','two','three']
        expected = ['one','two','three']
        self.write_file(list)


        gotten = cwv.get_lemitized_words_in_order('testFile')

        self.remove_file()

        self.assertEquals(expected, gotten)

    def test_get_key_words_and_values(self):
        input = ['one','two','three']

        expected = {}
        expected['one']=1.0
        expected['two']=1.0
        expected['three']=1.0
        expected['one two'] =3.0
        expected['two three']= 3.0
        expected['one two three']=5.0
        gotten = cwv.get_keywords_and_values(input)

        self.assertEquals(expected, gotten)

    def test_create_words_and_values(self):
        input = ['one','two','three']

        self.write_file(input)
        expected = {}
        expected['one']=1.0
        expected['two']=1.0
        expected['three']=1.0
        expected['one two'] =3.0
        expected['two three']= 3.0
        expected['one two three']=5.0
        gotten = cwv.create_words_and_values(self.fileName)

        self.remove_file()

        self.assertEquals(expected, gotten)




