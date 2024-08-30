import sqlite3

conc = sqlite3.connect('youtube_videos.db')

cursor = conc.cursor()

cursor.execute(''' 
      CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL   
               )
''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_videos(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))

    conc.commit()

def update_videos(Video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, Video_id))
    conc.commit()

def delete_videos(Video_id):
    cursor.execute("DELETE FROM videos where id = ?", (Video_id,))
    conc.commit()



def main():
    while True:
        print("*" *50)
        print("\n Youtube manager app with Database")
        print("1. List all Videos:")
        print("2. Add videos:")
        print("3. Update Videos:")
        print("4. Delete Videos:")
        print("5. Exist app")
        print("*" *50)
        choice = input("Enter your choice:")

        match choice:

            case '1':
                list_all_videos()

            case '2':
                name = input("Enter the video name:")
                time = input("Enter the video time:")
              
                add_videos(name, time)

            case '3':
                Video_id = int(input("Enter Video ID to update:"))
                new_name = input("Enter the video name:")
                new_time = input("Enter the video time:")

                update_videos(Video_id, new_name, new_time)

            case '4':
                Video_id = int(input("Enter Video ID to delete:"))
                delete_videos(Video_id)

            case '5':
                break

            case _:
                print("Invalid Choice")

    conc.close()


if __name__ == "__main__":
    main()
 
 
