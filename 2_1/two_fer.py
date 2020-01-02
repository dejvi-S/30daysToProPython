def two_fer(name = "you"):
    try:
        print(f"One for {name}, one for me.")
    except:
        raise Exception("Invalid two_fer!")
    pass
