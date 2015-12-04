'''
Created on 1 Dec 2015

@author: SainathVasudev_M
'''
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for dish in food:
        if stock[dish] > 0:
            total += prices[dish]
        
    return total


print compute_bill("food")