#1. Sum Between
def sum_between(start: int, end: int) -> int:
    """
    Return sum of integers between start and end (both included).

    print(sum_between(3, 5)) => 3 + 4 + 5 = 12
    print(sum_between(5, 5)) => 5
    """
    summa = 0
    for i in range(start, end + 1):
        summa = summa + i
    return summa
#sum_between(3, 5)


#2. Sum of even numbers
def sum_of_even_numbers(n: int) -> int:
    """
    Return sum of even numbers from 0 up to n (included).
    
    print(sum_of_even_numbers(5)) => 0 + 2 + 4 = 6
    print(sum_of_even_numbers(0)) => 0
    """
    summa = 0
    for i in range(n + 1):
        if i % 2 == 0:
            summa = summa + i
    return summa
#print(sum_of_even_numbers(5))


#3. Sum of multiples
def sum_of_multiples(n: int, end: int) -> int:
    """
    Return sum of numbers which are multiples of n between 0 and end (included).
    
    print(sum_of_multiples(3, 10)) => 3 + 6 + 9 = 18
    print(sum_of_multiples(7, 10)) => 7
    print(sum_of_multiples(11, 10)) => 0
    """
    summa = 0
    for num in range(1, end + 1):
        if num % n == 0:
            summa += num
    return summa
#sum_of_multiples(3, 10)


#4. Cross sum
def cross_sum(numbers: str) -> int:
    """
    Return cross sum of numbers.
    
    print(cross_sum("1234")) => 1 + 2 + 3 + 4 = 10
    print(cross_sum("0")) => 0
    print(cross_sum("4129458")) => 33
    """
    summa = 0
    for symbol in numbers:
        summa = summa + int(symbol)
    return summa
#cross_sum("1234")


#5. Multiple between
def multiply_between(start: int, end: int) -> int:
    """
    Multiply all numbers between start and end (both included).

    print(multiply_between(1, 3)) => 1 * 2 * 3 = 6
    print(multiply_between(4, 14)) => 14529715200
    print(multiply_between(0, 7)) => 0
    """
    summa = 1
    for num in range(start, end + 1):
        summa = summa * num
    return summa
multiply_between(4, 14)


#6. Make hola string
def make_hola_string(count: int) -> str:
    """
    Make hola string.
    
    print(make_hola_string(3)) => "holaholahola"
    print(make_hola_string(0)) => ""
    """
    times = ""
    #for hola in range(count):
        times += "hola"
    return times
make_hola_string(4)


#7. Compound interest
def compound_interest(amount: int, years: int, rate: int) -> float:
    """
    Calculate compound interest.
    
    print(compound_interest(100, 2, 2)) => 104.04
    print(compound_interest(2000, 6, 8)) => 3173.748645888
    """
    for years in range(1, years+1):
        intress = amount * rate / 100
        amount = amount + intress
    return amount
compound_interest(2000, 6, 8)


#8. Remove vowels
def remove_vowels(original_string: str) -> str:
    """
    Return the given string without vowels.
    
    print(remove_vowels("tere-tere")) => tr-tr
    print(remove_vowels("hklmn")) => hklmn
    print(remove_vowels("aauuiii")) => ""
    """
    string_no_vowels = " "
    vowels = "AEIOUÕÄÖÜaeiouõäöü"
    for symbol in original_string:
        if symbol not in vowels:
            string_no_vowels += symbol
    return string_no_vowels
remove_vowels("hklmn")