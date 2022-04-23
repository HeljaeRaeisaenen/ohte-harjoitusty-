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

### Commands
To run unit test for the program:

`poetry run invoke test`


To see a summary of save the results of the tests in an html file:

`poetry run invoke coverage-report`


Or to view the results instantly in your browser:

`poetry run invoke coverage-html`


To check the code with pylint:

`poetry run invoke lint`

