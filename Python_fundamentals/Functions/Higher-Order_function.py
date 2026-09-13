# user_DB = fake data, similar to data we might receive from a database/API
user_DB = [
    {"name": "Arun", "age": 22},
    {"name": "Priya", "age": 17},
    {"name": "Rahul", "age": 25},
    {"name": "Divya", "age": 19},
]


# Function that checks whether a user is an adult
def is_adult(user):
    return user["age"] >= 18


# Higher-order function
def filter_users(user_DB, condition):
    result = []

    for user in user_DB:
        # condition is a function passed as an argument
        if condition(user):
            result.append(user)

    return result


# Pass is_adult function to filter_users
adults = filter_users(user_DB, is_adult)

print(adults)