# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on yksinkertainen peli, jolla voi testata visuaalista muistiaan. Peli tulee olemaan vastaavanlainen kuin esimerkiksi Human Benchmark -sivun [Visual Memory](https://humanbenchmark.com/tests/memory) -peli.

## Käyttöliittymä

Sovelluksessa on kolme eri näkymää
- [x] Päänäkymä, josta pääsee kahteen alanäkymään:
  - [x] Pelinäkymä
  - [ ] Parhaat tulokset -näkymä

## Perustoiminnallisuus

- [ ] Käyttäjä voi antaa käyttäjänimen
  - Käyttäjänimi toimii kuten monissa vanhoissa PC-peleissä, eli se ei ole sinänsä tunnus, vaan vapaasti valittava nimi
- [x] Käyttäjä voi aloittaa uuden pelin
- [x] Käyttäjä voi pelata muistipeliä
  - [x] Peli loppuu, kun käyttäjä epäonnistuu liian monta kertaa
- [x] Käyttäjä voi lopettaa pelaamisen kesken
- [ ] Käyttäjän saavuttamat tulokset tallentuvat lokaaliin tietokantaan käyttäjänimellä
- [ ] Käyttäjä voi katsoa parhaita tuloksia
 
## Jatkokehitysideoita

- Pelin parametrit tallennetaan käyttäjän muokattavissa olevaan konfiguraatiotiedostoon
  - Parametreja voi olla esimerkiksi pelikentän koko ja sen kasvu, muistettavien ruutujen määrän kasvu, sallittujen epäonnistumisien määrä, aika jonka muistettavat ruudut ovat näkyvissä
- Graafinen näkymä parametrien muuttamiseen itse pelissä
- Monimutkaisempia pelimuotoja, kuten esim. ruutujen ilmestyminen eri aikoihin, taustaruudukon katoaminen
