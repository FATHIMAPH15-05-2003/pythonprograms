products={"apple":240,"banana":60,"orange":100}

costly_products=max(products.values())
print(costly_products)


# return values
data={v:k for k,v in products.items()}
print(max(data))

#or
def get_value(key):
    return products.get(key)
print(get_value("apple"))    
