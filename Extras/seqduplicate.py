def distinct_seq(data):
    if len(data) == len(set(data)):
        return True
    else: return False
print(distinct_seq([1,2,3,4,5]))
print(distinct_seq([1,2,3,5,5]))