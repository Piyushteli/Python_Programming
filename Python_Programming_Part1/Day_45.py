"""
if __name__=="__main__" in python

    It is a certain code only when the script is run directly rather than being imported as a module

1)__name__:
            This is a built-in python variable that holds the name of the current module

2)if __name__=="__main__":
                            This checks if the current module is the main module

"""
def welcome():
    print("Welcome to in India")

def main():
    print("You are clever student")

print(__name__)
if __name__=="__main__":
    welcome()
    main()