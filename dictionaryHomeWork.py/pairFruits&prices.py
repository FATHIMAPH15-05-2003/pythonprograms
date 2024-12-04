fruits={"orange","mango","grape"}

price=[100,200,300]

fruits_price={fruits:price for fruits,price in zip(fruits,price)}
print(fruits_price)