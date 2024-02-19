from random import randint

class rand_listpyt():
    rand_list = []
    check_val = -1
    occur = -1
    def __init__(self):
        rand_list = []
        occur = -1
    def __init__(self,check_val_in):
        rand_list = []
        check_val = check_val_in
        occur = -1
    def gen_rand(self):
        self.rand_list.append(randint(1,10))
    def get_lst(self):
        return self.rand_list