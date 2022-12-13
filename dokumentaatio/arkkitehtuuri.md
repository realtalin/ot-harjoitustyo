# Arkkitehtuuri

## Rakenne
Ohjelman pakkausrakenne on seuraavanlainen:  
  
![pakkausrakenne](./kuvatiedostot/rakennekaavio.png)

Pakkaus __game__ sisältää pelilogiikan ja peliloopin. __UI__:ssa olevat luokat vastaavat pelin ja menujen piirtämisestä sekä käyttäjän syötteiden lukemisesta. __Services__-pakkauksessa on kellopalvelu pelille. __Components__ sisältää pelikentän, ja __sprites__ piirrettävät solut sekä niiden taustat.
 

## Luokkakaavio

```mermaid
classDiagram
  GameLoop "1" -- "1" Clock
  GameLoop "1" -- "1" EventQueue
  GameLoop "1" -- "1" Mouse
  GameLoop "1" -- "1" Game
  Game "1" -- "1" Playfield
  Playfield "1" -- "*" Cell
```
      
## Uuden Tason Luominen
```mermaid
sequenceDiagram
  participant GameLoop
  participant Clock
  participant Game
  participant Playfield
  participant Cell
  GameLoop->>Clock: get_time()
  Clock-->>GameLoop: current_time
  GameLoop->>Game: update_state(current_time)
  Game->>Playfield: all_correct_clicked()
  Playfield-->>Game: True
  Game->>Playfield: Playfield.create_playfield()
  Playfield->>Cell: Cell()
  Cell-->>Playfield: cells
  Playfield-->>Game: playfield
```
