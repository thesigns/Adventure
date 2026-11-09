# Zasady gry

## Tworzenie postaci

Przed rozegraniem scenariusza gracz tworzy postać: określa jej imię, wiek, płeć, gatunek, profesję i historię oraz zalety, wady i poziom doświadczenia (zwykle zerowy), od których zależy bazowa liczba Punktów Determinacji, a MG ustala jej ekwipunek startowy. Punktem odniesienia jest przeciętny przedstawiciel gatunku i profesji postaci, więc cechy typowe dla nich nie są zaletami ani wadami. Pełne zasady tworzenia postaci są w `Rules/CharacterCreation.md`.

## Karta postaci

Karta postaci gracza jest zapisana w pliku `Character.md` w folderze jej kampanii, np. `Campaigns/Randuvil/Character.md` (zob. `Rules/CharacterCreation.md`). MG pilnuje jej stanu i aktualizuje ją na bieżąco, gdy tylko coś się zmieni, m.in.:

- bieżące PDT po każdym wydaniu punktów i odnowieniu puli,
- poziom zranienia i urazy po każdej ranie i każdej dobie leczenia,
- ekwipunek: zdobyte, utracone, zużyte i uszkodzone przedmioty oraz liczbę amunicji, źródeł światła, prowiantu i innych zapasów,
- pieniądze,
- cechy i bazowe PDT, gdy postać zyska albo straci zaletę lub wadę,
- punkty doświadczenia po ich przyznaniu, a poziom doświadczenia i bazowe PDT po awansie,
- wątki fabularne.

Karta jest źródłem prawdy o stanie postaci. Przy wznowieniu gry MG odczytuje stan postaci z karty.

## Rzut standardowy

Wszystkie niepewne rezultaty rozstrzyga się rzutem **3K6** według tablicy rezultatów, którą MG układa przed rzutem. Rzuca wyłącznie MG, zawsze skryptem `Scripts/roll.py`, a gracz może poprawić swoje szanse, wydając Punkty Determinacji. Pełne zasady rzutu standardowego, w tym kiedy rzucać, jak układać tablice rezultatów i jak oceniać trudność, są w `Rules/StandardThrow.md`.

## Punkty Determinacji

Punkty Determinacji (PDT) to wysiłek, upór i szczęście, które postać gracza może włożyć w ważne dla siebie działanie. Za każdy punkt wydany przed rzutem MG rzuca jedną kością więcej i odrzuca najsłabsze, a pula odnawia się po porządnym wypoczynku. Pełne zasady są w `Rules/Determination.md`.

## Zdrowie, rany i śmierć

Każda istota ma poziom zranienia od 0% (bez ran) do 100% (śmierć), który podnoszą rany, od draśnięcia po cios śmiertelny i zmasakrowanie. Od poziomu zranienia zależą kary do działań, a rany goją się tylko w minimalnie komfortowych warunkach. Pełne zasady, w tym skala ran, wytrzymałość istot, agonia, urazy, leczenie i śmierć, są w `Rules/Health.md`.

## Ekwipunek

Ekwipunek nie ma osobnej mechaniki: broń, pancerz, narzędzia i inne przedmioty działają jak okoliczności, które MG uwzględnia w tablicy rezultatów. Pancerz sprawia, że przeciwnik rzadziej rani postać i zadaje jej lżejsze rany, a przedmioty zużywalne, takie jak amunicja czy źródła światła, MG liczy na karcie postaci. Pełne zasady są w `Rules/Equipment.md`.

## Walka

Walka toczy się w rundach trwających około 10 sekund, a każda runda to jeden rzut standardowy z tablicą, która opisuje skutki dla obu stron. Przed walką gracz określa taktykę postaci, a walka trwa, dopóki się nie rozstrzygnie: śmiercią, agonią, ucieczką albo poddaniem się jednej ze stron. Rundy z tą samą tablicą gracz może zlecić jako serię, którą MG rzuca jednym poleceniem. Zmęczenie liczy się tylko w walce z kimś, kto męczy się wolniej albo wcale, i utrudnia ją co 6 rund. Pełne zasady walki, w tym kategorie przeciwników i typowy układ tablicy rundy, są w `Rules/Combat.md`.

## Cechy (zalety i wady)

Zaleta wyróżnia postać na tle przeciętnego przedstawiciela jej gatunku i profesji: ułatwia o jeden poziom działania ze swojej dziedziny albo umożliwia działania, które bez niej byłyby niemożliwe, a wada działa odwrotnie. Cechy wybiera się przy tworzeniu postaci, wpływają na bazową liczbę Punktów Determinacji i bardzo rzadko zmieniają się w trakcie gry. Zaleta może też dawać zdolność nadprzyrodzoną, której skutek, ograniczenia i limit użyć MG ustala przy wycenie. Pełne zasady są w `Rules/Traits.md`.

## Doświadczenie

Postać zaczyna zwykle na zerowym poziomie doświadczenia, a na koniec każdego scenariusza dostaje punkty doświadczenia za dokonania, które określa scenariusz albo ocenia MG. Punkty wydaje się jak walutę na awans: przejście na poziom *n* kosztuje *n* × 1000 punktów. Każdy poziom daje postaci 1 bazowy Punkt Determinacji i podnosi o 1 górny limit bazowych PDT. Pełne zasady są w `Rules/Experience.md`.

## Zmęczenie, głód i światło

- **Brak snu:** każda doba bez snu utrudnia wszystkie działania o jeden poziom, aż do przespanej nocy.
- **Głód:** każdy dzień bez jedzenia utrudnia wszystkie działania o jeden poziom, aż do posiłku.
- **Ciemność:** działanie w ciemności, które wymaga wzroku, jest trudniejsze o jeden poziom, a w całkowitej ciemności o dwa.
- **Źródła światła** działają przez ograniczony czas, który określa świat (zob. *Przedmioty zużywalne* w `Rules/Equipment.md`).

MG śledzi porę dnia i upływ czasu.

## Rzut monetą

Nierozwiązywalny spór między graczem a MG, np. o przebieg wydarzeń albo interpretację zasady, rozstrzyga rzut monetą skryptem `Scripts/coin.py`. Moneta wskazuje „Rację ma MG” albo „Rację ma gracz”, a rozstrzygnięcie jest ostateczne. Pełne zasady są w `Rules/CoinThrow.md`.

## Zasady świata

Zasady podstawowe są wspólne dla wszystkich światów. Świat opisuje setting w katalogu `Settings/` albo, jeśli scenariusz nie korzysta z żadnego settingu, sam scenariusz. Setting może uzupełniać zasady podstawowe, a scenariusz jedne i drugie. W razie sprzeczności rozstrzyga scenariusz, potem setting, a na końcu zasady podstawowe. Świat określa w szczególności:

- konwencję i klimat gry,
- przykłady przeciwników w każdej kategorii i wytrzymałość istot,
- przykłady pancerzy lekkich, średnich i ciężkich,
- tempo leczenia gatunków innych niż człowiek i dodatkowe sposoby leczenia,
- magię, modlitwę i inne moce nadprzyrodzone, jeśli istnieją,
- sprzęt, ceny, wierzchowce, pojazdy i przedmioty niezwykłe, np. czas działania źródeł światła.
