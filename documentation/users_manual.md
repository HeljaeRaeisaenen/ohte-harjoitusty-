# User Manual

Download the project's latest release from here: [link](https://github.com/HeljaeRaeisaenen/ohte-harjoitusty-/releases/tag/loppupalautus).

## Starting the program

Before you can use the program, you must install the dependencies it requires by executing this command: `poetry install`.
After this, the program can be started in the terminal with `poetry tun invoke start`.

## Logging in

The program requires the user to log in. This can be done by writing login credentials in the text fields in the program window:

[picture]

You can also toggle the interface language between Finnish and English by clicking the button in the upper right corner.

If you don't have a username, write your desired username in the field. An user will be automatically created. You can change your password later if you do remember your old password.

If you forget your password, there's nothing you can do but create a new user. You can, however, leave the password field blank.

Please consider that the encryption used on the passwords is probably weak and that I'm not a cryptographer, and that to ensure your safety, _you should not use an username or a password that you use in any other service_.

## Using the placement generator

After you have succesfully logged in, you can 
- start creating the placement,
- view your placement-creating statistics,
- change your password,
- delete your data, 
- look at some info, or
- log out.

If you choose to make a placement, the program opens a new view and asks you for a csv file. By clicking the button, you can select the desired file from your folders with a mouse.

The file must have a very specific structure: 
- It must be comma-separated. You can save Excel and ODT documents in this format by selecting 'csv' as the filetype, and 'comma' as the delimiter while saving the file.
- It must have only two columns, with the first of them having the names you desire to seat (Firstname Lastname), and the second having the seating wishes associated with the name as first names or full names. The best result is achieved when these are separated within the cell by a comma.
- The first row of the file must have headers or other useless information. The first row will be discarded by the program.

If the file doesn't conform to these requirements, the program will likely not work.

The requirements exist mostly because of time limitations and also because this is the type of file that I've worked with when creating seating arrangements by hand.

The program also asks you for the number of tables you have in mind. The people your file will hopefully be full of will be divided into this many groups.

After you have succesfully given the needed information, a placement is made. You unfortunately cannot inluence the arrangement in other ways. You have the possibility of saving the placement as a csv file, which you can open, for example, with Excel or LibreOffice Calc. The contents of the file follow this format: each two rows are one table. Each two row table is separated from the next by an empty row. 

Something to note is that the program treats people who have wished for a certain person as if they had wished for each other, when this person can't be found in the _names_ column. This is motivated by the facts that (a) people who have mutual friends are often friends each other, and (b) sometimes people write a friendgroup nickname or other such things in their wished company. This might elevate the assumed amount of fulfilled seating wishes artificially.
