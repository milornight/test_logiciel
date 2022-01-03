import sqlite3, random, itertools, string
import logging, re

# ajouter un utilisateur avec tous les champs
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
        logging.info("insertData:{}".format(e))

# afficher le db de l'utilisateur
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
        logging.info("affichageData:{}".format(e))

# initialisation db
def deleteData():
    try:
        conn = sqlite3.connect('bibli.db')
        c = conn.cursor()
        sql = "DELETE from Utilisateur"
        c.execute(sql)
        conn.commit()
        conn.close()
        logging.info("deleteData successful")
    except Exception as e:
        logging.info("deleteData:{}".format(e))

# supprimer db
def delete_table():
        conn = sqlite3.connect('bibli.db')
        c = conn.cursor()
        c.execute("drop table {}".format('Utilisateur'))
        conn.commit()
        conn.close()
        print('delete done... table name :{}'.format('Utilisateur'))

# verifier si user/password sont valides
def checkdata():
    try:
        conn = sqlite3.connect('bibli.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        # selection username et password
        for raw in c.execute('SELECT username FROM Utilisateur'):
            if len(raw[0]) < 3 :
                logging.error("Username's length is less than 3")
            else :
                if re.search(r'[!@#$%^&*()+="]',raw[0]) :
                    logging.error("Username has special caracter")
                else :
                    for raw2 in c.execute('SELECT password FROM Utilisateur'):
                        if len(raw2[0]) < 8 :
                            logging.error("Password is less than 8")
                        else :
                            if re.search(r'[!@#$%^&*()+="]+',raw2[0]) and re.search(r'[|-_.,;:~]+', raw2[0]) and \
                               re.search(r'[A-Z]+', raw2[0]) and re.search(r'[a-z]+', raw2[0]) and \
                               re.search(r'[0-9]+', raw2[0]) :
                                logging.info("True")
                            else :
                                logging.error("Password does not respect conditions")                            
    except Exception as e:
        logging.info("affichageData:{}".format(e))

# Renvoyer les clefs
def send_spublickey(username):
    try:
        conn = sqlite3.connect('bibli.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        # selection username et password
        s = []
        for raw in c.execute("SELECT spublickey FROM Utilisateur where username='{}'".format(username)):
           s.append(raw[0])
           print(s)
        return s
    except Exception as e:
        logging.info("send spublickey:{}".format(e))

def send_sprivatekey(username):
    try:
        conn = sqlite3.connect('bibli.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        # selection username et password
        s = []
        for raw in c.execute("SELECT sprivatekey FROM Utilisateur where username='{}'".format(username)):
           s.append(raw[0])
           print(s)
        return s
    except Exception as e:
        logging.info("send sprivatekey:{}".format(e))

def send_epublickey(username):
    try:
        conn = sqlite3.connect('bibli.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        # selection username et password
        s = []
        for raw in c.execute("SELECT epublickey FROM Utilisateur where username='{}'".format(username)):
           s.append(raw[0])
           print(s)
        return s
    except Exception as e:
        logging.info("send epublickey:{}".format(e))

def send_eprivatekey(username):
    try:
        conn = sqlite3.connect('bibli.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        # selection username et password
        s = []
        for raw in c.execute("SELECT eprivatekey FROM Utilisateur where username='{}'".format(username)):
           s.append(raw[0])
           print(s)
        return s
    except Exception as e:
        logging.info("send eprivatekey:{}".format(e))

if __name__ == '__main__':
    # delete_table()
    deleteData()
    insertData('Amelie00', 'Amelie_000#')
    insertData('Lynne2', 'Lynne-111@')
    #affichageData()
    checkdata()
    s_public_key = send_spublickey('Lynne2')
    print(s_public_key)
    #updateData("facial_camera_info_64", '5', 178)
    #selectData("facial_camera_info_64")
