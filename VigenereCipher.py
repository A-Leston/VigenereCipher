# a-b-c-d-e-f-g-h-i-j-k--l--m--n--o--p--q--r--s--t--u--v--w--x--y--z
# 0-1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25
# vigenere cipher by ascii/index math instead of using a large matrix, but the result is the same
# input a filename and a key, result is an encrypted file or decrypted file saved on computer
# but must specify if decrypting or encrypting, and must decrypt in same way it was encrypted
# also it skips any characters that aren't in the alphabet (spaces and special characters)
# and is only using a capital alphabet so everything is turned to capital
# though in theory the cipher could be expanded to work for every ascii number as a much larger matrix


def encrypt(fileName, key):
    # reads the file given and saves its text, also make key loop to be as long as text
    # for each letter in original text and key
    # original index + key index = encrypted index
    # before addition convert each ascii to 0-25 by subtracting 65 from the ascii number
    # but if result is greater than 25, subtract 26 from it, to stay in alphabet range
    # then convert result back to ascii by adding 65
    # result will be the ascii code of the corresponding vigenere cipher letter

    # reads file and saves text
    text = ""
    try:
        file = open(fileName, 'r')
        text = file.read().upper()
        file.close()
    except:
        print("error reading file, restarting")
        main()
    textList = list(text)

    # loops key be to length of text
    loopedKey = ""
    while len(loopedKey) < len(text):
        for element in key:
            loopedKey += element

    loopedKeyList = list(loopedKey)

    # the encryption algorithim
    newText = ""
    for i in range(len(textList)):
        if 65 <= ord(textList[i]) <= 90:
            letterIndex = ord(textList[i]) - 65
            keyIndex = ord(loopedKeyList[i]) - 65
            newIndex = letterIndex + keyIndex
            if newIndex > 25:
                newIndex -= 26
            newLetter = chr(newIndex + 65)
            newText += newLetter
        else:
            newText += str(textList[i])

    # creates new file to write output onto
    try:
        newFile = open("C:\\Users\\Ariel\\Documents\\schoolstuff\\cipherTest\\encrypted_text.txt", 'w')
        newFile.write(newText)
        newFile.close()
    except:
        print("error writing to new file")
        quit()


def decrypt(fileName, key):
    # reads the file given and saves its text, also make key loop to be as long as text
    # for each letter in encrypted text and key
    # encrypt index - key index = original index
    # but if result is negative, add 26 to it, to stay in alphabet range
    # before subtraction convert each ascii to 0-25 by subtracting 65 from the ascii number
    # then convert result back to ascii by adding 65
    # result will be the ascii of the original letter that was encrypted

    # reads file and saves text
    text = ""
    try:
        file = open(fileName, 'r')
        text = file.read().upper()
        file.close()
    except:
        print("error reading file, restarting")
        main()

    textList = list(text)

    # loops key to length of text
    loopedKey = ""
    while len(loopedKey) < len(text):
        for element in key:
            loopedKey += element

    loopedKeyList = list(loopedKey)

    # the inverse of the encryption algorithm
    newText = ""
    for i in range(len(textList)):
        if 65 <= ord(textList[i]) <= 90:
            letterIndex = ord(textList[i]) - 65
            keyIndex = ord(loopedKeyList[i]) - 65
            newIndex = letterIndex - keyIndex
            if newIndex < 0:
                newIndex += 26
            newLetter = chr(newIndex + 65)
            newText += newLetter
        else:
            newText += str(textList[i])

    # create new file to write onto
    try:
        newFile = open("C:\\Users\\Ariel\\Documents\\schoolstuff\\cipherTest\\decrypted_text.txt", 'w')
        newFile.write(newText)
        newFile.close()
    except:
        print("error writing to new file")
        quit()


def main():
    # gets the file path, key, and encrypt/decrypt choice from user
    # then calls encrypt or decrypt with that info
    fileName = input("enter full path of txt file that you want modified: ")
    key = input("enter the key to use for modification: ")
    choice = input("do you want to encrypt or decrypt this file?(enter 'E' for encrypt or 'D' for decrypt): ")

    if choice.upper() == "E":
        encrypt(fileName, key.upper())
        print("encrypted and saved!")

    elif choice.upper() == "D":
        decrypt(fileName, key.upper())
        print("decrypted and saved!")

    else:
        print("error, that is not an option. restarting now.")
        main()


main()
