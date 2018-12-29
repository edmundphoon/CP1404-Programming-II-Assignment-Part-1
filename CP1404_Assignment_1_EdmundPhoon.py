"""
CP1404/CP5632 Assignment Part 1 Edmund Phoon Jian Cheng 09/12/18
Songs To Learn 1.0
Link to GitHub repository: https://github.com/JCUS-CP1404/a1--edmundphoon
Git branch: feedback
"""
import csv

# display menu
def display_menu():
    menu = """
    Menu:
    L - List songs
    A - Add new song
    C - Complete a song
    Q - Quit
    """
    print(menu)
    return menu


# loading the list of current songs
def load_songs():
    # reading the file
    in_file = open("songs.csv", "r")
    table = in_file.read()
    list_of_songs = [table.split(',') for table in open("songs.csv")]
    # each element (song_row) for every row in the list_of_songs
    song_row = [str(song_row) for song_row in list_of_songs]
    song_count = 0
    song_learn_count = 0
    song_haven_learn_count = 0
    list_of_songs.sort(key = lambda song_row: song_row[1])
    # replacing the 'y' and 'n' into '*' and ' ' for song learnt
    for song_row in list_of_songs:
        song_row[3] = song_row[3].strip('\n')
        if song_row[3] == "y":
            song_row[3] = " "
            song_learn_count += 1
        elif song_row[3] == "n":
            song_row[3] = "*"
            song_haven_learn_count += 1
        # printing the format of each song
        # 0. * Heartbreak Hotel               - Elvis Presley             (1956)
        print(" {:}. {:} {:30} - {:25} ({:})".format(int(song_count), song_row[3], song_row[0], song_row[1], song_row[2]))
        # move to next song row
        song_count += 1
    # printing the number of songs learned and still to learn
    # 2 songs learned, 4 songs still to learn
    print("{:} songs learned, {:} songs still to learn".format(str(song_learn_count), str(song_haven_learn_count)))
    #closing the file for loading songs
    in_file.close()


def complete_song():
    # reading and editing the file
    in_file = open("songs.csv", "r+")
    table = in_file.read()
    list_of_songs = [table.split(',') for table in open("songs.csv")]
    song_row = [str(song_row) for song_row in list_of_songs]
    total_num_of_songs = len(song_row)
    list_of_songs.sort(key=lambda song_row: song_row[1])
    for song_row in list_of_songs:
        song_row[3] = song_row[3].strip('\n')
    song_count = 0

    # number input from song list
    print("Enter the number of a song to mark as learned")
    # Number for song input
    num_learn = str(input(">>> "))

    # input cannot be a string value; using the try and except statement
    try:
        int(num_learn)
    except ValueError:
        print("Invalid input; enter a valid number")
        num_learn = str(input(">>> "))

    # input cannot be left empty
    while len(num_learn) <= 0:
        print("Input cannot be blank")
        num_learn = str(input(">>> "))

    # input is not supposed to be negative
    while int(num_learn) < 0:
        print("Number must be >= 0")
        num_learn = str(input(">>> "))

    # when the target number is out of the song list number range, indicate an invalid number
    while int(num_learn) >= int(total_num_of_songs):
        print ("Invalid song number")
        num_learn = str(input(">>> "))

    # if the number input is greater than 0, proceed to find the matching row in the list of songs
    for song_row in list_of_songs:
        # if the match is found, proceed to change learn status
        if int(num_learn) == int(song_count):
            # if song's learn status is already learned, send message that it is already learned
            if "y" in song_row[3]:
                print("You have already learned {:}".format(song_row[0]))
            # if song's learn status is haven't learned yet, change learn status to learned and write in file
            elif "n" in song_row[3]:
                # convert 'n' to 'y' in song_row
                song_row[3] = "y"
                print("{:} by {:} learned".format(song_row[0], song_row[1]))
                # open the songs.csv file to overwrite file
                out_file = open("songs.csv", "w")
                # print out the new updated list on the csv file
                for song_row in list_of_songs:
                    out_file.write("{},{},{},{}\n".format(song_row[0], song_row[1], song_row[2], song_row[3]))
                # closing the writing file for complete songs
                out_file.close()
        # move to next song row
        song_count += 1

    # closing the file for complete songs
    in_file.close()


