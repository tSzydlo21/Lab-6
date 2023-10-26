def encode(password):
    final = ""
    length = len(str(password))
    num = int
    while length != 0:
        num = (int(str(password)[0:1])) + 3
        if num >= 10:
            num = num - 10
        final = final + str(num)
        password = str(password)[1:]
        length -= 1
    return final

def decode(password):
    final = ''

    for i in password:
        if int(i) - 3 < 0:
            final += str(7+int(i))
        else:
            final += str(int(i)-3)

    return final

def main():
    userChoice = True
    encodedPassword = None
    while userChoice:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        userInput = int(input("Please enter an option: "))
        password = int
        if (userInput == 3):
            userChoice = False
            break
        elif (userInput == 1):
            password = int(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
            encodedPassword = encode(password)
            print("")
        elif (userInput == 2):
            print("The encoded password is " + str(encodedPassword) + ", and the original password is " + str(decode(encodedPassword)))
            print("")
main()