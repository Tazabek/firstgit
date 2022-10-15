def add_fruit(fruit, basket=None):
    if basket is None:
        basket = []
    basket.append(fruit)
    return basket
    
b = add_fruit("banana")
b
# ['banana']
c = add_fruit("apple")
c
# ['apple']