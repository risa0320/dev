
import unittest

from db_connection_part.mysql_main import DataFetcher


class TestDataFetcher(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fetcher = DataFetcher()
        rows = [
            dict(text='test_1', number=10, invalid=0),
            dict(text='test_2', number=20, invalid=1),
            dict(text='test_3', number=0, invalid=0),
            dict(text='', number=30, invalid=0),
            dict(number=40, invalid=0),
        ] * 10
        cls.fetcher.test_table.insert_many(rows)

    @classmethod
    def tearDownClass(cls):
        cls.fetcher.test_table.delete()

    def test_count_data_valid(self):
        """ invalid=0"""
        row_count = self.fetcher.count_data(invalid=0)
        self.assertEqual(row_count, 40)
        
    def test_count_data_invalid(self):
        """ invalid=1"""
        row_count = self.fetcher.count_data(invalid=1)
        self.assertEqual(row_count, 10)
        
    def test_count_data_test_1(self):
        """ text=test_1"""
        row_count = self.fetcher.count_data(text='test_1')
        self.assertEqual(row_count, 10)
        
    def test_count_data_test_2(self):
        """ text=test_2"""
        row_count = self.fetcher.count_data(text='test_2')
        self.assertEqual(row_count, 10)
        
    def test_count_data_test_3(self):
        """ text=test_3"""
        row_count = self.fetcher.count_data(text='test_3')
        self.assertEqual(row_count, 10)
        
    def test_count_data_text_is_empty(self):
        """ text=''"""
        row_count = self.fetcher.count_data(text='')
        self.assertEqual(row_count, 10)
        
    def test_count_data_text_is_null(self):
        """ text=NULL"""
        row_count = self.fetcher.count_data(text=None)
        self.assertEqual(row_count, 10)
        
    def test_count_data_number_0(self):
        """ number=0"""
        row_count = self.fetcher.count_data(number=0)
        self.assertEqual(row_count, 10)
        
    def test_count_data_number_10(self):
        """ number=10"""
        row_count = self.fetcher.count_data(number=10)
        self.assertEqual(row_count, 10)
        
    def test_count_data_number_20(self):
        """ number=20"""
        row_count = self.fetcher.count_data(number=20)
        self.assertEqual(row_count, 10)
        
    def test_count_data_number_30(self):
        """ number=30"""
        row_count = self.fetcher.count_data(number=30)
        self.assertEqual(row_count, 10)
        
    def test_count_data_number_40(self):
        """ number=40"""
        row_count = self.fetcher.count_data(number=40)
        self.assertEqual(row_count, 10)
        
