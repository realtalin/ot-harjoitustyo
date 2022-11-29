# Luokkakaavio

```mermaid
 classDiagram
      Playfield "1" -- "*" Cell
      GameLoop "1" -- "1" Playfield
      GameLoop "1" -- "1" Clock
      GameLoop "1" -- "1" EventQueue
      GameLoop "1" -- "1" Mouse
      
