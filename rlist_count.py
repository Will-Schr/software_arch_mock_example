class list_cnt():
    def __init__(self, list_in):
        self.lst_chk = list_in
    def count_lst(self, value_in):
        occur = 0
        for item in self.lst_chk:
            if item == value_in:
                occur += 1
        return occur