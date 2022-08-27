
# Python & MySQL Password Manager

Hello there and welcome to my repository! :wave::wave::wave:

## About and Motivation for this Project

With everyone creating and having a more significant online presence with each passing day, the number of cyber-attacks that target people is increasing. While most of these attacks aren't targeting specific individuals, they are widespread and can reach hundreds to thousands of individuals. There are many ways users can protect themselves from cyber-attacks. One of these ways is to increase the strength of your passwords for your digital accounts. Creating strong and secure passwords that are not reused is easy, but remembering all the different passwords can be pretty tricky. Writing the passwords down on a piece of paper, in a notebook, notes app, or text file takes the security of those passwords and reduces them to zero. 

The solution to the above problem is using a Password Manager. At its core, a password manager allows users to store, create, update, and delete passwords in a database. The passwords stored are end-to-end encrypted, ensuring their safety even if the database is attacked. In addition, password managers can have additional features such as generating a random password, showing reused passwords, indicating whether a password is weak or strong, etc. 

I have been personally using LastPass for over three years now, and for the most part, the experience has been solid. However, since I started using LastPass in early 2019, I had no experience with them before LogMeIn bought them out. While my experience for most of the three years has been good, recently, I have had inconsistencies with their product. In addition, I have minimal experience with their technical support team but can easily describe my experience as frustrating. So, I started browsing other password managers and seeing what they have to offer. Then I decided it would be an excellent experience to learn and develop my password manager.

This project attempts to develop my personal password manager using Python and MySQL. This project will include a GUI allowing users to create, modify, delete, and store passwords inside a database. The user can also search for a password based on a critical value such as the app/website name or URL. Once the password has been identified, the user can copy the password to their clipboard. In addition, the user can generate a random password based on their desired length of characters. Each record stored in the database will include the name of the app/website, username, password, and URL. Each password stored in the database must be encrypted or hashed to ensure security.


## Getting Started

This application can only run in the terminal and must be used from there. First, you will need to navigate into the application's folder. For instance, the following command can be used to navigate into the folder:


```
cd Downloads/passwordManager
```

Once you have navigated into the applications folder, you can see two main files stored here: CRUD.py and passGenerator.py. As the files are named, the CRUD.py file allows the user to create, read, update, and delete passwords in the database, and the passGenerator.py file allows the user to generate a random password.

The passGenerator.py uses the tkinter library to create a GUI, and the CRUD.py currently uses the terminal.

To run these applications, the following commands can be used:


```
python passGenerator.py
```

![image](https://user-images.githubusercontent.com/89234922/183299827-b1c96e8f-fea5-4061-8daf-c5ad0d452421.png)


```
python CRUD.py
```

![image](https://user-images.githubusercontent.com/89234922/183299982-edefce9e-2922-4029-8947-7e89cb4323d8.png)


## Installation

To run the application, you will need to have the following installed:

  •	Python: programming language the application is written in

  •	MySQL Server: RDBMS used to store the data

  •	tkinter: creating GUI interface
  
  • getpass: password input module that does not use echoing
  
  • cryptography: generating a symmetric encryption key for encrypting and decrypting passwords in the database
  
  • base64: encoding and decoding data


Once you have these installed, you must set up the MySQL server. As a reminder, you will need to input your credentials as you had when you set up your MySQL Server.

For example:
```
{
host=’localhost'
user=’testUser’
password=’testPass1234’
database=’testMyDB1’
}
```
## Roadmap

There is still much to be done with this project, and it's far from completion. The following steps of the project I intend to implement are as follows:

:white_check_mark: 1.	Use ~~hash function~~ cryptography to create a symmetric encryption to encrypt and decrypt passwords being stored in the database

   2.	Create a GUI using tkinter for CRUD.py

   3.	Create a main application combining passGenerator.py and CRUD.py with a GUI using tkinter

   4.	Create a master password when accessing the password manager application, and have the master password encrypted


