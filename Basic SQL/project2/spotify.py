import sqlite3


class Spotify():
    def __init__(self) -> None:
        self.connectToDatabase()
    def connectToDatabase(self):
        self.connect = sqlite3.connect("library.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("create table if not exists songlibrary(name TEXT,ownSong TEXT,song_length FLOAT,album TEXT)")
        self.connect.commit()
    def disconnectFromDatabase(self):
        self.connect.close()
    def addSongToDatabase(self,name,ownName,song_length,album_name):
        if(name and ownName and song_length and album_name):
            self.cursor.execute("insert into songlibrary values(?,?,?,?)",(name,ownName,song_length,album_name))
            self.connect.commit()
        else:
            print("Error input")
    def deleteSongFromDatabase(self,name):
        if(name):
            self.cursor.execute("Delete From songlibrary where name = ?",(name,))
            self.connect.commit()
        else:
            print("Error input")
    def getSingleSong(self,name):
        if(name):
            self.cursor.execute("select * from songlibrary where name = ? ",(name,))
            data = self.cursor.fetchall()
            if(len(data) != 0):
                print("Data:",data)
            else:
                print("This is song not found")
    def getAllData(self):
        self.cursor.execute("select * from songlibrary")
        data = self.cursor.fetchall()
        if(len(data) != 0):
            print("All Songs:",data)
        else:
            print("Library don't have any song")
