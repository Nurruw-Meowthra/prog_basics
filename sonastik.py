#1. Get hobbies
def get_hobbies(hobbies_dict: dict, name: str) -> list:
    """
    Return the hobbies of a given person.

    hobbies = {
    "Tom": ["running", "reading"],
    "John": ["movies", "music", "swimming"]
    }

    get_hobbies(hobbies, "Tom")  => ["running", "reading"]
    get_hobbies(hobbies, "Timmy")  => "name not in dictionary"

    :param hobbies_dict: dictionary with peoples' hobbies.
    :param name: name of person whose hobbies are to be returned.

    :return: List of hobbies of the person with given name or "name not in dictionary".
    """
    if name not in hobbies_dict:
        return "name not in dictionary"
    else:
        return hobbies_dict[name]
    
    
#2. Tallest
def find_tallest(height_dict: dict) -> str:
    """
    Return the name of the tallest peron in given dictionary.

    find_tallest({"Tom": 186, "Mari": 175, "Jhon": 190}) => "Jhon"

    :param height_dict: dictionary with peoples' names and heights
    :return name of tallest person in given dict.
    """
    tallest_name = next(iter(height_dict))
    max_height = height_dict[tallest_name]
    for name, height in height_dict.items():
        if height > max_height:
            max_height = height
            tallest_name = name
    return tallest_name


#3. Remove sixes
def remove_sixes(six_dict: dict) -> dict:  
    """
    Return a dictionary where all keys which's values are dividable by six are removed.

    remove_sixes({"a": 4, "b": 8, "c": 6, "d": 18}) => {"a": 4, "b": 8}

    :param six_dict: dictionary to be modified.
    :return: dict without values that are dividable by six.
    """
    keytdel = []
    for nam, val in six_dict.items():
        if val % 6 == 0:
            keytdel.append(nam)
    for key in keytdel:
        del six_dict[key]
    return six_dict


#4. Exchange
def exchange_keys_and_values(exchange_dict: dict) -> dict:
    """
    Return a dict where keys and values have been exchanged.

    exchange_keys_and_values({"a": "b", "c": "d"}) => {"b": "a", "d": "c"}

    :param exchange_dict: dictionary to be modified.
    :return dictionary where values and keys have been exchanged.
    """
    d = {}
    for nam, value in exchange_dict.items():
        d[value] = nam
    return d


#5. Count symbol appearances
def count_symbol_appearances(stringy:  str)  ->  dict:
    """
    Return dict where key is the symbol and the value is the count this symbol is present in the string.
    
    count_symbol_appearances("hello hi") => {'h': 2, 'e': 1, 'l': 2, 'o': 1, ' ': 1, 'i': 1}  
    
    :param stringy: string to be processed.
    :return: dictionary with symbol counts.
    """  
    counts = {}
    for symbol in stringy:
        if symbol in counts:
            counts[symbol] += 1
        else:
            counts[symbol] = 1
    return counts
count_symbol_appearances("hello hi")


#6. Organise by first symbol
def organise_by_first_symbol(strings: list) -> dict:
    """
    Return dict where key the is a symbol and the value is a list of words starting with this symbol.

    organise_by_first_symbol(["hello", "word", "world", "welcome", "yes"]) =>
        {'h': ['hello'], 'w': ['word', 'world', 'welcome'], 'y': ['yes']}

    :param strings: list of strings.
    :return: dict with starting symbol and corresponding words in order of appearance.
    """
    counts = {}
    for custr in strings:
        if not custr:
            continue
        frstsymbl = custr[0]
        if frstsymbl in counts:
            counts[frstsymbl].append(custr)
        else:
            counts[frstsymbl] = [custr]
    return counts


print(organise_by_first_symbol(["hello", "word", "world", "welcome", "yes"]))