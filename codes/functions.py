"""
Functions are a block of code that is executed when it is called.
Functions can take parameters and return values.
Functions are defined using the def keyword.
"""

def greet():
    print("Good morning!")

greet()


def check_weather():
    temperature = 8
    if temperature > 25:
        print(f"It's {temperature} degrees and It's hot outside!")
    elif temperature < 10:
        print(f"It's {temperature} degrees and it's cold outside!")
    else:
        print(f"The weather is {temperature} degrees and it is nice today!")

check_weather()



def weather(temperature):
    if temperature > 30:
        print(f"It's {temperature} degrees and It's hot outside!")
    elif temperature < 20:
        print(f"It's {temperature} degrees and it's cold outside!")
    else:
        print(f"The weather is {temperature} degrees and it is nice today!")


weather(19)

weather(temperature = 35)

# Total Price = Price of Item + Tax + Shipping
def total_price(price: float, tax_rate: float, shipping: float, discount: float):
    discounted_price = (price * discount) / 100
    tax = price * tax_rate
    if discount > 0 and discount <= 100:
        total = ( price - discounted_price) + tax + shipping
        print(f"A {discount}% discount amounting to ${discounted_price} has been applied to the item")
        print(f"The total price of the item is ${total} including shipping and tax.")
    else:
        total2 = price + tax + shipping
        print(f"Invalid discount amount ({discount}%). No discount has been applied. Please enter a value between 0 and 100.")
        print(f"The total price of the item is ${total2} including shipping and tax.")


total_price(1500, 0.075, 40, 5)


def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)

result * 3


def calculate_area(width, height):
    area = width * height
    return area

calculated_area = calculate_area(5, 10)

print(f"The Room Size is {calculated_area} square meters.")