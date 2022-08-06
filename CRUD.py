#Importing necessary modules and libraries
import mysql.connector
from getpass import getpass
from sqlConnection import mysql_connection
import tkinter
from tkinter import *


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

    my_data = (name, username, pwd, url)

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
          )  #Changing user input from a string to a list for MySQL to process parameter

    #Executing query
    mycursor.execute(query, pwd)

    read_result = mycursor.fetchone()

    #Printing the corresponding password for the user input
    for x in read_result:
        print(x)

    #Closing connection to the database
    conn.close()
    mycursor.close()


#NEEDS TO BE FINISHED: Currently records are not being updated in the database#
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
    new_password = getpass(
                          'Please Enter the New Password: '
                          )

    query = """
            UPDATE Passwords SET Password = %s WHERE Name = %s
            """
    update_data = (
                  new_password,
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
