import random

def function(mylist):
    print(random.choices(mylist, weights = [1, 2, 1, 1, 1, 1, 1, 1, 1, 1], k = 15))

function([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
function([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])