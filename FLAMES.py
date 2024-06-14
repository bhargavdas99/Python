from collections import Counter

# Dictionary to map result characters to relationship res
relationship_map = {
    "F": "Friends",
    "L": "Lovers",
    "A": "Affectionate",
    "M": "Marriage",
    "E": "Enemies",
    "S": "Siblings"
}

def get_relationship_result(name1, name2):
    # Counter to count occurrences of each character in names
    counter1 = Counter(name1)
    counter2 = Counter(name2)

    # Calculate the combined length of both names
    combined_length = len(name1) + len(name2)

    # Reduce the combined length by twice the count of common characters
    for char, count in counter1.items():
        if char in counter2:
            combined_length -= (2 * min(count, counter2[char]))

    # print("count",combined_length)
    # Base list representing the possible outcomes
    res = ["F", "L", "A", "M", "E", "S"]

    # Main loop to determine the final outcome
    while len(res) > 1:
        split_index = (combined_length % len(res)) - 1
        # print("split_index",split_index)
        if split_index>=0:
            # take the right part and left part of the split_index
            res = res[split_index+1:] + res[:split_index]
        else:
            res = res[:len(res)-1] #just remove the last element

        

    # Print the final relationship outcome
    print(relationship_map[res[0]])

if __name__ == "__main__":
    # Input for person names
    person1 = input("Enter person 1: ").strip().lower()
    person2 = input("Enter person 2: ").strip().lower()

    # Get and print the relationship result
    get_relationship_result(person1, person2)
