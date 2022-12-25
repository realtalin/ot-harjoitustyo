# Visuaalimuisti

Visuaalimuisti on yksinkertainen visuaalista muistia testaava peli


## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/realtalin/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](https://github.com/realtalin/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Tuntikirjanpito](https://github.com/realtalin/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Arkkitehtuuri](https://github.com/realtalin/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](https://github.com/realtalin/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

## Julkaisut
- [Viikko 6](https://github.com/realtalin/ot-harjoitustyo/releases/tag/viikko6)
- [Viikko 5](https://github.com/realtalin/ot-harjoitustyo/releases/tag/viikko5)


## Asennus
- Asenna ohjelman riippuvuudet komennolla `poetry install`

## Komentorivikomennot
- Tietokannan alustus: `poetry run invoke initialize`
- Pelin käynnistys: `poetry run invoke start`  
- Yksikkötestit: `poetry run invoke test`  
- Testikattavauusraportti: `poetry run invoke coverage-report`  
- Lint-tarkistus: `poetry run invoke lint`  
