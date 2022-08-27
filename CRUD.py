#Importing necessary modules and libraries
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import mysql.connector
from sqlConnection import mysql_connection
from getpass import getpass
import tkinter
from tkinter import *

#Generating a symmetric encryption key that will be used to encrypt and decrypt passwords
password_provided = "@dU9tkPcZ,[>"
password = password_provided.encode()   #Convcerting password_propvided type to bytes
salt = b'uY;D1]8GaXFSxiA?'
kdf = PBKDF2HMAC (
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
    )
        
key = base64.urlsafe_b64encode(kdf.derive(password))


####################################
""" Creating Password in Database """
####################################


#Creating a function for storing an entry in the database
def create_information():
    #Connecting to the database
    conn = mysql.connector.connect(host='localhost',
                                   user=input('Please Enter Username: '),
                                   password=getpass('Please Enter Password: '),
                                   database='PasswordManager')
    print(conn)  #Verifying connection to the database

    mydb = conn
    mycursor = mydb.cursor()

    #SQL query used to insert data into the database
    query = """
            INSERT INTO Passwords (Name, Username, Password, URL)
            VALUES (%s, %s, %s, %s)
            """

    #Getting user input for query
    name = input('Please Enter Name for App/Site: ')
    username = input('Please Enter Username for App/Site: ')
    pwd = getpass('Please Enter Password for App/Site: ')
    url = input('Please Enter URL for Site: ')

    ### Encrypt PWD Start ###
    
    
    
    encrypted_pwd = pwd.encode()
    
    f = Fernet(key)
    cipher_pwd = f.encrypt(encrypted_pwd)

    ### Encrypt PWD End ###

    my_data = (
              name,
              username,
              cipher_pwd,
              url
              )

    #Executing query
    mycursor.execute(query, my_data)
    mydb.commit()

    #Verifying the the query has been successfully inserted into the database
    print(mycursor.rowcount, "Record Successfully Inserted Into Database")

    #Closing connection to the database
    conn.close()
    mycursor.close()

    
####################################
""" Reading Password in Database """
####################################


#Creatting a function for returning a specific password
def read_information():
    #Connecing to the database
    conn = mysql.connector.connect(host='localhost',
                                   user=input('Please Enter Username: '),
                                   password=getpass('Please Enter Password: '),
                                   database='PasswordManager')
    print(conn)  #Verifying connection to the database

    mydb = conn
    mycursor = mydb.cursor()
    
    #SQL query to find password
    query = """
            SELECT Password FROM Passwords WHERE Name = %s
            """
    user_app = input(
                    'Please Enter the Name of the App/Site to Retrieve Corresponding Password: '
                    )
    pwd = (
          user_app,
          )  #Changing user input from a string to a tuple for MySQL to process parameter
    
    #Executing query
    mycursor.execute(query, pwd)

    read_result = mycursor.fetchone()
    print(read_result)  #Returning encrypted password
    
    f = Fernet(key)
    
    delimiter = ','
    str_pwd = delimiter.join(read_result)
    
    bytes_pwd = bytes(str_pwd, 'utf-8')
    
    decrypted_pwd = f.decrypt(bytes_pwd)
    final_pwd = str(decrypted_pwd, 'utf-8')     #Converting password in type bytes to string
    print(final_pwd)    #Returning Decrypted Password

    #Closing connection to the database
    conn.close()
    mycursor.close()


#####################################
""" Updating Password in Database """
####################################


#Creating function for updating a specific password
def update_information():
    #Connecting to the database
    conn = mysql.connector.connect(host='localhost',
                                   user=input('Please Enter Username: '),
                                   password=getpass('Please Enter Password: '),
                                   database='PasswordManager')
    print(conn)  #Verifying connection to the database

    mydb = conn
    cursor = mydb.cursor()

    user_app = input(
                    'Please Enter the Name of App/Site Where You Would Like to Update the Password: '
                    )
    new_pwd = getpass(
                          'Please Enter the New Password: '
                          )

    encrypted_pwd = new_pwd.encode()
    f = Fernet(key)
    cipher_pwd = f.encrypt(encrypted_pwd)

    query = """
            UPDATE Passwords SET Password = %s WHERE Name = %s
            """
    update_data = (
                  cipher_pwd,
                  user_app,
                  )

    #Executing query
    cursor.execute(query, update_data)
    mydb.commit()

    #Verifying the query has updated password in database
    print(cursor.rowcount, "Record Successfully Updated in Database")

    #Closing connection to the database
    conn.close()
    cursor.close()


#####################################
""" Deleting Password in Database """
#####################################


def delete_information():
    #Connecing to the database
    conn = mysql.connector.connect(host='localhost',
                                   user=input('Please Enter Username: '),
                                   password=getpass('Please Enter Password: '),
                                   database='PasswordManager')
    print(conn)  #Verifying connection to the database

    mydb = conn
    mycursor = mydb.cursor()

    query = """
            DELETE FROM Passwords WHERE Name = %s
            """
    user_app = input(
                    'Please Enter the Name of the App/Site You Wish to Delete From the Database: '
                    )
    pwd = (
          user_app,
          )  #Changing user input from string to list for MySQL to process the parameter

    #Executing query
    mycursor.execute(query, pwd)
    mydb.commit()

    #Verifying the query has deleted record successfully
    print(mycursor.rowcount, "Record Successfully Deleted in Database")

    #Closing connection to the database
    conn.close()
    mycursor.close()

