'''
Implement a function to make pairs of even-odd numbers
You have to implement a function called get_pairs that is given a list of numbers, makes pairs
with them. Each pair consists one even number and one odd number. The function will return
a list containing all pairs as tuples. You have to implement the function using arrays.

The function will accept as parameter a (Python) list of integer numbers. The function will
return a (Python) list containing tuples. Each tuple is a pair of even-odd numbers (first
the even, then the odd number). The pairs have to be formed in order: the first available
even number with the first available odd number.

To implement this function create maximum two arrays and traverse numbers list. For each number,
check is it an even number or an odd number, and check if there is a pair available in one
of the arrays created. If there is, save the pair for the output. If not, store the number
until you find a pair.
'''
def get_pairs(numbers):
    pairs = []
    # YOUR CODE GOES HERE
    return pairs


def main():
    numbers = [ x for x in range(0, 20, 2)]
    numbers += [ x for x in range(1, 20, 2)]
    print(get_pairs(numbers))


if __name__ == "__main__":
    main()