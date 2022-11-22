```mermaid
 classDiagram
      Monopoli "1" -- "1" Pelilauta
      Monopoli "1" -- "2..8" Pelaaja
      Monopoli "1" -- "2" Noppa
      Pelilauta "1" -- "40" Ruutu
      Ruutu "1" -- "*" Pelinappula
      Pelinappula "1" -- "1" Pelaaja
      Ruutu <|-- Aloitus
      Ruutu <|-- Vankila
      Ruutu <|-- Sattuma
      Ruutu <|-- Yhteismaa
      Ruutu <|-- Asema
      Ruutu <|-- Laitos
      Ruutu <|-- Katu
      Aloitus <.. Monopoli
      Vankila <.. Monopoli
      Sattuma "1" -- "*" Kortti
      Yhteismaa "1" -- "*" Kortti
      Katu "1" -- "4" Talo
      Katu "1" -- "1" Hotelli
      Katu "*" -- "1" Pelaaja
      class Ruutu{
          seuraava_ruutu
          toiminto()
      }
      class Kortti{
          toiminto()
      }
      class Pelaaja{
          saldo
      }
