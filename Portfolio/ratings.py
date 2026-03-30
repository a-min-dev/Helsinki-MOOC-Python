"""
The program includes a single function, sort_by_ratings, which takes a list of dictionaries
as its argument.  The function sorts the dictionaries in descending order based on the ratings.
The original list is left unchanged.
"""

def sort_by_ratings(items: list):
    # The use of lambda tells the sorted() function to look at the "rating" value of each dictionary
    # rather than comparing the dictionaries themselves
    return sorted(items, key = lambda item: item["rating"], reverse = True)


# Test the function
shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]

print("Rating according to IMDB")
for show in sort_by_ratings(shows):
    print(f"{show['name']}  {show['rating']}")