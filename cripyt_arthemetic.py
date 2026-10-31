from itertools import permutations

def solve_cryptarithmetic(word1, word2, word3):
    # Get unique letters across all words
    letters = set(word1 + word2 + word3)
    if len(letters) > 10:
        print("Too many unique letters (max 10 digits available).")
        return None

    letters = list(letters)
    # Leading letters can't be zero
    leading_letters = {word1[0], word2[0], word3[0]}

    for perm in permutations(range(10), len(letters)):
        digit_map = dict(zip(letters, perm))

        if any(digit_map[l] == 0 for l in leading_letters):
            continue

        num1 = word_to_num(word1, digit_map)
        num2 = word_to_num(word2, digit_map)
        num3 = word_to_num(word3, digit_map)

        if num1 + num2 == num3:
            return digit_map, num1, num2, num3

    return None


def word_to_num(word, digit_map):
    num = 0
    for ch in word:
        num = num * 10 + digit_map[ch]
    return num


def print_solution(word1, word2, word3, digit_map, num1, num2, num3):
    print(f"\nSolution found:")
    print(f"  {word1} = {num1}")
    print(f"  {word2} = {num2}")
    print(f"  {word3} = {num3}")
    print(f"  {num1} + {num2} = {num3}\n")
    print("Letter -> Digit mapping:")
    for letter in sorted(digit_map):
        print(f"  {letter} = {digit_map[letter]}")


if __name__ == "__main__":
    word1, word2, word3 = "SEND", "MORE", "MONEY"

    result = solve_cryptarithmetic(word1, word2, word3)

    if result:
        digit_map, num1, num2, num3 = result
        print_solution(word1, word2, word3, digit_map, num1, num2, num3)
    else:
        print("No solution exists.")