
def main():
    userInput=input("String:")

    print("No of Spaces", count_spaces(userInput))
    
# Counts the number of spaces

def count_spaces(string):

    spaces=0
    for char in string:
        if char == " " :
            spaces = spaces+1

    return spaces

main()
    
        
