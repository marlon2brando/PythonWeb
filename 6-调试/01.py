def sayHello(name):
    print("i want to say hello with you, {0}".format(name))
    print("Done.......")

if __name__ == "__main__":
    print("***" * 10)
    name = input("Please enter your name:")
    sayHello(name)
    print("@@@" * 10)

