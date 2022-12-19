# Arkkitehtuuri

## Rakenne
Ohjelman pakkausrakenne on seuraavanlainen:  
  
![pakkausrakenne](./kuvatiedostot/rakennekaavio.png)

__Services__-pakkauksen __Game__-pakkaus sisältää pelilogiikan. __UI__:ssa olevat luokat vastaavat pelin ja menujen piirtämisestä sekä käyttäjän syötteiden lukemisesta. Pakkaus __sprites__ sisältää piirrettävät objektit.

## Sovelluslogiikka

Pelin logiikka pohjautuu GameLoop-luokkaan, joka päivittää pelin tilannetta jatkuvasti. GameLoopin suhdetta muihin luokkiin kuvaa seuraava luokkakaavio:


### Luokkakaavio

```mermaid
classDiagram
  GameLoop "1" -- "1" Clock
  GameLoop "1" -- "1" EventQueue
  GameLoop "1" -- "1" Mouse
  GameLoop "1" -- "1" Game
  Game "1" -- "1" Playfield
  Playfield "1" -- "*" Cell
```

Game-luokka huolehtii meta-tason pelilogiikasta, joka ei liity yksittäiseen tasoon, kuten pisteiden ja jäljellä olevien elämien laskeminen. Game-olio luo aina uuden Level-olion kun pelaaja läpäisee edellisen. Level koostuu monista Cell-olioista. Level luo oikean vastauksen ja tarkistaa, painaako käyttäjä oikeita soluja vai ei.

Luokkia Clock, EventQueue ja Mouse on vain yksi, ja ne injektoidaan GameLoopille sen konstruktorissa.

Seuraava sekvenssikaavio on esimerkki tilanteesta, jossa pelaaja on vastannut edelliseen tasoon oikein, ja luodaan uusi taso.


## Uuden Tason Luominen
```mermaid
sequenceDiagram
  participant GameLoop
  participant Clock
  participant Game
  participant Level
  participant Cell
  GameLoop->>Clock: get_time()
  Clock-->>GameLoop: time
  GameLoop->>Game: update_state(time)
  Game->>Level: all_correct_clicked()
  Level-->>Game: True
  Game->>Level: Level.create_level()
  Level->>Cell: Cell()
  Cell-->>Level: cells
  Level-->>Game: level
```
