
## Structure

```mermaid
classDiagram
  Placement-->Participants
  UI-->Placement

  class Participants
    Participants: list names
    Participants: list firstnames
    Participants: list wishes
    Participants: list placed
    Participants: initialize()
  
  class Placement
    Placement: list file
    Placement: list friendgroups
    Placement: int tables
    Placement: list finished placement
    Placement: create_friendgroup(personindex)
    Placement: place_friend_immeadiate(personindex, friends, i, maximum)
    Placement: place_friend_secondary(personindex, friends, i)
    Placement: combine_friendgroups()
    
  class UI
  ```
  The UI uses the attributes and methods of the class Placement, which uses Participants as a data structure.
