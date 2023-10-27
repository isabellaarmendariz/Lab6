# Sydney Vargo & Isabella Armendariz
# October 25, 2023

def main():
    # make menu
    print("\nMenu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(num):
    # create lists
    numsList = []
    answerList = []

    # add digits in number to list
    for char in num:
        numsList.append(char)

    # make digits integers
    numsList = [int(char) for char in numsList]

    # increase by 3
    for digit in numsList:
        if digit == 7:
            newDigit = 0
        elif digit == 8:
            newDigit = 1
        elif digit == 9:
            newDigit = 2
        else:
            newDigit = digit + 3

        # add them to an answer list
        answerList.append(newDigit)

    # make it a string again
    answer = ""
    for value in answerList:
        answer += str(value)

    # return string
    return answer


def decode(encodepass):
    # create lists
    num_list = []
    num_list2 = []

    # add digits in encoded password to list
    for char in encodepass:
        num_list.append(char)

    # make the characters in the list into integers
    num_list = [int(char) for char in num_list]

    # decrease by 3 and account for exceptions
    for digit in num_list:
        if digit == 2:
            new_digit = 9
        elif digit == 1:
            new_digit = 8
        elif digit == 0:
            new_digit = 7
        else:
            new_digit = digit - 3

        # add changed digits to a new list
        num_list2.append(new_digit)

    # make the password a string again
    decodepass = ""
    for value in num_list2:
        decodepass += str(value)

    # return string
    return decodepass


if __name__ == '__main__':
    while True:
        main()
        choice = int(input("Please enter an option: "))
        if choice == 3:
            break
        elif choice == 1:
            num = input("Please enter your password to encode: ")
            encodepass = encode(num)
            print("Your password has been encoded and stored!")
        elif choice == 2:
                print(f"The encoded password is {encode(num)}, and the original password is {decode(encodepass)}.")
