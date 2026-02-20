import copy


def demonstrate_copy_behavior():
    original = {
        "user": "Sahil",
        "roles": ["admin", "editor"]
    }

    shallow_copy = copy.copy(original)
    deep_copy = copy.deepcopy(original)

    # Modify nested list
    shallow_copy["roles"].append("viewer")

    print("Original after shallow modification:", original)
    print("Shallow copy:", shallow_copy)
    print("Deep copy:", deep_copy)


if __name__ == "__main__":
    demonstrate_copy_behavior()
