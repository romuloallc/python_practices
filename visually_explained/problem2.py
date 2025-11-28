# Since details are passed in using labels or keywords -> use **kwargs
# **kwargs -> Collect all keywords arguments into details dictionary
def describe_pet(name, type, **details):
    print(f"Pet name: {name}")
    print(f"Animal type: {type}")

    if details:
        print("Details:")
        for key, value in details.items():
            print(f"  {key}: {value}") 


def main():
    # Example usage:
    describe_pet("Whiskers", "cat", color="gray", age=3, favorite_food="tuna")


if __name__ == "__main__":
    main()

