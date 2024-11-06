# WAP that accepts a character and perform the following
# a. print whether the character is a letter or numeric or a special character 
def check(char1):
    if char1.isalpha()==True:
        print("char is letter")
    elif char1.isdigit()==True:
        print("char is numeric")
    else:
        print("char is special character")
char1=input("enter the character")

check(char1)


# b. if the character is a letter print whether is uppercase or lowercase

def case(char1):
    if char1.isupper()==True:
        print("yes it is in upper case")
    elif char1.islower()==True:
        print("yes it is ;lower case ")
    else:
        print("char is in title")
case(char1)

# if the character is a numeric digit print its name in text

def name(char2):
    dict_1={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
    char3=str(char2)
    if char3.isdigit()==True:
        for i in dict_1.keys():
            if i==char2:
             print("name of digit is :", dict_1[char2])
char2=int(input("enter digit"))
name(char2)