# Test Documentation

The application has been tested both with unit tests and manually via the user interface.

## Automated testing
The application logic classes Participant and Placement have their own test files containing unit tests. These are in the _tests_-directory within the source directory. The ParticipantsRepo-class is tested by testing the Placement class: the functionality of these two is so intertwined, that Placement can't be used without ParticipantsRepo, and testing both of them together is intuitive. The database_functions-module is tested within its own test file.

The coverage of the unit tests is 85%.

![image](https://user-images.githubusercontent.com/94612974/167952325-5da0cece-9195-4805-bbb8-1570df2f0f1a.png)


## Manual testing

The app has been installed on a Linux system following the instrutions in the [user manual](), after which it has been tested by hand, mimicking how an actual user would use it. The app has been given input that is of the wrong type and format, as well as good input which it can use. 

## Problems in quality
The app has an error message about the inputted file having too many or too few rows or columns. This is given to the user whenever an index error occurs within the application logic, and therefore can be shown to the user even when the file's format is perfect. This is a lazy feature that relies on the assumption that the application logic will not raise index errors with correctly formatted input; however, there's no guarantee that this is the case. The approach to error messages and error handling is a bare-bones one, however the testing hasn't been able to crash the program as it is now.
