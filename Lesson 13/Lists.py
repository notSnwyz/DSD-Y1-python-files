topFiveSongs = []
print("Enter your top 5 songs: ")

for i in range(5):
    songs = input()
    topFiveSongs.append(songs)

print("Your top 5 songs are:",*topFiveSongs)

option = int(input("1. Add a new song\n2. Remove a song\n"))

if option == 1:
    songs = input()
    topFiveSongs.append(songs)
    topFiveSongs.sort()
    print(*topFiveSongs)

elif option == 2:
    print("1.",*topFiveSongs[0],"\n2.",*topFiveSongs[1],"\n3.",*topFiveSongs[2],"\n4.",*topFiveSongs[3],"\n5.",*topFiveSongs[4])

    indexRemove = int(input("Which song do you want to remove?: "))

    if indexRemove == 1:
        topFiveSongs.remove(topFiveSongs[0])

    elif indexRemove == 2:
        topFiveSongs.remove(topFiveSongs[1])
    
    elif indexRemove == 3:
        topFiveSongs.remove(topFiveSongs[2])
    
    elif indexRemove == 4:
        topFiveSongs.remove(topFiveSongs[3])

    elif indexRemove == 5:
        topFiveSongs.remove(topFiveSongs[4])

    topFiveSongs.sort()
    print(*topFiveSongs)