def main():
    # introduction
    print("Songs To Learn 1.0 - by Edmund Phoon Jian Cheng")

    # start code by reading the songs.csv file
    in_file = open("songs.csv", "r")
    table = in_file.read()
    # seperate elements with ',' using the split function
    list_of_songs = [table.split(',') for table in open("songs.csv")]
    # each element (song_row) for every row in the list_of_songs
    song_row = [str(song_row) for song_row in list_of_songs]
    print("{:} songs loaded".format(len(song_row)))                                          
    in_file.close()

    # display menu
    display_menu()
    # get choice
    choice = str(input(">>> ")).upper()

    while choice != 'Q':
        # if choice is 'List songs'
        if choice == 'L':
            # display_list()
            load_songs()
            display_menu()
            choice = str(input(">>> ")).upper()

        # if choice is 'Add new song'
        elif choice == 'A':
            # Title for new song input
            new_title = str(input("Title: "))
            while len(new_title) <= 0:
                print("Input cannot be blank")
                new_title = str(input("Title: "))
            # Artist for new song input
            new_artist = str(input("Artist: "))
            while len(new_artist) <= 0:
                print("Input cannot be blank")
                new_artist = str(input("Artist: "))
            # Year for new song input
            new_year = str(input("Year: "))
            # try and except statement for correct input
            try:
                # input cannot be left empty
                while len(new_year) <= 0:
                    print("Input cannot be blank")
                    new_year = str(input("Year: "))
                # input is not supposed to be negative
                while int(new_year) < 0:
                    print("Number must be >= 0")
                    new_year = str(input("Year: "))
            except ValueError:
                print("Invalid input; enter a valid number")
                new_year = str(input("Year: "))
            # if the song's year is stated, proceed with adding the song in the opened songs.csv and print to confirm list addition
            if int(new_year) >= 0:
                in_file = open("songs.csv", "r+")
                table = in_file.read()
                list_of_songs = [table.split(',') for table in open("songs.csv")]
                song_row = [str(song_row) for song_row in list_of_songs]
                # printing the format of the new song in the songs.csv
                # Heartbreak Hotel,Elvis Presley,1956,y
                print("{},{},{},{}".format(new_title,new_artist,new_year,'n'), file=in_file)
                list_of_songs.sort(key=lambda song_row: song_row[1])
                print("{:} by {:} ({:}) added to song list".format(new_title, new_artist, new_year))
                in_file.close()
                # display menu
                display_menu()
                choice = str(input(">>> ")).upper()

        # if choice is 'Complete a song'
        elif choice == 'C':
            # read songs.csv file to find songs learned and not learned
            in_file = open("songs.csv", "r")
            table = in_file.read()
            list_of_songs = [table.split(',') for table in open("songs.csv")]
            song_row = [str(song_row) for song_row in list_of_songs]
            total_num_of_songs = len(song_row)
            completed_songs = 0
            # check if there are any songs yet to learn
            for song_row in list_of_songs:
                if "n" in song_row[3]:
                    complete_song()
                    break
                elif "y" in song_row[3]:
                    completed_songs += 1
                # when there is a song yet to learn, proceed to continue to complete the song function
            if completed_songs == total_num_of_songs:
                print ("No more songs to learn!")
            # display menu
            display_menu()
            choice = str(input(">>> ")).upper()

        else:
            print("Invalid menu choice")
            # display menu
            display_menu()
            choice = str(input(">>> ")).upper()

    # end code
    # read songs.csv file to confirm the number of songs saved in the file
    in_file = open("songs.csv", "r")
    table = in_file.read()
    list_of_songs = [table.split(',') for table in open("songs.csv")]
    song_row = [str(song_row) for song_row in list_of_songs]
    print("{:} songs saved to songs.csv".format(len(song_row)))
    print("Have a nice day :)")
    in_file.close()

if __name__ == '__main__':
    main()
