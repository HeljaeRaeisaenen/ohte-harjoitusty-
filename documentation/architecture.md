
## Structure

### Packaging structure
Or pakkausrakenne, I'm not sure what these terms are in English.

![packaging_structure](https://user-images.githubusercontent.com/94612974/166560603-d2c0b919-5ab0-4368-839c-7479ff890acf.png)

#### Application logic
```mermaid
classDiagram
  ParticipantsRepo-->Participant
  Placement-->ParticipantsRepo
  UI-->Placement

  class Participant
    Participant: str name
    Participant: str first_name
    Participant: list wishes

    Participant: bool placed
    Participant: tuple seat_coordinates
    
  class ParticipantsRepo
    ParticipantsRepo: dict participiants
    ParticipantsRepo: list has_friendgroup
    ParticipantsRepo: list placed_fin
    ParticipantsRepo: initialize()
  
  class Placement
    Placement: object ParticipantsRepo
    Placement: int tables_n
    Placement: list finished placement
    Placement: int total_wishes
    Placement: int wishes_placed
    Placement: check_everything_ok()
    Placement: count_wishes()
    Placement: create_tables()
    Placement: create_placement()
    
  class UI
  ```
  The UI uses the attributes and methods of the class Placement, which uses ParticipantsRepo as a data structure. The ParticipantsRepo contains objects of class Participant.

## The user interface
The user interface has three classes, and distinct views:

- a login view,
- "First view" which the user sees first, and from which they can access other views
- an "Info view", where the user receives information
- a "Begin placement" view where the user can give the program a file and specifications,
- and a "Finish placement" view, where the user can save the finished placement and log out.

A sixth class called UI controls the transitions between these. The class Begin in ui_begin_placement uses the application logic classes.

## Application logic

![logick](https://user-images.githubusercontent.com/94612974/166562289-a83cb828-1021-45ab-b08f-fa3a11120fa9.png)

The class Placement is responsible for the logical part of the program, with the aid of Participant and ParticipantsRepo. ParticipantsRepo makes use of Participant, and Placement makes use of ParticipantsRepo. ParticipantsRepo uses a filereading function from the package readwrite to read the partici??ants from a file, while turning the lines of the file into Participant-objects, with several useful attributes. The database classes and functions are only used from the UI.

Placement creates a placement, following four steps:

1. Initializing everything and making sure the user input is usable
2. Grouping the participants of the event, or the names in the inputted file, together placed on their wishes
3. Placing these groups in lists that represent tables, and will later be saved into  a csv file
4. Placing people left out in step 3 in the lists, and ensuring no one was left out

The logic isn't very refined, and it certainly can't make an optimal seating arrangement.

## Storing the information
The login credentials are stored in a local Sqlite database in plaintext.

The finished seating arrangement is saved in an csv file. The user can decide the location and name of the file.

## Main functionality
### The user logs in

```mermaid
sequenceDiagram
  actor U as User
  participant P as UI
  participant L as Login
  
  U->>P: enter (username, passwoed), click Login button
  P->>L: find_username(username)
  activate L
  L-->>P: ok
  P->>L: verify_password(password)
  L-->>P: ok
  deactivate L
  P-->>U: "you can enter"
  ```
  When the program is started, the user can log in. This is what happens if everything goes well.
  
  ```mermaid
sequenceDiagram
  actor U as User
  participant P as UI
  participant L as Login
  
  U->>P: enter (username, passwoed), click Login button
  P->>L: find_username(username)
  activate L
  L-->>P: "no username like that"
  P->>L: create_username(username, password)
  L-->>P: ok
  deactivate L
  P-->>U: "you can enter"
  ```
  This happpens if the username doesn't exist. A new user is automatically created.
  
  ### Use of the program once logged in
  
  ```mermaid
  sequenceDiagram
  actor U as User
  participant P as UI
  participant Pa as ParticipantsRepo
  participant L as Placement
  participant R as Read & Write files

  U->>P: enter csv-file and tables int, click Start button
  P->>Pa: crate ParticipantsRepo object, hand over the file
  activate Pa
  Pa->>R: read the file
  R-->>Pa: return file contents as a list
  Note right of Pa: Processes the list
  P->>L: create Placement object with ParticipantsRepo as an attribute
  activate L
  Note right of L: Does stuff with ParticipantsRepo
  L-->>P: return finished placement
  deactivate L
  deactivate Pa
  P-->>U: "here's your placemnt"
  U->>P: "save it here"
  P-->>U: "ok"
```
  
  The logic of the program is initiated from the user interface. This sequence happens when the user has succesfully given the program a csv file and a number for tables.
