# Choroby

Rany i leczenie: `Rules/Health.md` i *Zdrowie i leczenie* w `Mechanics.md`.

## Czarny kaszel

Choroba śmiałków: łapie się ją głęboko pod ziemią, mija na powierzchni. Uczeni z Domu Visara: „choroba głębin”.

### Co wiedzą ludzie

- Objawy: suchy kaszel, czarna plwocina o poranku, potem duszność, na końcu gorączka i dławienie.
- Chorują ci, którzy długo siedzą pod ziemią: śmiałkowie, rzadziej górnicy. Im dłużej i głębiej, tym gorzej.
- Przyczyna wg ludzi: pył, zimno ruin, klątwa krasnoludów.
- Chory zdrowieje po dłuższym pobycie na powierzchni, nikt nie wie dlaczego. Kto zostaje pod ziemią, umiera.
- Nie przechodzi z człowieka na człowieka.
- Zielarki i kapłani nie mają na nią lekarstwa.

### Prawda (nie wie nikt na wyspie)

- Niosą ją zarodniki bladych grzybów z Głębin (zob. *Pożywienie* w `Trolls.md`).
- Grzyby przypominają purchawki: blade kule od pięści do głowy. Nadepnięte albo potrącone pękają i wypuszczają chmurę czarnego pyłu.
- Pękają też pod trollami i robalami, które o nie ocierają, więc chmura może wisieć w powietrzu, zanim przyjdzie postać.
- Trolle i stwory z Głębin są odporne.
- Zarodniki żyją tylko w mikroklimacie podziemi, na powierzchni giną.
- Najgęściej rosną w Głębinach i na najgłębszych poziomach ruin.
- Razem z trollami zgubiła krasnoludy.

### Zakażenie

- Zakażone miejsca ustala scenariusz.
- Ukryty rzut MG, bez PDT, tablice z `gm_tables.json`:
  - postać nadepnie albo potrąci grzyb albo wejdzie w wiszącą chmurę: przeciętne (`k3`),
  - przejście przez salę, której posadzkę pokrywają grzyby: trudne (`k4`),
  - każde kolejne trzy doby w Głębinach albo na najgłębszych poziomach ruin: łatwe (`k2`).
- Kto widzi grzyby i idzie ostrożnie, nie nadepnie. Rzut tylko po ciemku, w biegu, w walce, w ciasnym przejściu albo gdy chmura już wisi.
- Przykład: `python Scripts/roll.py --kampania <kampania> --ukryty --etykieta c1 --tablica k3`
- Kaszel zaczyna się po dobie. MG opisuje go bez wskazywania przyczyny.
- Chory nie rzuca ponownie: nowe zakażenie od razu pogłębia chorobę o stopień.

### Stopnie

Działa jak uraz przejściowy (zob. *Urazy* w `Rules/Health.md`). Kary się nie sumują, każdy stopień zastępuje poprzedni.

1. **Kaszel:** skradanie i długi wysiłek (bieg, wspinaczka, marsz z ciężarem) o poziom trudniejsze.
2. **Duszność:** walka, bieg, wspinaczka i dźwiganie o poziom trudniejsze, skradanie o dwa. PDT się nie odnawia.
3. **Gorączka:** wszystko o poziom trudniejsze, skradanie o dwa. PDT się nie odnawia.

- Pod ziemią: +1 stopień co dwie doby. Na 3. stopniu każda doba pod ziemią to lekka rana, aż do śmierci.
- Na powierzchni: −1 stopień co dwie doby, o każdej porze roku. Po 1. stopniu zdrowy.
- Nic innego nie leczy. Przebyta choroba nie chroni przed następną.
