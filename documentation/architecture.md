
## Structure

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
    Participants: dict participiants
    Participants: list has_friendgroup
    Participants: list placed_fin
    Participants: initialize()
  
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
  The UI uses the attributes and methods of the class Placement, which uses Participants as a data structure.

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
  This is what happens if everything goes well.
  
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
  P-->>U: you can enter
  ```
  This happpens if the username doesn't exist.
  
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
  L-->>U: "here's your placemnt"
  U->>L: "save it here"
  L-->>U: "ok"
```
  
  Here's what happens next.
