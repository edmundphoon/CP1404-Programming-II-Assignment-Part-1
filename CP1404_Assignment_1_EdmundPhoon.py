"""
CP1404/CP5632 - Assignment Part 1# -*- coding: utf-8 -*-
Songs To Learn 1.0
@author: edmundpjc
"""
import csv

#display menu
def display_menu():
    menu = """
    Menu:
    L - List songs
    A - Add new song
    C - Complete a song
    Q - Quit
    """
    print (menu)
    return menu

def load_songs():
    in_file = open("songs.csv", "r")
    list_of_songs = in_file.read()
    song_row = 0
    song_learn_count = 0
    song_haven_learn_count = 0
    for song_row in list_of_songs:
        # 0. * Heartbreak Hotel               - Elvis Presley             (1956)
        print (" {:}. {:} {:30} - {:25} ({:})".str(format(song_row), list_of_songs[song_row][3], list_of_songs[song_row][0], list_of_songs[song_row][1], list_of_songs[song_row][2])

    if list_of_songs[song_row][3] == "y":
        each_song_learn = "*"
        song_learn_count += 1
    elif list_of_songs[song_row][3] == "n":
        each_song_learn = " "
        song_haven_learn_count += 1
    else:
        print ("Error")

    load_song_result = "{:} songs learned, {:} songs still to learn".str(format(song_learn_count, song_haven_learn_count))
    return load_song_result
    in_file.close()


def complete_song():
    in_file = open("songs.csv", "r+")
    list_of_songs = in_file.read()
    print("Enter the number of a song to mark as learned")
    num_learn = int(input(">>> "))
    num_learn_result = " "
    song_row = 0
    for song_row in list_of_songs:
        for song_num in list:
            if song_num == num_learn:
                num_learn_result = "{:} by {:} learned".format(list_of_songs[song_row][1], list_of_songs[song_row][2])
            elif song_num != num_learn:
                num_learn_result = "You have already learned {:}".format(list_of_songs[song_row][1])
            else:
                num_learn_result = "Invalid number"
    return str(num_learn_result)
    in_file.close()


def main():
    name = str(input("Name: "))
    print("----------------------------\n")
    print("Songs To Learn 1.0 - by", format(name))
    display_menu()
    # get choice
    choice = str(input(">>> ")).upper()

    while choice != 'Q':
        #if choice is 'List songs'
        if choice == 'L':
            #display_list()
            load_songs()
            display_menu()
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
                new_dict = {str(add_name): int(add_age)}
                print ("{:} by {:} ({:}) added to song list".format(new_title, new_artist, new_year))
                display_menu()
                choice = str(input(">>> ")).upper()
            else:
                print("Invalid input; enter a valid number")
                new_year = str(input("Year: "))

        # if choice is 'Complete a song'
        elif choice == 'C':
            complete_song()
            display_menu()
            choice = str(input(">>> ")).upper()

        else:
            print ("Invalid menu choice")
            display_menu()
            choice = str(input(">>> ")).upper()

    list_of_songs = [[0, 'Heartbreak Hotel', 'Elvis Presley', 1956, 'y'],
                     [1, 'Somebody That I Used to Know', 'Gotye featuring Kimbra', 2012, 'n'],
                     [2, 'Macarena', 'Los Del Rio', 1996, 'n'],
                     [3, 'I Want to Hold Your Hand', 'The Beatles', 1964, 'y'],
                     [4, 'Let It Be', 'The Beatles', 1970, 'y'],
                     [5, 'Boom Boom Pow', 'The Black Eye Peas', 1956, 'y'],
                     [6, 'My Sharona', 'The Knack', 1979, 'n']]

    print("{:} songs saved to songs.csv".format(len(list_of_songs)))
    print("Have a nice day :)")

if __name__ == '__main__':
    main()