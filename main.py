# Sydney Vargo &
# October 25, 2023

def main():
    # make menu
    print("Menu")
    print("_____________")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    # get choice
    choice = int(input("Please choose an option: "))

    # if choice == 1
    if choice == 1:
        num = input("Please enter the number you would like encoded: ")
        answer = encode(num)
        print(answer)


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


if __name__ == '__main__':
    main()
