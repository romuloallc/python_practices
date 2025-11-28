# Need to combine *args and **kwargs
def make_sandwich(*ingredients, **options):
    print("Making a sandwich with:")
    for ingredient in ingredients:
        print(f"  {ingredient}")

    print("Options:")
    for key, value in options.items():
        print(f"  {key}: {value}")


def main():
    # Example usage:
    make_sandwich("turkey", "lettuce", "tomato", sauce="mayo", toasted=True)


if __name__ == "__main__":
    main()

