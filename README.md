# Ohjelmistotekniikka Harjoitustyö

## Seating Placement Generator
The application creates seating arrangements for parties. The seating is influenced by the wishes of the participants. The program uses csv-files.

### Documentation

[Requirements specification](https://github.com/HeljaeRaeisaenen/ohte-harjoitusty-/blob/main/documentation/requirements_spec.md)

[Architecture](https://github.com/HeljaeRaeisaenen/ohte-harjoitusty-/blob/main/documentation/architecture.md)

[Work hour log](https://github.com/HeljaeRaeisaenen/ohte-harjoitusty-/blob/main/documentation/workhourlog.md)

[Changelog](https://github.com/HeljaeRaeisaenen/ohte-harjoitusty-/blob/main/documentation/changelog.md)


## Release
[release](https://github.com/HeljaeRaeisaenen/ohte-harjoitusty-/releases/tag/viikko5)

## Installing and terminal commands
The program can be installed from the previous section titled Release. 

To have it work properly, you must have poetry installed:

`poetry install`

To run the program, type:

`poetry run invoke start`

in the directory where the program is.

### Important

To use the program, you need a csv file with n rows and exactly 2 columns, with the first column containing names (Firstname Lastname), and the second, the names of the wished company, preferably separated by a comma. The file must use a comma as the delimiter. It's assumed that the first row contains headers, and will be ignored. In case you don't have such a specific file, [here's a file you can test the program on](https://github.com/HeljaeRaeisaenen/ohte-harjoitusty-/blob/main/src/data/testi.csv). In the src/data folder there are some more files. All the files have been created just for testing purposes.

### Commands
- To run unit tests for the program:

`poetry run invoke test`


- To see a summary of save the results of the tests in an html file:

`poetry run invoke coverage-report`


- To check the code with pylint:

`poetry run invoke lint`

