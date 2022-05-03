# User Manual

Download the project's latest release from here: [link].

## Starting the program

Before you can use the program, you must install the dependencies it requires by executing this command: `poetry install`.
After this, the program can be started in the terminal with `poetry tun invoke start`.

## Logging in

The program requires the user to log in. This can be done by writing login credentials in the text fields in the program window:

[picture]

You can also toggle the interface language between Finnish and English by clicking the button in the upper right corner.

If you don't have an username, write your desired username in the field. An user will be automatically created.

If you forget your password, there's nothing you can do, but create a new user. You can, however, leace the password field blank.

Please consider that the usernames and passwords are saved as plaintext, and that to ensure your safety, _you should not use an username or a password that you use in any other service_.

## Using the placement generator

After you have succesfully logged in, you can start creating the placement, view your placement-creating statistics, log out or look at some info. If you choose to make a placement, the program opens a new view and asks you for a csv file. By clicking the button, you can select the desired file from your folders visually.

The file must have a very specific structure: 
- It must be comma-separated (you can save Excel documents in this format by selecting 'csv' as the filetype, and 'comma' as the delimiter)
- It must have only two columns, with the first of them having the names (Firstname Lastname), and the second having the seating wishes as first names or full names, separated within the cell by a comma
- The first row of the file must have headers or other useless information. The first row will be discarded by the program.

If the file doesn't conform to these requirements, the program will probably not work.

The requirements exist mostly because of time limitations and also because this is the type of file that I've worked with when creating seating arrangements by hand.

The program also asks you for the number of tables you have in mind. The people you hopefully have your file full of will be divided into this many groups.

After you have succesfully given the needed information, a placement is made. You unfortunately cannot inluence the arrangement in other ways. You have the possibility of saving the placement as a csv file, which you can open, for example, with Excel or LibreOffice Calc. The contents of the file follow this format: each two rows are one table. Each two row table is separated from the next by an empty row. 
