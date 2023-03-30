# code page definition that lets python know which language code was written in
# -*- coding: cp1252 -*-

# import time module to notebook project
import time

#
import pickle


def check_if_file_exists(file_name="notebook.dat"):
    try:
        # try open file to read to see if it exists
        file = open(file_name, "rb")
        file.close()
        return file_name
    except FileNotFoundError:
        # If the file doesn't exist create it
        file = open(file_name, "wb")
        print("No default notebook was found, created one.")
        file.close()
        return file_name


file_name = check_if_file_exists()

while True:
    # printing options for user
    print("(1) Read the notebook\n(2) Add note\n(3) Edit a note\n"
          "(4) Delete a note\n(5) Save and Quit\n")
    # get input from user
    selected_num = int(input("Please select one: "))
    # read notebook if user selects 1
    if selected_num == 1:
        # open file with bit reading mode "rb"
        readfile = open(file_name, "rb")
        # read contents of file
        try:
            content = pickle.load(readfile)
        except EOFError:
            # if the file is empty, initialize it with an empty list
            content = []
        finally:
            # close the file after reading it
            readfile.close()
        # print the contents
        for note in content:
            print(note)
    # If 2 is selected, add new note to notebook
    elif selected_num == 2:
        # open notebook for reading in bit reading mode "rb"
        readfile = open(file_name, "rb")
        try:
            # load contents of file
            content = pickle.load(readfile)
        except EOFError:
            # if the file is empty, initialize it with an empty list
            content = []
        finally:
            # close the file after reading it
            readfile.close()
        # get new note from user
        message = input("Write a new note: ")
        # add user input into file and add timestamp
        content.append(message + ":::" + time.strftime("%X %x") + "\n")
        # open file for writing in bit-writing mode
        writefile = open(file_name, "wb")
        # write content into file
        pickle.dump(content, writefile)
        writefile.close()
    # if user selected 3 then edit notebook
    elif selected_num == 3:
        # open file in bit reading mode
        load_file = open(file_name, "rb")
        # load file contents
        content = pickle.load(load_file)
        load_file.close()
        # get number of notes
        num_of_notes = len(content)
        print("The list has", num_of_notes, "notes.")
        # get index of desired note to remove
        index = int(input("Which of them will be changed?: "))
        # print content of removed note
        print(content[index])
        # get input for new note
        new_note = input("Give the new note: ")
        # create new content note
        content[index] = new_note + ":::" + time.strftime("%X %x") + "\n"
        # open file in bit writing mode
        edit_file = open(file_name, "wb")
        # copy new content into file
        pickle.dump(content, edit_file)
        edit_file.close()

    elif selected_num == 4:
        read_file = open(file_name, "rb")
        content = pickle.load(read_file)
        read_file.close()
        num_of_notes = len(content)
        print("the list has", num_of_notes, "notes.")
        index = int(input("Which of them will be deleted?: "))
        # check if index input is valid
        try:
            print("Deleted note", content[index])
            # remove content
            content.pop(index)
        except IndexError:
            # consider user does not know index starts at 0 and delete index - 1
            print("Deleted note", content[index - 1])
            content.pop(index - 1)
        edit_file = open(file_name, "wb")
        # copy back new state of file
        pickle.dump(content, edit_file)
        edit_file.close()

    # if user selected 5 quit the program
    elif selected_num == 5:
        print("Notebook shutting down, thank you.")
        break
    # if user fails to input correct number indicate error
    else:
        print("Invalid input please select one of the available options")
