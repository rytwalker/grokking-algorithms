import random

# HASH TABLE
book = dict()
book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49

# Phone book
phone_book = {}
phone_book['jenny'] = 8675309
phone_book['emergency'] = 911

# Voted
voted = {}


def check_voter(name):
    if voted.get(name):
        print("Kick em out!")
    else:
        voted[name] = True
        print("Let them vote")


check_voter('tom')
# Let them vote
check_voter('tom')
# Kick em out!
check_voter('mike')
# Let them vote

# Cache
cache = {}


def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server()
        cache[url] = data
        return data


def get_data_from_server():
    return random.randint(1, 1000)
