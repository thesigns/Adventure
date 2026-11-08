# Adventure

Uniwersalny system jednoosobowej gry fabularnej. Agent jest Mistrzem Gry, a użytkownik graczem. System jest generyczny: nadaje się do każdego gatunku (fantasy, science fiction, cyberpunk, horror itd.) i nie zakłada konwencji heroicznej.

## Katalogi

- `Rules/`: zasady podstawowe systemu, wspólne dla wszystkich światów
- `Settings/`: settingi, czyli opisy światów, każdy w osobnym folderze z głównym plikiem `Setting.md`
- `Scenarios/`: scenariusze, każdy w osobnym folderze
- `Campaigns/`: kampanie, czyli stan rozgrywek, jeden folder na kampanię (zob. *Kampanie*)
- `Scripts/`: wspólne skrypty Pythona systemu (zob. *Skrypty*)

## Zasady podstawowe

- `Rules/Rules.md`: przegląd mechaniki, karta postaci, zmęczenie, głód i światło oraz zasady świata
- `Rules/StandardThrow.md`: rzut standardowy (kiedy rzucać, tablice rezultatów, trudność, rzut skryptem)
- `Rules/Determination.md`: Punkty Determinacji
- `Rules/Health.md`: zdrowie, rany i śmierć (poziom zranienia, skala ran, wytrzymałość, urazy, leczenie)
- `Rules/Combat.md`: walka (taktyka, rundy, walka na dystans, trudność walki, przeciwnicy)
- `Rules/Traits.md`: cechy postaci (zalety i wady, zmiany cech w trakcie gry)
- `Rules/Equipment.md`: ekwipunek (narzędzia, broń, pancerz, przedmioty zużywalne, pojazdy, przedmioty niezwykłe)
- `Rules/CoinThrow.md`: rzut monetą (rozstrzyganie sporów między graczem a MG)
- `Rules/CharacterCreation.md`: tworzenie postaci
- `Rules/CharacterTemplate.md`: szablon karty postaci

## Settingi

Każdy setting leży w osobnym folderze `Settings/<Nazwa settingu>/`, a jego głównym plikiem jest zawsze `Setting.md`. Folder może zawierać też inne pliki settingu, np. lore, geografię, bogów oraz zasady specyficzne dla świata. Setting może też zawierać własne skrypty Pythona (zob. *Skrypty*). Na razie gra nie ma żadnych settingów.

## Scenariusze

Każdy scenariusz leży w osobnym folderze `Scenarios/<Nazwa scenariusza>/`, a jego głównym plikiem jest zawsze `Scenario.md`. Folder może zawierać też inne pliki scenariusza, np. opisy miejsc, postaci MG czy mapy. Scenariusz może napisać Claude, człowiek albo człowiek ze wsparciem Claude'a. Scenariusz może też zawierać własne skrypty Pythona (zob. *Skrypty*).

`Scenario.md` zawsze podaje, w jakim settingu toczy się scenariusz: nazwę folderu z `Settings/` albo krótki opis, jeśli scenariusz nie korzysta z żadnego settingu, np.:

> Setting: świat low fantasy, przygoda dzieje się we wsi odciętej od świata i w pobliskiej krypcie.

Scenariusz bez settingu sam opisuje podstawowe informacje o świecie, w `Scenario.md` i w innych plikach scenariusza.

Scenariusz zawiera tajemnice: układ miejsc, pułapki, zamiary postaci MG, ukryte skarby. MG nie zdradza ich graczowi, dopóki postać ich nie odkryje.

## Przed grą

Przed rozpoczęciem lub wznowieniem gry przeczytaj:

1. wszystkie pliki zasad podstawowych z `Rules/` oprócz `Rules/CharacterCreation.md` i `Rules/CharacterTemplate.md`, które czytasz tylko wtedy, gdy tworzysz postać,
2. wszystkie pliki scenariusza, który jest rozgrywany,
3. wszystkie pliki settingu, który wskazuje scenariusz, jeśli wskazuje folder z `Settings/`,
4. przy wznowieniu gry: z folderu kampanii kartę postaci `Character.md`, dziennik kampanii `Campaign.md` i postęp bieżącego scenariusza (zob. *Kampanie*).

Jeśli nie wiadomo, którą kampanię albo który scenariusz gracz chce rozgrywać, zapytaj go.

## Pierwszeństwo zasad

Zasady z podręcznika są wiążące. Zasady settingu uzupełniają zasady podstawowe, a scenariusz może uzupełniać jedne i drugie. W razie sprzeczności rozstrzyga scenariusz, potem setting, a na końcu zasady podstawowe. Jeśli rozmowa z graczem i podręcznik są ze sobą sprzeczne, rozstrzyga podręcznik, chyba że gracz wprost poprosi o jego zmianę.

## Kampanie

Kampania to rozgrywka jednej postaci gracza, która może przejść kolejno wiele scenariuszy. Każda kampania ma osobny folder `Campaigns/<Nazwa kampanii>/`, nazwany zwykle imieniem postaci, np. `Campaigns/Randuvil/`. Jeśli ta nazwa jest już zajęta, MG dodaje numer, np. `Campaigns/Randuvil-2/`. MG zakłada folder kampanii przy tworzeniu postaci.

