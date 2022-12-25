# Arkkitehtuuri

## Rakenne
Ohjelman pakkausrakenne on seuraavanlainen:  
  
![pakkausrakenne](./kuvatiedostot/rakennekaavio.png)

__Services__-pakkauksen __game__-pakkaus sisältää pelilogiikan. __Database__-pakkaus vastaa tietokantaoperaation rajapinnasta muille luokille, ja __repositories__-pakkaus vastaa itse tietokantaoperaatioista. __UI__:ssa olevat luokat vastaavat pelin ja menujen piirtämisestä. Pakkaus __sprites__ sisältää piirrettävät objektit.

## Sovelluslogiikka

Pelin logiikka pohjautuu GameLoop-luokkaan, joka päivittää pelin tilannetta jatkuvasti. GameLoopin suhdetta muihin luokkiin kuvaa seuraava luokkakaavio:


### Luokkakaavio

```mermaid
classDiagram
  GameLoop "1" -- "1" Clock
  GameLoop "1" -- "1" EventQueue
  GameLoop "1" -- "1" Mouse
  GameLoop "1" -- "1" Game
  Game "1" -- "1" Level
  Level "1" -- "*" Cell
```

Game-luokka huolehtii meta-tason pelilogiikasta, joka ei liity yksittäiseen tasoon, kuten pisteiden ja jäljellä olevien elämien laskeminen. Game-olio luo aina uuden Level-olion kun pelaaja läpäisee edellisen. Level koostuu monista Cell-olioista. Level luo oikean vastauksen ja tarkistaa, painaako käyttäjä oikeita soluja vai ei.

Luokkia Clock, EventQueue ja Mouse on vain yksi, ja ne injektoidaan GameLoopille sen konstruktorissa.

Seuraava sekvenssikaavio on esimerkki tilanteesta, jossa pelaaja on vastannut edelliseen tasoon oikein, ja luodaan uusi taso.


## Uuden tason luominen
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

## Tietojen tallennus

Pelaajien saavuttamat tulokset tallennetaan SQLite-tietokantaan. Tulosten tallennuksessa hyödynnetään Repository-suunnittelumallia. Tulosten tallentamisesta vastaavat ScoreService ja ScoreRepository-luokat.

## Tuloksen tallentaminen
```mermaid
sequenceDiagram
  participant GameLoop
  participant Game
  participant ScoreService
  participant ScoreRepository
  GameLoop->>Game: game_over()
  Game-->>GameLoop: True
  GameLoop->>Game: save_score()
  Game->>ScoreService: save(game.username, game.score)
  ScoreService->>ScoreRepository: save(score)
```
