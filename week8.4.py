
page=int(input("Page No: "))

def main():

    if isEven(page):
        print(page)
    else:
        print("%60s%d"%("",page))
def isEven(page):
    return page % 2 ==0

main()
