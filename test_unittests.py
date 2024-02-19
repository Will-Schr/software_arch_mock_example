import unittest
from unittest import mock
import rlist_count
import listgen


class TestTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(4,4)

class test_rlist_count(unittest.TestCase):
    def test_list_cnt_simple(self):
        rlist_test = rlist_count.list_cnt([1,2,3,4,4,4])
        self.assertEqual(rlist_test.count_lst(4),3)
    def test_list_cnt_simple2(self):
        rlist_test = rlist_count.list_cnt([1,2,3,4,4,4])
        self.assertEqual(rlist_test.count_lst(2),1)

class test_system_under_test(unittest.TestCase):
    @mock.patch('listgen.randint')
    def test_sut_1(self, randint_mock):
        randint_mock.return_value = 5
        test_lstgen = listgen.rand_listpyt(5)
        for i in range(5):
            test_lstgen.gen_rand()
        test_counter = rlist_count.list_cnt(test_lstgen.get_lst())
        self.assertEqual(test_counter.count_lst(5),5)
    @mock.patch('listgen.randint')
    def test_sut_2(self, randint_mock):
        randint_mock.return_value = 8
        test_lstgen = listgen.rand_listpyt(5)
        for i in range(3):
            test_lstgen.gen_rand()
        test_counter = rlist_count.list_cnt(test_lstgen.get_lst())
        self.assertEqual(test_counter.count_lst(8),3)

if __name__ == '__main__':
    unittest.main()