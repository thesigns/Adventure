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

- Purchawki pochodzą z Głębin. Razem z trollami zgubiły krasnoludy (zob. `Dwarves.md`).

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

## Gorączka z rany

- Brudna rana ropieje i daje gorączkę. Ludzie wiedzą, że ranę trzeba przemyć i opatrzyć czystym płótnem.
- Rzut po każdej ranie (nie po draśnięciu), ukryty, bez PDT, tablice z `gm_tables.json`:
  - rana przemyta i opatrzona czystym płótnem: łatwe (`k2`),
  - rana nieopatrzona albo opatrzona brudnym: przeciętne (`k3`),
  - pazury i zęby trolla, robala, jaszczura albo szczurów, rana z bagna albo z ruin, nieopatrzona: trudne (`k4`).
- Gorączka zaczyna się następnego dnia.
- Skutki: wszystkie działania o poziom trudniejsze, rany się nie goją (zob. *Leczenie* w `Rules/Health.md`).
- Co rano jawny rzut, przeciętny; z opieką zielarki albo maścią łatwy, bez dachu trudny:

| Wynik | Rezultat                     |
|-------|------------------------------|
| 3–5   | gorączka rośnie: lekka rana  |
| 6–8   | gorączka trwa                |
| 9–18  | gorączka mija                |

## Gnilec

- Szkorbut. Choroba końca zimy i długich wypraw o suszonej rybie.
- Przychodzi po ok. sześciu tygodniach bez świeżego jedzenia: świeżego mięsa i ryb, ziół, jagód.
- Pierwszy stopień: krwawiące dziąsła, zmęczenie. Długi wysiłek o poziom trudniejszy, rany goją się o połowę wolniej.
- Po kolejnych czterech tygodniach: wypadają zęby, otwierają się stare rany. Wszystko o poziom trudniejsze, rany się nie goją.
- Leczy tydzień świeżego jedzenia na stopień. Ludzie wiedzą, że pomaga dzięgiel i jagody, a wiosną zbierają pierwsze zioła.

## Ślepota śnieżna

- Grozi w dzień na lodowcu i w śniegu bez osłony oczu.
- Pasterze i łowcy z gór noszą opaski z kości, drewna albo skóry z wąskimi szparami. Z opaską nie ma rzutu.
- Wieczorem jawny rzut, przeciętny; pod chmurami łatwy, w pełnym słońcu wiosną trudny. Porażka: ślepota.
- Skutki przez 1–3 dni: ból, łzawienie, działania wymagające wzroku o dwa poziomy trudniejsze.
- Leczy ciemność i zimne okłady.

## Inne choroby

- **Czerwonka:** od złej wody w obozach, w ferdzie i na Wielkim Tingu. Przez kilka dni wszystko o poziom trudniejsze, rany się nie goją.
- **Zapalenie płuc:** po nocy w mokrym ubraniu na mrozie albo po lodowatej wodzie. MG może je wpisać w tablicę zimna (zob. *Zimno* w `Mechanics.md`). Przebiega jak gorączka z rany.