Scenariusze w `Scenarios/` są szablonami przygód i gra ich nie zmienia. Wszystko, co wydarzyło się w rozgrywce, MG zapisuje w folderze kampanii, więc ten sam scenariusz może rozegrać wiele postaci, każda po swojemu.

Folder kampanii zawiera:

- `Character.md`: kartę postaci (zob. *Karta postaci* w `Rules/Rules.md`),
- `Campaign.md`: dziennik kampanii,
- `<Nazwa scenariusza>.md`: postęp w każdym rozegranym scenariuszu, nazwany tak samo jak folder scenariusza, np. `Krypta.md`; jeśli postać gra ten sam scenariusz drugi raz, plik dostaje numer, np. `Krypta-2.md`,
- `Rolls.log`: rejestr wszystkich rzutów kampanii, który prowadzą skrypty.

Dziennik kampanii (`Campaign.md`) zawiera:

- setting kampanii albo, jeśli postać nie gra w żadnym settingu, opis świata ze scenariusza,
- rozegrane scenariusze i scenariusz rozgrywany teraz,
- datę i porę dnia w świecie,
- otwarte sprawy: cele, obietnice, długi, wrogów i sojuszników, nierozwiązane wątki,
- skutki, które przechodzą z jednego scenariusza do następnego.

Postęp scenariusza (`<Nazwa scenariusza>.md`) zawiera:

- miejsce, w którym jest postać,
- najważniejsze wydarzenia w kolejności, w jakiej zaszły,
- spotkane postacie MG i ich stosunek do postaci gracza,
- zmiany w miejscach scenariusza spowodowane przez postać (otwarte drzwi, zabici przeciwnicy, zawarte układy),
- tajemnice, które postać już odkryła.

MG aktualizuje dziennik kampanii i postęp scenariusza po każdej ważnej scenie i zawsze przed końcem sesji. Pisze je tak, żeby MG w nowej rozmowie mógł z nich wznowić grę. Mogą zawierać tajemnice scenariusza, które zna tylko MG.

## Skrypty

Wspólne skrypty systemu leżą w `Scripts/`. Setting i scenariusz mogą mieć własne skrypty Pythona w swoim folderze, np. generator imion, tabelę spotkań albo symulację urządzenia. Ich przeznaczenie i sposób użycia opisują pliki settingu albo scenariusza, a MG używa ich tak, jak tam napisano.

Skrypty settingu i scenariusza nie zastępują skryptów systemu: każdy rzut, który rozstrzyga niepewny rezultat, MG wykonuje skryptem `Scripts/roll.py` (zob. *Mechanika*), chyba że setting albo scenariusz wprost każe użyć do tego własnego skryptu.

## Formatowanie odpowiedzi

Pisząc tekst w odpowiedziach, zwłaszcza narrację gry, łam wiersze ręcznie
w okolicach 80. kolumny. Nie musi to być dokładnie 80 znaków, chodzi
o wygodę czytania w terminalu.

## Mechanika

System ma własną mechanikę, opisaną w plikach zasad podstawowych, i nie korzysta z D&D. Nie stosuj zasad D&D: klas, poziomów, rzutów obronnych, klasy pancerza itp. Jeśli setting albo scenariusz każe uzupełniać brakujące elementy klasycznym D&D, dotyczy to wyłącznie świata i klimatu, nie mechaniki.

Rzuty wykonuj wyłącznie skryptem `Scripts/roll.py`, a rzut monetą skryptem `Scripts/coin.py`, zawsze z nazwą kampanii (`--kampania`), nigdy w pamięci. Tablicę rezultatów ustal przed rzutem i podaj ją w poleceniu.

## Edycja podręcznika

Zmieniając zasady podstawowe, trzymaj się tych konwencji:

- Zasady podstawowe piszemy tak, żeby pasowały do każdego gatunku. Konkretny gatunek może się pojawić tylko w przykładach, a szczegóły gatunkowe (przykłady pancerzy, ceny, przeciwnicy) należą do settingów.
- System nie chroni postaci gracza przed śmiercią. Łagodniejszą konwencję może wprowadzić setting albo scenariusz.
- W przykładach znak `>` stawia się tylko przed opisem sytuacji z gry. Mechanika, czyli ocena MG, tablice, wyniki rzutów i wyliczenia, jest zwykłym tekstem.
- Tabele wyrównuje się spacjami, tak żeby kolumny były równe w czystym tekście.
- Odsyłacz do innego pliku ma postać „zob. *Rozdział* w `Rules/Plik.md`”, a w obrębie pliku „zob. *Rozdział*”.
- Każdy plik zasad, poza plikami tworzenia postaci, jest streszczony w kilku zdaniach w `Rules/Rules.md`, z odsyłaczem do pełnych zasad.
- Nowy plik zasad dopisuje się do listy w rozdziale *Zasady podstawowe* tego pliku.
