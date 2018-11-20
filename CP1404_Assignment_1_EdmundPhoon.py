"""
CP1404/CP5632 - Assignment Part 1# -*- coding: utf-8 -*-

@author: edmundpjc
"""

# welcome message
name = str(input("Name: "))
print ("Welcome ", format(name))
print ("Songs to Learn 1.0")

#display menu
menu = """
Menu:
L - List songs
A - Add new song
C - Complete a song
Q - Quit
"""
print (menu)

#get choice
choice = str(input(">>> ")).upper()

while choice != 'Q':

    #if choice is 'List songs'
    if choice == 'L':
        print ("Test")
        print ("? songs learned, ? songs still to learn")
        print (menu)
        choice = str(input(">>> ")).upper()

    # if choice is 'Add new song'
    elif choice == 'A':
        #Title for new song input
        new_title = str(input("Title: "))
        while len(new_title) <= 0:
            print ("Input cannot be blank")
            new_title = str(input("Title: "))
        #Artist for new song input
        new_artist = str(input("Artist: "))
        while len(new_artist) <= 0:
            print ("Input cannot be blank")
            new_artist = str(input("Artist: "))
        #Year for new song input
        new_year = str(input("Year: "))
        while int(new_year) < 0:
            print ("Number must be >= 0")
            new_year = str(input("Year: "))
        if int(new_year) >= 0:
            print ("{:} by {:} ({:}) added to song list".format(new_title, new_artist, new_year))
            print (menu)
            choice = str(input(">>> ")).upper()
        else:
            print("Invalid input; enter a valid number")
            new_year = str(input("Year: "))

    # if choice is 'Complete a song'
    elif choice == 'C':
        print ("Enter the number of a song to mark as learned")
        num_learn = int(input(">>> "))
        print ("? learned")
        print (menu)
        choice = str(input(">>> ")).upper()

    else:
        print ("Invalid menu choice")
        print (menu)
        choice = str(input(">>> ")).upper()

print("? songs saved to songs.csv")
print("Have a nice day :)")