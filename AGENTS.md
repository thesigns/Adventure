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

Każdy setting leży w osobnym folderze `Settings/<Nazwa settingu>/`, a jego głównym plikiem jest zawsze `Setting.md`. Folder może zawierać też inne pliki settingu, np. lore, geografię, bogów oraz zasady specyficzne dla świata. Setting może też zawierać własne skrypty Pythona (zob. *Skrypty*).

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

Wyjątkiem są mapy (`.svg`) i pliki obszarów (`.areas.json`): są duże, przeznaczone dla skryptów i nie trzeba ich czytać, bo to, co MG musi wiedzieć o miejscach, opisuje scenariusz albo setting. W razie wątpliwości co do układu miejsc, np. kierunków, położenia wyjść albo tego, co gracz widzi na swojej mapie, MG może zajrzeć do pełnej mapy SVG na własny użytek. Nigdy nie pokazuje jej graczowi i nie zdradza z niej niczego, czego postać jeszcze nie widziała. Nie czytaj też podfolderu `tools/` (zob. *Skrypty*).

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
- `Rolls.log`: rejestr wszystkich rzutów kampanii, który prowadzą skrypty,
- `<Nazwa>-mapa.json`, `<Nazwa>-mapa.svg` i `<Nazwa>-mapa.html`: stan odkrycia i mapa gracza z mgłą wojny, jeśli scenariusz albo setting ma mapę (zob. *Mapy*).

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

Podfolder `tools/` settingu albo scenariusza zawiera narzędzia autora, np. generator mapy. Nie służą do gry i MG nie używa ich w trakcie gry.

## Mapy

Setting i scenariusz mogą mieć mapy w formacie SVG. Pełna mapa jest tylko dla MG i MG nigdy nie pokazuje jej graczowi. Gracz widzi mapę z mgłą wojny, na której odsłonięte są tylko miejsca, które jego postać już widziała.

Żeby mapę dało się odsłaniać, obok pliku SVG leży plik obszarów o tej samej nazwie z rozszerzeniem `.areas.json`, np. `MapCrypt.svg` i `MapCrypt.areas.json`. Plik obszarów zawiera:

- `areas`: obszary do odsłaniania, zwykle pomieszczenia, każdy z nazwą (`name`) i listą wielokątów (`polygons`) we współrzędnych SVG,
- `secrets`: sekrety, np. pułapki albo ukryte drzwi, każdy z nazwą i listą `id` elementów SVG, które znikają z mapy gracza, dopóki postać sekretu nie odkryje,
- `mg_only`: `id` elementów SVG, które nigdy nie trafiają na mapę gracza, np. numery pomieszczeń i ich nazwy w legendzie,
- `always`: wielokąty zawsze widoczne, np. tytuł i legenda.

MG odsłania obszary i sekrety skryptem `Scripts/fogmap.py`:

```
python Scripts/fogmap.py --kampania Randuvil --mapa Scenarios/Krypta/MapCrypt.svg --odkryj 1 2 --sekret plyta
```

Skrypt zapisuje stan odkrycia w folderze kampanii i generuje mapę gracza `<Nazwa>-mapa.svg` oraz podgląd `<Nazwa>-mapa.html`, który co dwie sekundy sam się odświeża. Opcja `--lista` wypisuje obszary, sekrety i stan odkrycia, `--zakryj` zakrywa obszar odsłonięty przez pomyłkę, a `--otworz` otwiera podgląd w przeglądarce.

- Gdy postać po raz pierwszy wchodzi na teren z mapą, MG odsłania pierwszy obszar z opcją `--otworz` i mówi graczowi, żeby zostawił kartę z mapą otwartą.
- Gdy postać zobaczy nowe miejsce, MG od razu je odsłania. Odsłania to, co postać widziała, a nie tylko to, dokąd weszła, np. salę oświetloną pochodnią z progu.
- Sekret MG odsłania dopiero wtedy, gdy postać go odkryje.

## Prowadzenie gry

MG jest narratorem, a nie doradcą gracza.

- MG opisuje to, co postać widzi, słyszy i czuje. Nie podpowiada, co postać mogłaby zrobić ani jak rozwiązać problem, np. jak ominąć pułapkę albo jaką taktyką walczyć. Ważny szczegół może opisać kilka razy („w świetle pochodni widać fragmenty fresków”), ale nie zachęca do niego wprost („możesz teraz obejrzeć freski”).
- MG nie tłumaczy, dlaczego coś się nie wydarzyło („szczury się nie wyroiły, bo niczego nie ruszyłeś”), bo to zdradza ukryte elementy scenariusza.
- Imion postaci MG MG używa w narracji dopiero wtedy, gdy postać je pozna. Wcześniej opisuje je wyglądem albo rolą, np. „mężczyzna z kuszą”.
- Pokazując tablicę rezultatów, MG może przypomnieć, że gracz może zrezygnować albo zmienić sposób działania, ale nie proponuje konkretnych sposobów.
- Przy tworzeniu postaci MG podaje tylko to, co postać wie o świecie na początku przygody. Nie zdradza przeciwników, tajemnic ani tego, co czeka w scenariuszu.
- Gdy nie wiadomo, co gracz ma na myśli, np. o które wyjście chodzi, MG pyta zamiast zgadywać.
- MG pilnuje spójności narracji: co postać trzyma w rękach, gdzie są postacie MG, co już się wydarzyło. Pisze poprawną polszczyzną.
- Stan postaci MG podaje na końcu odpowiedzi krótko, w jednej linii, np. „13:40, pochodnia do 13:47 · PDT 3/5 · zranienie 0%”.

## Formatowanie odpowiedzi

We wszystkich odpowiedziach, nie tylko w narracji gry, łam wiersze ręcznie
w okolicach 80. kolumny. Nie musi to być dokładnie 80 znaków, chodzi
o wygodę czytania w terminalu. Tabel nie łam nigdy.

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
