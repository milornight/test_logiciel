import sqlite3, random, itertools, string
import logging, re

res = False

# Creer la base de donnees
def create_db():
    global res
    if res is True :
        delete_table()
    conn = sqlite3.connect('bibli.db')
    c = conn.cursor()
    sql = """CREATE TABLE {}
          (username TEXT PRIMARY KEY,
          password TEXT NOT NULL,
          spublickey TEXT KEY NOT NULL,
          sprivatekey TEXT NOT NULL,
          epublickey TEXT KEY NOT NULL,
          eprivatekey TEXT NOT NULL
          )
          """.format('Utilisateur')
    c.execute(sql)
    conn.commit()
    conn.close()
    res = True
    return res

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
        conn.close()
    except Exception as e:
        logging.info("affichageData:{}".format(e))

# initialisation db
def deleteData():
    global res
    try:
        conn = sqlite3.connect('bibli.db')
        c = conn.cursor()
        sql = "DELETE from Utilisateur"
        c.execute(sql)
        conn.commit()
        conn.close()
        logging.info("deleteData successful")
        res = False
        return True
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
        # initialiser db
        deleteData()
        # insert les data
        insertData('Amelie00', 'Amelie_000#')
        insertData('Lynne2', 'Lynne-111@')
        # selection username et password
        for raw in c.execute('SELECT username FROM Utilisateur'):
            if len(raw[0]) < 3 :
                logging.error("Username's length is less than 3")
                conn.close()
                return False
            else :
                if re.search(r'[!@#$%^&*()+="]',raw[0]) :
                    logging.error("Username has special caracter")
                    conn.close()
                    return False
                else :
                    for raw2 in c.execute('SELECT password FROM Utilisateur'):
                        print(raw2[0])
                        if len(raw2[0]) < 8 :
                            logging.error("Password is less than 8")
                            conn.close()
                            return False
                        else :
                            #print("yessssss befor verification")
                            if re.search('[!@#$%^&*()+=]',raw2[0]) and re.search('[|_~-]',raw2[0]) and re.search('[A-Z]', raw2[0]) and re.search('[a-z]', raw2[0]) and \
                               re.search('[0-9]', raw2[0]) :
                                #print("yessssss")
                                logging.info("True")
                                conn.close()
                                return True
                            else :
                                logging.error("Password does not respect conditions")
                                #print("Nooooooo")
                                conn.close()
                                return False                            
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
        conn.close()
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
        conn.close()
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
        conn.close()
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
        conn.close()
        return s
    except Exception as e:
        logging.info("send eprivatekey:{}".format(e))

def check_all_data():
    conn = sqlite3.connect('bibli.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    if checkdata() == True :
        for user in c.execute('SELECT username FROM Utilisateur') :
            spubkey = send_spublickey(user[0])
            if len(spubkey[0]) != 128 :
                logging.error("User:{}, it's s-public key is not 128".format(user[0]))
            sprikey = send_sprivatekey(user[0])
            if len(sprikey[0]) != 128 :
                logging.error("User:{}, it's s-private key is not 128".format(user[0]))
            epubkey = send_epublickey(user[0])
            if len(epubkey[0]) != 128 :
                logging.error("User:{}, it's e-public key is not 128".format(user[0]))
            eprikey = send_eprivatekey(user[0])
            if len(eprikey[0]) != 128 :
                logging.error("User:{}, it's e-private key is not 128".format(user[0]))
            
            logging.info("True")

if __name__ == '__main__':
    # delete_table()
    #deleteData()
    #insertData('Amelie00', 'Amelie_000#')
    #insertData('Lynne2', 'Lynne-111@')
    #affichageData()
    res = checkdata()
    print(res)
    #s_public_key = send_spublickey('Lynne2')
    #print(s_public_key)
    #check_all_data()