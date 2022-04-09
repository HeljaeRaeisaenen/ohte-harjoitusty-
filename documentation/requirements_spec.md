# Requirements specification 

## Purpose

The purpose of this program is to help create a seating placement ('plaseeraus' or 'plassi' in Finnish) for table parties or other such events. Seating wishes of the participants will be taken into account, although wishes can rarely be completely fulfilled. The goal is to create seating arrangements that are less prone to human error than handmande ones, and also satisfactory, meaning that of at least some of the wishes of a participant.

## Users

The application does not have a need for different user groups or for the ability to log in, but these can be realized in order to satisfy the learning objectives of the course.

## Outline for the user interface

![UI](https://user-images.githubusercontent.com/94612974/160600527-6d642e05-783a-45b2-8eb7-40e4f125eefd.png)

The image reads "Placement Generator", "input a csv file", "number of tables", and "start". This should be the view the user sees when starting the application. The user can write text into the fields. How the file is inputted is still undecided. Clicking the start-button will initiate the placement. The user should be able to control the application with a mouse and a keyboard: clicking on buttons and writing text.

## Functionality

In the initial draft, the user picks a csv file which contains the participants' names and their placement wishes and inputs it to the program along with the desired number of tables and participants. This should be possible using a GUI. The program creates the placement and outputs it into another csv file, (or maybe even a printable pdf, but this may not be feasible due to my the skill level).

## Further development

Useful additional functionalities would be, for example giving the user the option to select from a few of TKO-äly's (who'll in the best case scenario benefit from this) most used table party venues, which will cause the program to automatically take into account the table length limitations and anomalities of the given space (not all tables can be of equel length in all venues), though the gain-effort ratio of this isn't good; or the ability of the program to understand minor spelling errors in the names. Also, the possibility to use an "avec" system could be made possible.
