class reverseString:
    def rev(self, string):
        if isinstance(string,str) and (len(string)>2):
            reversedString=[]
            i=0
            j = len(string) # calculate length of string and save in index

            while j > i:
                reversedString += string[ j - 1 ] # save the value of str[index-1] in reverseString
                j -= 1 # decrement index
            print("The original string is: ")
            print(string + '\n')
            print("The reversed string is: ")
            print(''.join(reversedString)) # reversed string
            print(string + '\n')

            strArr = list(string)
            print("Reversing with built in function: ")
            print(''.join(strArr[::-1]) + '\n') #Reverse with function

            strArr.reverse() #Reverse using built in function
            print("Reversed List: ", ''.join(strArr))

        else:
            print("Please pass valid string!")

s = reverseString()
s.rev("Nawal")