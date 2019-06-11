"""
this file is simple encrypt with python script
Developer : Mohammed Abdelawal
"""
result = ''
message = ''
choice = ''

while choice != '-1':
    choice = input("\n Enter 1 to Encrypt, 2 to Decrypt, -1 to Exit Program: ")

    if choice == '1':
        message = input("\n Enter the text to encrypt: ")

        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) - 2)

        print (result + '\n\n')
        result = ''

    elif choice == '2':
        message = input("\n Enter the text to decrypt: ")

        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) + 2)

        print (result + '\n\n')
        result = ''

    elif choice != '-1':
        print ("You have entered an invalid choice. Please try again.\n\n")
