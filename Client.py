# Author: Zachary A. Bishop
# Created: 7/17/18
# Last updated: 7/17/18
#
# Purpose:
#   Demonstrate a salt + password hash implementation for storing and authenticating passwords
#   Information used: https://crackstation.net/hashing-security.htm
#

from hashlib import sha256
from os import urandom
from random import randrange
from Server import Server


def menu():

    keep_going = True
    while keep_going:
        print("1.) Add New User")
        print("2.) Validate User")
        print("3.) Exit")

    menu_choice = input("Enter your choice: ")

    if menu_choice is "1":
        username = input("Enter new username: ")
        password = input("Enter new password: ")
        salt_size = randrange(15,25)
        salt = urandom(salt_size)
        hash_alg = sha256()
        hash_alg.update(password)
        hashed_password = hash_alg.digest()
        hash_alg.update(salt + hashed_password)
        salted_password = hash_alg.digest()

        s.add_user(username, salt, salted_password)

        print("Added user: " + username)
        print("User Salt: " + str(salt))
        print("User Password: " + str(hashed_password))
        print("User Salted Password: " + str(salted_password))

    if menu_choice is "2":
        username = input("Enter username: ")
        password = input("Enter password: ")

    if menu_choice is "3":
        keep_going = False

if __name__ == '__main__':

    s = Server()
    menu()
