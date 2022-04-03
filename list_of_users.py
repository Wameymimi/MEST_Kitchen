my_users = [
    {
        "ID": 1,
        "Name": "Bethel",
        "Phone Number": 256247618,
        "Number of Visits": 29,
        "Post":
            {"ID": 1011, 
            "Title": "New Post 1", 
            "Summary": "Summary about new post!"
            },
    }, 

    {
        "ID": 2,
        "Name": "Funmi",
        "Phone Number": 256247618,
        "Number of Visits": 33,
        "Post":
            {"ID": 1011, 
            "Title": "New Post 1", 
            "Summary": "Summary about new post!"
            },
    }, 

    {
        "ID": 3,
        "Name": "Mush",
        "Phone Number": 256247618,
        "Number of Visits": 54,
        "Post":
            {"ID": 1011, 
            "Title": "New Post 1", 
            "Summary": "Summary about new post!"
            },
    }, 
    
    {
        "ID": 4,
        "Name": "Jaiye",
        "Phone Number": 256247618,
        "Number of Visits": 26,
        "Post":
            {"ID": 1011, 
            "Title": "New Post 1", 
            "Summary": "Summary about new post!"
            },
    }, 
    
    {
        "ID": 5,
        "Name": "Mimi",
        "Phone Number": 256247618,
        "Number of Visits": 87,
        "Post":
            {"ID": 1011, 
            "Title": "New Post 1", 
            "Summary": "Summary about new post!"
            },
    }, 
    
    {
        "ID": 6,
        "Name": "Boakye",
        "Phone Number": 256247618,
        "Number of Visits": 42,
        "Post":
            {"ID": 1011, 
            "Title": "New Post 1", 
            "Summary": "Summary about new post!"
            },
    }, 
    
    {
        "ID": 7,
        "Name": "Kelvin",
        "Phone Number": 256247618,
        "Number of Visits": 67,
        "Post":
            {"ID": 1011, 
            "Title": "New Post 1", 
            "Summary": "Summary about new post!"
            },
    }, 
    
    {
        "ID": 8,
        "Name": "Sogo",
        "Phone Number": 256247618,
        "Number of Visits": 40,
        "Post":
            {"ID": 1011, 
            "Title": "New Post 1", 
            "Summary": "Summary about new post!"
            },
    }, 
    
    {
        "ID": 9,
        "Name": "Clement",
        "Phone Number": 256247618,
        "Number of Visits": 34,
        "Post":
            {"ID": 1011, 
            "Title": "New Post 1", 
            "Summary": "Summary about new post!"
            },
    }
]

index = 0
length = len(my_users)

for user in my_users:
    if length > index:
        print("Number of Visits is", my_users[index].get("Number of Visits"), "for", my_users[index].get("Name"),)
        index += 1