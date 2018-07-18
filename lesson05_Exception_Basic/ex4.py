# run me!
class RelationException(Exception):
    def __init__(self, err_msg1, err_msg2):
        self.msg1 = err_msg1
        self.msg2 = err_msg2
    def __str__(self):
        return "Are you sure that " + self.msg1 + " and " + self.msg2 + " are in love with other?" 

try:
    raise RelationException("P1","P2")
except RelationException as e:
    # print("---encountered MyEception---")
    print(e)

