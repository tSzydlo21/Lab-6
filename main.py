def encode(password):
    final = ""
    length = len(str(password))
    num = int
    while length != 0:
        num = (int(str(code)[0:1])) + 3
        if num >= 10:
            num = num - 10
        final = final + str(num)
        code = str(code)[1:]
        length -= 1
    return final

def decode(password):
    return

def main():
    print(encode(123456))
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
            print("The encoded password is " + str(encodedPassword) + ", and the original password is " + decode(password))
            print("")
main()