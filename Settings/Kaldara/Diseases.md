# Choroby

Ten plik opisuje choroby wyspy i ich mechanikę. Rany, urazy i leczenie opisują zasady podstawowe (zob. `Rules/Health.md`) i *Zdrowie i leczenie* w `Mechanics.md`.

## Czarny kaszel

Choroba śmiałków. Łapie się ją w ruinach i jaskiniach, głęboko pod ziemią, a leczy słońcem. Uczeni z Domu Visara nazywają ją w swoich zapiskach chorobą głębin.

### Co wiedzą ludzie

- Czarny kaszel zaczyna się od suchego kaszlu i czarnej plwociny o poranku. Potem przychodzi duszność, a w końcu gorączka, w której chory dławi się własnym oddechem.
- Chorują ci, którzy długo siedzą pod ziemią: śmiałkowie, rzadziej górnicy z Grimsfjord. Im dłużej i im głębiej, tym gorzej.
- Śmiałkowie mówią, że to od pyłu, od zimna ruin albo od klątwy krasnoludów. Starzy śmiałkowie wiążą na twarz mokrą chustę w zapylonych salach, a młodzi się z nich śmieją.
- Chory, który wróci na powierzchnię, zdrowieje, jeśli posiedzi na słońcu. Latem, w białe noce, mija to szybko. Zimą, gdy dzień trwa kilka godzin, śmiałek, który wrócił chory jesienią, kaszle często do wiosny. Kto zostaje pod ziemią z czarnym kaszlem, umiera.
- Czarny kaszel nie przechodzi z człowieka na człowieka. Nikt nie zaraził się od chorego, więc chorych nie wypędza się z domów.
- Kapłani Solvara wynoszą chorych na słońce i mówią, że to ich bóg wygania z nich ciemność. Zielarki nie mają na czarny kaszel lekarstwa.

### Prawda o czarnym kaszlu

Tego nie wie nikt na wyspie (zob. *Zasady dla MG* w `Setting.md`).

Czarny kaszel niosą zarodniki bladych grzybów, które rosną w Głębinach przy gorących źródłach i szczelinach z parą (zob. *Pożywienie* w `Trolls.md`). Trolle i inne stwory z Głębin są na nie odporne. Zarodniki rosną w płucach człowieka w ciemności, a giną w świetle dnia. Najgęściej jest ich tam, gdzie grzyby porosły całe sale, i za krasnoludzkimi murami zarazy (zob. *Prawda o krasnoludach* w `Dwarves.md`). To czarny kaszel, razem z trollami, zgubił krasnoludy.

### Zakażenie

Zakażone miejsca ustala scenariusz: sale porośnięte bladymi grzybami, zamurowane sale krasnoludów, najgłębsze poziomy ruin i jaskinie Głębin. Postać zwykle nie wie, że coś jej grozi, więc MG rzuca ukrytym rzutem, bez PDT, gdy postać:

- przejdzie przez salę gęsto porośniętą grzybami albo przebywa w niej dłużej: przeciętne,
- wejdzie do sali za rozbitym murem zarazy, gdzie zarodniki wiszą w powietrzu jak pył: trudne,
- spędzi każde kolejne trzy doby w Głębinach albo na najgłębszych poziomach ruin: łatwe.

Mokra chusta na twarzy ułatwia o poziom, a łatwe zakażenie z chustą nie wymaga rzutu. Pancerz nie chroni (zob. *Pancerz* w `Rules/Equipment.md`). Tablice są w `gm_tables.json`: `k2` łatwe, `k3` przeciętne, `k4` trudne, np.:

```
python Scripts/roll.py --kampania <kampania> --ukryty --etykieta c1 --tablica k3
```

Zarażona postać zaczyna kasłać po dobie. MG opisuje kaszel jak każdy objaw, bez wskazywania, skąd się wziął. Postać, która już choruje, nie rzuca ponownie: każde nowe zakażenie od razu pogłębia chorobę o stopień.

### Stopnie choroby

Czarny kaszel działa jak uraz przejściowy (zob. *Urazy* w `Rules/Health.md`) i zapisuje się go na karcie postaci w urazach razem ze stopniem. Kary stopni się nie sumują: każdy stopień zastępuje poprzedni.

1. **Kaszel:** suchy kaszel i czarna plwocina o poranku. Skradanie i długi wysiłek, np. bieg, wspinaczka albo marsz z ciężarem, są trudniejsze o poziom.
2. **Duszność:** kaszel napadami i brak tchu po kilku krokach. Walka, bieg, wspinaczka i dźwiganie są trudniejsze o poziom, a skradanie o dwa. Noc nie jest porządnym wypoczynkiem, więc PDT się nie odnawia (zob. *Odnawianie* w `Rules/Determination.md`).
3. **Gorączka:** gorączka, dławienie się i czarne usta. Wszystkie działania są trudniejsze o poziom, a skradanie o dwa. PDT się nie odnawia.

- **Pod ziemią** choroba pogłębia się o stopień co dwie doby bez światła dnia. Na trzecim stopniu każda kolejna doba pod ziemią przynosi lekką ranę z wycieńczenia, aż do śmierci.
- **Na powierzchni** choroba się nie pogłębia, nawet w ciemnym domu i w zimową noc.
- **Słońce** leczy. Postać, która przebywa pod gołym niebem przez większość dnia, choćby pod chmurami, cofa chorobę o stopień: od maja do sierpnia co dzień, w marcu, kwietniu, wrześniu i październiku co trzy dni, a od listopada do lutego co tydzień. Po cofnięciu pierwszego stopnia jest zdrowa. Przebyta choroba nie chroni przed następną.
- **Światło Solvara**, ogień ani maści nie leczą czarnego kaszlu. Leczy go tylko światło dnia.
