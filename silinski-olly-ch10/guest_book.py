with open("guest_book.txt", "a") as file:
    while True:
        name = input("Please enter your name (or type 'quit' to exit): ")
        
        if name.lower() == 'quit':
            print("Exiting...")
            break 
        
        print(f"Welcome, {name}!")

        file.write(name + "\n")
