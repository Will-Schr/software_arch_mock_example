import listgen
import rlist_count


test = listgen.rand_listpyt(5)
for i in range(5):
    test.gen_rand()
test_count = rlist_count.list_cnt(test.rand_list)
print (test_count.lst_chk)
print(test_count.count_lst(5))
print(test_count.count_lst(2))

print(test.rand_list)