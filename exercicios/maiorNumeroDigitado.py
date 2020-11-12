def max_digit(number: int) -> int:
    number = str(number)
    listNumber = []

    if len(number) == 1:
        return int(number)
    else:
        for item in number:
            listNumber.append(int(item))
        return max(listNumber)


if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

# These "asserts" are used for self-checking and not for an auto-testing
print(max_digit(0) == 0)
print(max_digit(52) == 5)
print(max_digit(634) == 6)
print(max_digit(1) == 1)
print(max_digit(10000) == 1)
# print("Coding complete")
