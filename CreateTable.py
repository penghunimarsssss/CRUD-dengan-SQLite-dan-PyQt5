import sqlite3 as sql

def main():
    try: 
        db = sql.connect('DataMahasiswa.db')
        cur = db.cursor()
        tablequery = "CREATE TABLE Users (nim INT, nama lengkap TEXT, kelas TEXT, program studi TEXT, jurusan TEXT, telefon TEXT, email TEXT)"

        cur.execute(tablequery)
        print("Table Created Succesfully")

    except sql.Error as e:
        print("There is a table or an error has occurred")

    finally:
        db.close()
        
if __name__ == "__main__":
    main()