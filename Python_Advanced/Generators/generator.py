
user_DB = [
        {"name": "Arun", "age": 22},
        {"name": "Priya", "age": 25},
        {"name": "Rahul", "age": 21},
        {"name": "Divya", "age": 24},
    ]


def get_users():

    for users in user_DB:
        yield users


for users in get_users():
    print(users["name"])



# ---------------------------------------------------------------------------------------------------------------------
"""
Note: 
        get_users()
            ↓
        user 1 → yield → pause
            ↓
        user 2 → yield → pause
            ↓
        user 3 → yield → pause
            ↓
        user 4 → yield → pause

"""