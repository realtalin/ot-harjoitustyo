# Testaus

Peliä on testattu automatisoiduilla yksikkötesteillä unittestilla sekä manuaalisesti.

## Yksikkötestaus

### Pelilogiikka

Pelilogiikkaa on testattu testaamalla GameLoop, Game ja Level-luokkia luokissa TestGameLoop, TestGame ja TestLevel. GameLoop-luokan riippuvuudet on toteutettu Mock- tai Stub-olioina. Pelin ja tasojen tärkeimmät perustoiminnallisuudet on yksikkötestattu.

### Tulosten tallennus

Tulosten tallennus on testattu kattavasti testaamalla ScoreService ja ScoreRepository-luokkia luokissa TestScoreService ja TestScoreRepository. Testitietokannan nimi on määritelty .env.test-tiedostoon. ScoreServicen testeissä ScoreRepositoryn sijasta käytetään Mock-olioa.

## Manuaalinen testaus

Sovelluksen asennus ja vaatimusmäärittelyn ominaisuudet on testattu manuaalisesti kolmella eri Linux-asennuksella.