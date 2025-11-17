cinema = {
    "Wonka":  {"Time": "17:45", "Seats": 45},
    "Dune 2": {"Time": "19:00", "Seats": 30}
}

while True:
    option = int(input("Enter which option you want:\n1. View all movies\n2. Add a new movie\n3. Book ticket\n4. Delete a film\n5. Validate seat count\n6. Exit\n"))

    if option == 1:  
        for name, info in cinema.items():
            print(f"\n{name}\nTime: {info["Time"]}\nSeats: {info["Seats"]}\n")
        
    elif option == 2:
        print("The current movies are:")
        for name in cinema:
            print(name)
        movieName = input("Enter the name of the movie: ")
        movieTime = input("Enter the time of the movie: ")
        movieSeats = int(input("Enter the seats for the movie: "))

        cinema[movieName] = {"Time": movieTime, "Seats": movieSeats}
    
    elif option == 3:
        print("The current movies are:")
        for name in cinema:
            print(name)
        
        movieBook = input("Which movie do you want to book a seat for? ")

        if movieBook in cinema:
            bookSeats = int(input("How many seats do you want to book for the movie? "))

            cinema[movieBook]["Seats"] = cinema[movieBook]["Seats"] - bookSeats
            print("Seats booked!")
        
        else:
            print("Invalid movie")
    
    elif option == 4:
        print("The current movies are:")
        for name in cinema:
            print(name)
        
        movieRemove = input("Which movie do you want to remove? ")

        if movieRemove in cinema:
            cinema.pop(movieRemove)
        else:
            print("Invalid movie")

    elif option == 5:
        for name, info in cinema.items():
            if info["Seats"] < 1:
                print(f"{name} is sold out!")
            
            else:
                print(f"{name} has {info["Seats"]} seats left.")
    
    elif option == 6:
        break