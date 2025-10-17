"""Function examples."""


# func()
def func():
    """Prints I´m inside the function"""
    print("I´m inside the function")


# my_name_is(name)
def my_name_is(name) -> str:
    print("My name is " + name)
    

# sum_six(num)
def sum_six(num):
    return 6 + num


# sum_numbers()
def sum_numbers(a, b):
    return a + b


# usd_to_eur()
def usd_to_eur(usd_amount):
    exchange_rate = 0.8
    return usd_amount * exchange_rate