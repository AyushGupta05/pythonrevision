def net_price (list_price, discount = 0, tax = 0.05):

    return list_price * (1-discount)* (1 + tax)


print(int(net_price(500)))


# keyword arguments

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello(greeting = "Hello", title="Mr.", first="Spongebob", last =  "Squarepants")

# arbitary arguments 
# *args = allows you to pass multiple non key arguments




# **kwargs = allows you to pass multiple keyword aguments

def print_address(**kwargs):
    print(kwargs)

print_address(street ="123 fake street", city="fake city", state= "haryana" )