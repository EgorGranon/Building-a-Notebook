# Building-a-Notebook
## INTRODUCTION



In this exercise the idea is to build a notebook which applies the Python data structure list as a note manipulation method when the program is executed, and saves the data in a bitwise mode with pickle. The program has the following features:

A) It is possible to add notes, with similar timestamps as earlier.

B)It is possible to edit a note by selecting it from the list, and rewriting it with new data.

C) It is possible to delete notes separately based on the selection and

D) Notebook loads an existing notebook file from the file "notebook.dat" if such a file exists.



## Usage

When the program starts, the system should check for a notebook datafile "notebook.dat" and load it with pickle. If no such file exists, or there was a problem with the file, a new file is created and the user is notified "No default notebook was found, created one.". After this the basic main menu works as follows:

```commandline
>>> 
No default notebook was found, created one.
(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit

Please select one: 2
Write a new note: Buy birdseed.
(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit

Please select one: 1
Buy birdseed.:::16:41:40 04/25/11
```

If the user is not pleased with a note, it is possible to change one note with the option 3. Then the program asks for the edited note (0 is the first one on the list) with the prompt "The list has [number] notes.\nWhich of them will be changed?:". After giving an input, the user is then printed the selected note and asked for a new note "Give the new note:". This new note replaces the old note on the list:

```commandline
(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit

Please select one: 3
The list has 1 notes.
Which of them will be changed?: 0
Buy birdseed.:::16:41:40 04/25/11
Give the new note: Buy pig food.
(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit

Please select one: 1
Buy pig food.:::16:42:03 04/25/11
```
Deleting a note is done similarly as editing. The only real difference is that the deleted note is printed to the user with the notification "Deleted note [deleted note]".

```commandline
(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit

Please select one: 4
The list has 1 notes.
Which of them will be deleted?: 0
Deleted note Buy pig food.:::16:42:03 04/25/11
```

Finally, when the user decides to quit, the current notebook is saved as a datagram to the file "notebook.dat", with the notification "Notebook shutting down, thank you.".

```commandline
(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit

Please select one: 5
Notebook shutting down, thank you.
```

Also, if there already is a notebook datagram file, it should be loaded at startup, and otherwise normally used in the notebook program:

```commandline
>>> 

(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit

Please select one: 1
Buy gas:::16:45:51 04/25/11
(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit

Please select one: 4
The list has 1 notes.
Which of them will be deleted?: 0
Deleted note Buy gas:::16:45:51 04/25/11
(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit

Please select one: 2
Write a new note: Call tow truck
(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit

Please select one: 5
Notebook shutting down, thank you.
>>> 
```
