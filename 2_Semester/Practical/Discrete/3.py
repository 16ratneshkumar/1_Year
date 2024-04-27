"""3. Write a Program that generates all the permutations of a given set of digits, with or 
without repetition."""
from itertools import permutations,product

def generate_permutations(digits, repetition=True):
    if repetition:
        return list(permutations(digits))
    else:
        return list(product(digits, repeat=len(digits)))

# Example usage
if __name__ == "__main__":
    digits = [1, 2, 3,4]
    with_repetition = generate_permutations(digits, repetition=True)
    without_repetition = generate_permutations(digits, repetition=False)

    print("Permutations with repetition:")
    for perm in with_repetition:
        print(perm)

    print("\nPermutations without repetition:")
    for perm in without_repetition:
        print(perm)
    print(len(with_repetition),len(without_repetition))
