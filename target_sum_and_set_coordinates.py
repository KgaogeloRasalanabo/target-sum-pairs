# for wholes numbers array, square the array and display sum, lowest, highest and coordinates that give target sum 6

# display sum, min and max
def number_calculator(num):
    print("Sum =", sum(num))
    print("Lowest =", min(num))
    print("Highest =", max(num))


# squares each number in the array
def number_squarer(digits):
    new_numbers = [i ** 2 for i in digits]
    print("Array squared =", new_numbers)


# reduces the given array to max 6
def array_reducer(given_array, limiter):
    new_array = [n for n in given_array if n <= limiter]
    return new_array


# creates a set of coordinates/pairs that give target sum 6
def coordinates_finder(data, upper_limit):
    coord = []
    for i in set(data):
        for j in set(data):
            if i + j == upper_limit:
                coord.append((i, j))
    return coord


if __name__ == "__main__":
    numbers = [4, 9, 8, 4, 3, 5, 2, 5, 2, 3, 5, 3, 0, 1]
    target_sum = 6
    number_calculator(numbers)
    number_squarer(numbers)
    print("Key pairs giving sum", target_sum, "=", coordinates_finder(array_reducer(numbers, target_sum), target_sum))
