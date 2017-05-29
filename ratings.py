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

# dictionary created from data file
data = read_ratings_from_file(sys.argv[1])

# ratings. formatted print
for restaurant, rating in sorted(data.items()):
    print "%s is rated at %s." % (restaurant, rating)
