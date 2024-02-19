import unittest
# import sys
# sys.path.append(".")
# import rlist_count
# import listgen

# class test_rlist_count(unittest.TestCase):
#     def list_cnt_simple(self):
#         rlist_test = rlist_count.list_cnt([1,2,3,4,4,4])
#         self.assertEqual(rlist_test.count_lst(4),3)

class basic_test(unittest.TestCase):
    def base(self):
        self.assertEqual(3,3)
    def base2(self):
        self.assertEqual(3,3)


if __name__== '__main__':
    unittest.main()