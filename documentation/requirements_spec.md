# Requirements specification 

## Purpose

The purpose of this application is to help create a seating placement ('plaseeraus' or 'plassi' in Finnish) for table parties or other such events. Seating wishes of the participants will be taken into account, although wishes can rarely be completely fulfilled. The goal is to create seating arrangements that are less prone to human error than handmande ones, and also satisfactory, meaning that of at least some of the wishes of a participant are fulfilled.

*Done (save for the fact that not everyone's wishes are fulfilled).*

## Users

The application requires the user to log in. The user can create a username. The username can have a password, or be unprotected. The password won't be stored very securely. There are no different user groups. The user can change their password and delete their user and data.

*Done.*

## Outline for the user interface

![UI](https://user-images.githubusercontent.com/94612974/160600527-6d642e05-783a-45b2-8eb7-40e4f125eefd.png)

The image reads "Placement Generator", "input a csv file", "number of tables", and "start". This is the initial draft for the view the user sees when starting the application. In the application, there are several distinct views for different parts of the program, like logging in, choosing files etc. The user should be able to control the application with a mouse and a keyboard: clicking on buttons and writing text. 

*Done.*

## Functionality

The user picks a csv file which contains the participants' names and their placement wishes and inputs it to the program along with the desired number of tables and participants. This should be possible using a graphical user interface. The program creates the placement and outputs it into another csv file. The user doesn't have extensive control over how the placement is made.

The program's UI is also in English. The program shows what percentage of the participants' total number of seating wishes were made true after a placement is created.

_Done._

## Further development

Useful additional functionalities would be, for example giving the user the option to select from a few of TKO-äly's (who'll in the best case scenario benefit from this) most used table party venues, which will cause the program to automatically take into account the table length limitations and anomalities of the given space (not all tables can be of equel length in all venues); or the ability of the program to understand minor spelling errors in the names. Also, the possibility to use an "avec" system could be made possible. Another good functionality would be to treat people, who have wished for a certain person who isn't in the participants, as if they had wished each other. You can assume that if they know the same person, they probably know each other or at leat have something in common. This could also solve the problem, where peeople wish for "freshers" or other nouns or group names, and probably are a part of that group themselves as well.

But the placements made by this program are of much worse quality than those made by hand, and without many improvements, I don't see there to be incentive to use it in place of handmade placements.
