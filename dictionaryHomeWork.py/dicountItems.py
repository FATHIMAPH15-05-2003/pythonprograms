prices={'mango':100,'orange':200,'grape':300}

discount_prices={item:price*0.9 for item,price in prices.items()}
print(discount_prices)