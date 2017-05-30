"""Restaurant rating lister."""
import sys


def read_ratings_from_file(file_name):
    """ Create dictionary of restaurants' ratings from file"""

    ratings = {}

    with open(file_name) as f:
        for line in f:
            restaurant, rating = line.strip().split(":")
            ratings[restaurant] = rating

    return ratings


def print_sorted_ratings(ratings):
    """ Print sorted dictionary"""

    for restaurant, rating in sorted(ratings.items()):
        print "%s is rated at %s." % (restaurant, rating)

# dictionary created from data file
ratings = read_ratings_from_file(sys.argv[1])

print_sorted_ratings(ratings)

while True:
    print
    if raw_input("Would you like to add new rating (Y/N): ").lower() == "y":
        new_restaurant = raw_input("Enter a new restaurant name: ")
        new_score = raw_input("Enter %s score: " % (new_restaurant))
        ratings[new_restaurant] = new_score
    else:
        break

print
print_sorted_ratings(ratings)
