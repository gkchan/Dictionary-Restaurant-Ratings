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


def is_valid_score(score):
    """Test whether a score is from 1 to 5"""

    try:
        score = int(score)
    except ValueError:
        return False

    if score not in range(1, 6):
        return False

    return True


ratings = read_ratings_from_file(sys.argv[1])

prompt = """Press 1 to see all the ratings
Press 2 to add new restaurant
Press 3 to get out of here
>> """

while True:
    choice = int(raw_input(prompt))
    if choice == 1:
        print_sorted_ratings(ratings)
        print
    elif choice == 2:
        new_restaurant = raw_input("Enter a new restaurant name: ")
        new_score = raw_input("Rate %s in range from 1 to 5: " % (new_restaurant))
        if is_valid_score(new_score):
            ratings[new_restaurant] = new_score
            print "Thank you! New restaurant %s rated at %s was added." % (new_restaurant, ratings[new_restaurant])
        else:
            print "Sorry, this value is invalid. \nPlease, try again from the very beginning."
            continue
    elif choice == 3:
        break
    else:
        continue
