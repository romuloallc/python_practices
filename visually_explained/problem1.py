# I don't know how many number will be passed
# This is a good use case for *args
# *scores -> Collect all positional arguments into scores tuple
def average_score(*scores):
    if len(scores) == 0:
        return 0
    average_score = sum(scores) / len(scores)
    return average_score


def main():
    print(average_score(85, 90, 78))   # Output: 84.333...
    print(average_score(100, 95))      # Output: 97.5
    print(average_score())             # Output: 0 (no scores given)


if __name__ == "__main__":
    main()
