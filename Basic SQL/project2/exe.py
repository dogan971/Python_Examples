import spotify

print("""You are Welcome To Spotify 

1 -> Add Song

2 -> Get Song

3 -> Get All Song

4 -> Delete Song

Quit for 'q'
""")
spotify1 = spotify.Spotify()
while True:
    value = input("Enter the number: ")
    if(value == 'q'):
        break
    value = int(value)
    if(value == 1):
        name = input("Enter the name: ")
        writerName = input("Enter the writer name: ")
        song_length = int(input("Enter the song length: "))
        albumName = input("Enter the album name: ")
        spotify1.addSongToDatabase(name,writerName,song_length,albumName)
    elif(value == 2):    
        name = input("Enter the name: ")
        spotify1.getSingleSong(name)
    elif(value == 3):
        spotify1.getAllData()
    elif(value == 4):
        name = input("Enter the name: ")
        spotify1.deleteSongFromDatabase(name)