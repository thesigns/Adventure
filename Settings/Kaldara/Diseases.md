# Choroby

Rany i leczenie: `Rules/Health.md` i *Zdrowie i leczenie* w `Mechanics.md`.

## Czarny kaszel

Choroba śmiałków: łapie się ją głęboko pod ziemią, mija na powierzchni. Uczeni z Domu Visara: „choroba głębin”.

### Co wiedzą ludzie

- Objawy: suchy kaszel, czarna plwocina o poranku, potem duszność, na końcu gorączka i dławienie.
- Chorują ci, którzy długo siedzą pod ziemią: śmiałkowie, rzadziej górnicy. Im dłużej i głębiej, tym gorzej.
- Przyczyna: suche purchawki, popielatoszare, wielkości pięści, które rosną w głębokich ruinach i jaskiniach. Są suche i kruche: nadepnięte albo potrącone pękają i wypuszczają chmurę czarnego pyłu, a po dobie przychodzi kaszel.
- Purchawki pękają też pod trollami i robalami, więc pył może wisieć w powietrzu, zanim przyjdzie człowiek.
- Śmiałkowie omijają suche purchawki i uczą tego młodszych. Najwięcej ich w najgłębszych poziomach ruin.
- Chory zdrowieje po dłuższym pobycie na powierzchni. Kto zostaje pod ziemią, umiera.
- Nie przechodzi z człowieka na człowieka.
- Trolle i stwory z Głębin są na nią odporne.
- Zielarki i kapłani nie mają na nią lekarstwa.

### Prawda (nie wie nikt na wyspie)

- Purchawki przyszły z Głębin. Razem z trollami zgubiły krasnoludy (zob. `Dwarves.md`).

### Zakażenie

- Gdzie rosną suche purchawki, ustala scenariusz.
- Ukryty rzut MG, bez PDT, tablice z `gm_tables.json`:
  - postać nadepnie albo potrąci purchawkę albo wejdzie w wiszący pył: przeciętne (`k3`),
  - przejście przez salę, której posadzkę pokrywają purchawki: trudne (`k4`),
  - każde kolejne trzy doby w Głębinach albo na najgłębszych poziomach ruin: łatwe (`k2`).
- Kto widzi purchawki i idzie ostrożnie, nie nadepnie. W kurzu i popiele ruin łatwo je przeoczyć. Rzut tylko po ciemku, w biegu, w walce, w ciasnym przejściu albo gdy pył już wisi.
- Przykład: `python Scripts/roll.py --kampania <kampania> --ukryty --etykieta c1 --tablica k3`
- Kaszel zaczyna się po dobie.
- Chory nie rzuca ponownie: nowe zakażenie od razu pogłębia chorobę o stopień.

### Stopnie

Działa jak uraz przejściowy (zob. *Urazy* w `Rules/Health.md`). Kary się nie sumują, każdy stopień zastępuje poprzedni.

1. **Kaszel:** skradanie i długi wysiłek (bieg, wspinaczka, marsz z ciężarem) o poziom trudniejsze.
2. **Duszność:** walka, bieg, wspinaczka i dźwiganie o poziom trudniejsze, skradanie o dwa. PDT się nie odnawia.
3. **Gorączka:** wszystko o poziom trudniejsze, skradanie o dwa. PDT się nie odnawia.

- Pod ziemią: +1 stopień co dwie doby. Na 3. stopniu każda doba pod ziemią to lekka rana, aż do śmierci.
- Na powierzchni: −1 stopień co dwie doby, o każdej porze roku. Po 1. stopniu zdrowy.
- Nic innego nie leczy. Przebyta choroba nie chroni przed następną.
