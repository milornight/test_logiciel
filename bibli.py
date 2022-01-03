import sqlite3, random, itertools, string
import logging


def insertData(user, mdp):
    try:

        # ouverture/initialisation de la base de donnee 
        conn = sqlite3.connect('bibli.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()

        x = string.ascii_letters + string.digits + string.punctuation
        def ranstr(key, num):
            salt = ''.join([random.choice(key) for _ in range(num)])
            return salt

        spublic = ranstr(x, 128)
        sprivate = ranstr(x, 128) 
        epublic = ranstr(x, 128) 
        eprivate = ranstr(x, 128) 
        data = (user, mdp, spublic, sprivate, epublic, eprivate)
        c.execute("INSERT INTO Utilisateur (username, password, spublickey, sprivatekey, epublickey, eprivatekey) \
                    VALUES (?,?,?,?,?,?)", data)
        
        conn.commit()
        print("Records created successfully")
        conn.close()
    except Exception as e:
        sqlite3.logging.info("insertData:{}".format(e))


def affichageData():
    try:
        # ouverture/initialisation de la base de donnee 
        conn = sqlite3.connect('bibli.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        # affichage d'une table
        # lecture dans la base avec un select
        # parcourt ligne a ligne
        for raw in c.execute('SELECT * FROM Utilisateur'):
            print ("\nuser = ", raw[0])
            print ("\npassword = ", raw[1])
            print ("\nspublicKey = ", raw[2])
            print ("\nsprivateKey = ", raw[3])
            print ("\nepublicKey = ", raw[4])
            print ("\neprivateKey = ", raw[5])
    except Exception as e:
        sqlite3.logging.info("affichageData:{}".format(e))

if __name__ == '__main__':
    #sql = SqliteHelper(logging)
    # sql.creat_table("facial_camera_info_64")
    # sql.delete_table("facial_camera_info_64")
    insertData("Lynne2", 'Lynne111@#')
    affichageData()
    #sql.updateData("facial_camera_info_64", '5', 178)
    # sql.deleteData("facial_camera_info_64",122)
    #sql.selectData("facial_camera_info_64")
