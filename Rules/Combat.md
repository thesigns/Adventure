# Walka

## Taktyka

Przed walką gracz opisuje **taktykę** postaci, czyli jak postać walczy, np. „rąbię go mieczem”, „strzelam zza wozu” albo „próbuję go rozbroić i pojmać żywcem”. Jeśli gracz jej nie określi, MG o nią pyta.

Taktyka wyznacza, jakie skutki mogą się znaleźć w tablicy rundy. Postać, która chce pojmać przeciwnika żywcem, nie zabija go przypadkiem, a postać, która strzela zza osłony, trudniej trafić.

Po każdej rundzie MG opisuje przebieg walki, a gracz może na tej podstawie zmienić taktykę, uciec, poddać się albo zrobić coś innego (zob. *Między rundami*). Postać nie ucieka ani nie poddaje się sama w trakcie rundy: o tym gracz decyduje między rundami.

## Rundy

Walka toczy się w **rundach**. Runda to krótka wymiana ciosów rozstrzygana jednym rzutem z własną tablicą rezultatów. Trwa około 10 sekund, więc sześć rund to mniej więcej minuta. MG uwzględnia to, śledząc upływ czasu, np. ile pali się pochodnia albo kiedy nadejdzie pomoc. Walka trwa, dopóki się nie rozstrzygnie: jedna ze stron ginie, pada w agonii, ucieka albo się poddaje, albo dzieje się coś innego, co kończy walkę (nadchodzi pomoc, przeciwnik zostaje odpędzony).

Przed każdą rundą MG pokazuje graczowi tablicę, a gracz decyduje, ile Punktów Determinacji wydaje na tę rundę (zob. *Decyzja gracza* w `Rules/StandardThrow.md`). Przed pierwszą rundą, jeśli postać może się jeszcze wycofać, gracz może też zmienić taktykę albo zrezygnować z walki.

Tablica rundy opisuje skutki dla obu stron: na niskich wynikach przeciwnik rani postać, na wysokich postać rani przeciwnika, a pomiędzy jest wymiana bez rozstrzygnięcia. Pas bez rozstrzygnięcia jest wąski, żeby walka nie ciągnęła się bez końca. Rany zadane w rundzie od razu zmieniają zranienie obu stron, a więc i trudność następnej rundy.

MG zna zranienie przeciwnika przed rzutem, więc wpisuje w tablicę skutki wprost: „bandyta pada”, „bandyta ucieka ranny”.

Walkę z wyraźnymi etapami (np. potyczka ze strażą, po której nadchodzi jej dowódca) MG może podzielić na kilka osobnych walk.

## Między rundami

Po rundzie, która nie zakończyła walki, MG opisuje sytuację, także stan przeciwnika, a gracz decyduje, co dalej. Może:

- walczyć dalej tak samo,
- zmienić taktykę, np. odpędzać zwierzę pochodnią zamiast rąbać je mieczem albo wycofać się za osłonę,
- zrobić coś innego niż walka: uciec, poddać się, wypić miksturę, pomodlić się, zawołać o pomoc.

MG układa tablicę następnej rundy zgodnie z decyzją gracza. Działanie inne niż walka zajmuje rundę: jego tablica opisuje, czy się udało i czy przeciwnik w tym czasie zranił postać. Poddanie się kończy walkę bez rzutu, chyba że reakcja przeciwnika jest niepewna.

Postać w agonii nie walczy dalej. Co dzieje się z nią potem, zależy od przeciwnika (zob. *Koniec walki*).

## Seria rund

Gdy kolejne rundy mają tę samą tablicę, bo gracz walczy dalej tak samo, wydaje na każdą rundę tyle samo Punktów Determinacji, a zranienie żadnej ze stron nie zmienia trudności, gracz może zlecić serię rund. MG pokazuje tablicę raz i rzuca całą serię jednym poleceniem skryptu z opcjami `--rundy` i `--stop` (zob. *Rzut skryptem* w `Rules/StandardThrow.md`).

W `--stop` MG podaje wyniki, po których sytuacja się zmienia: zwykle rany postaci gracza oraz rany, po których przeciwnik pada, ucieka albo zmienia zachowanie. Jeśli przeciwnik może paść dopiero po kilku ranach, MG ustawia `--rundy` tak, żeby seria skończyła się najpóźniej w rundzie, w której mógłby paść. Seria kończy się też, gdy zmieni się okoliczność spoza tablicy, np. zgaśnie pochodnia albo nadejdzie pomoc.

Po serii MG opisuje przebieg walki runda po rundzie, a gracz znów decyduje, co dalej (zob. *Między rundami*).

## Zmęczenie w walce

Gdy obie strony męczą się tak samo, zmęczenie nie ma znaczenia. Liczy się tylko wtedy, gdy jedna strona męczy się wyraźnie wolniej albo wcale, np. człowiek walczy z golemem, nieumarłym lub robotem.

Strona, która się męczy, po każdych 6 rundach ciągłej walki, czyli mniej więcej po minucie, dostaje okoliczność „zmęczenie”: walka staje się dla niej trudniejsza o pół poziomu (obie wartości przesuwają się o 1, zob. *Trudność walki*). Zmęczenie się kumuluje: po 12 rundach to już poziom, a po 18 półtora. Mija po kilku minutach odpoczynku.

Zaleta w rodzaju dobrej kondycji wydłuża ten czas do 12 rund, a wada w rodzaju astmy skraca go do 3. Reguła działa w obie strony: jeśli to postać gracza się nie męczy, zmęczenie przeciwnika ułatwia jej walkę.

Seria rund kończy się najpóźniej w rundzie, w której przybywa zmęczenia, bo zmienia się trudność walki (zob. *Seria rund*).

## Walka na dystans

Gdy postać gracza strzela do przeciwnika, MG ustala, co w tym czasie robi przeciwnik, zgodnie z jego naturą, uzbrojeniem i sytuacją: odpowiada ogniem (jeśli ma czym), skraca dystans, kryje się albo ucieka (jeśli ma dokąd). Na tej podstawie układa tablicę rundy. Przeciwnik, który odpowiada ogniem, może zranić postać już w tej rundzie. Przeciwnik, który biegnie ku postaci, zwykle jej jeszcze nie rani, ale na niskich wynikach dopada ją i walka przechodzi w zwarcie.

Gdy przeciwnik strzela do postaci gracza, a postać go widzi, MG przed ułożeniem tablicy pyta gracza, co robi postać, np. czy odpowiada ogniem, kryje się, szarżuje albo ucieka. Tablica zależy od odpowiedzi: postać, która się kryje, na wysokich wynikach dociera do osłony bez szwanku, ale nie rani przeciwnika. Jeśli postać nie widzi strzelca, np. łucznika w zasadzce, MG rzuca od razu, bez pytania (zob. *Decyzja gracza* w `Rules/StandardThrow.md`).

Im większy dystans, tym trudniej trafić: każda wyraźnie większa odległość utrudnia strzał o jeden poziom. Cel poza zasięgiem broni jest nieosiągalny, a strzał po prostu się nie udaje, bez rzutu (zob. *Kiedy rzucać* w `Rules/StandardThrow.md`). Na przykład nóż rzucony w ogra oddalonego o 200 metrów nie doleci.

Zasięg jest też okolicznością walki. Atak z dystansu na przeciwnika, który nie może odpowiedzieć tym samym, ułatwia walkę, a broń dystansowa w zwarciu ją utrudnia. Osłona utrudnia trafienie (zob. *Pancerz* w `Rules/Equipment.md`).

## Trudność walki

Z kategorii przeciwnika (zob. *Przeciwnicy*) wynikają dwie wartości:

- **próg trafienia:** wynik równy progowi lub wyższy oznacza, że postać rani przeciwnika,
- **zakres rany:** wyniki z tego zakresu oznaczają, że przeciwnik rani postać.

Okoliczności zmieniają trudność walki jak przy każdym innym działaniu (zob. *Okoliczności* w `Rules/StandardThrow.md`): o 2 punkty za każdy poziom i o 1 punkt za pół poziomu (zob. *Poziom w punktach* w `Rules/StandardThrow.md`). To, którą wartość przesuwa okoliczność, zależy od tego, czego dotyczy:

- **atak postaci** przesuwa tylko próg trafienia, np. celowanie w głowę albo inny słaby punkt, broń lepsza albo gorsza niż typowa, odległość strzału, osłona i pancerz przeciwnika,
- **obrona postaci** przesuwa tylko zakres rany, np. pancerz, tarcza i osłona postaci, broń przeciwnika lepsza albo gorsza niż typowa, broń, która zmusza postać do wpuszczenia przeciwnika blisko,
- **cała walka** przesuwa obie wartości, np. zranienie i zmęczenie obu stron, zaskoczenie, teren, ciemność, zalety i wady dotyczące walki oraz każdy dodatkowy przeciwnik, który czyni walkę trudniejszą o jeden poziom.

Jeśli opis okoliczności mówi po prostu, że utrudnia albo ułatwia walkę, dotyczy ona całej walki. Utrudnienie podnosi próg trafienia albo poszerza zakres rany, a ułatwienie działa odwrotnie.

Jeśli zakres rany po przesunięciu znika, przeciwnik nie może zranić postaci. Jeśli próg trafienia przekracza 18, postać nie może zranić przeciwnika tym sposobem walki. Jeśli zakres rany sięga progu trafienia albo dalej, wyniki wspólne oznaczają, że obie strony ranią się nawzajem.

Postać celuje w głowę przeciętnego przeciwnika (próg trafienia 9, zakres rany 3–6) i jest lekko ranna. Celowanie to okoliczność ataku (+2 do progu), a rana dotyczy całej walki (+1 do obu wartości): próg trafienia 12, zakres rany 3–7.

Okoliczność, która dotyczy tylko części walki, liczy się tylko w tych rundach, np. zaskoczenie zwykle tylko w pierwszej.

## Rany w walce

Rana zależy od dwóch stron: od tego, czym się atakuje, i od tego, kto jest celem.

- **Broń albo natura atakującego:** każda broń i każdy atak mają **rozpiętość ran**, od najlżejszej rany przy słabym trafieniu do najcięższej przy najlepszym. Na przykład proca zadaje od draśnięcia do rany, miecz od draśnięcia do ciężkiej rany, a czar kula ognista od draśnięcia do zmasakrowania. Typową ranę, czyli ranę od pełnego trafienia w człowieka bez pancerza, podaje *Skala ran* (zob. `Rules/Health.md`): pies gryzie, zadając lekką ranę, a niedźwiedź ciężką.
- **Cel:** rodzaj istoty i jej wytrzymałość (zob. *Wytrzymałość* w `Rules/Health.md`), pancerz, tarcza i osłona (zob. *Pancerz* w `Rules/Equipment.md`) przesuwają ranę o stopień albo więcej. Ten sam cios miecza zabija szczura, rani człowieka, a rycerza w zbroi płytowej ledwie drapie. Dotyczy to obu stron: postaci gracza i przeciwnika.

MG ustala rozpiętość ran po uwzględnieniu obu stron i rozkłada ją w tablicy: im bardziej skrajny wynik, tym cięższa rana.

## Typowy układ tablicy rundy

Od najniższych wyników:

| Wynik                                    | Rezultat                                                        |
|------------------------------------------|-----------------------------------------------------------------|
| 3                                        | przeciwnik zadaje ranę o stopień cięższą od typowej, walka trwa |
| reszta zakresu rany                      | przeciwnik zadaje typową ranę, walka trwa                       |
| od końca zakresu rany do progu trafienia | wymiana bez rozstrzygnięcia, walka trwa                         |
| od progu trafienia do 16                 | postać zadaje przeciwnikowi typową ranę                         |
| 17–18                                    | postać zadaje ranę o stopień cięższą od typowej                 |

Przy broni o dużej rozpiętości ran MG wpisuje w tablicę więcej stopni. Gdy przeciwnik ciska w postać kulą ognistą, na wyniku 3 może być zmasakrowanie, a na najwyższych wynikach zakresu rany tylko draśnięcie.

W obrębie tego układu MG może wydzielić inne skutki, np. utratę broni, uszkodzenie pancerza, ucieczkę przeciwnika albo uraz.

## Przeciwnicy

| Przeciwnik | Przykłady                               | Trudność walki    | Próg trafienia | Zakres rany |
|------------|-----------------------------------------|-------------------|----------------|-------------|
| słaby      | wyrostek z nożem, chłop z widłami, pies | łatwa             | 6              | 3–4         |
| przeciętny | bandyta, strażnik, wilk                 | przeciętna        | 9              | 3–6         |
| silny      | weteran, niedźwiedź                     | trudna            | 11             | 3–9         |
| potężny    | wielka bestia, mistrz miecza            | bardzo trudna     | 13             | 3–11        |
| legendarny | istota z legend                         | prawie niemożliwa | 16             | 3–14        |

Kategoria mówi, jak groźny jest przeciwnik w walce, a wytrzymałość, jak trudno go zranić. To dwie różne rzeczy: mistrz miecza jest potężnym przeciwnikiem o ludzkiej wytrzymałości.

Świat podaje własne przykłady przeciwników w każdej kategorii.

## Koniec walki

Zwycięstwo nie musi oznaczać śmierci przeciwnika. Przeciwnicy zachowują się zgodnie z naturą. Ludzie i zwierzęta zwykle uciekają albo się poddają, gdy są ranni albo walka idzie źle. Istoty pozbawione instynktu samozachowawczego walczą do końca. MG uwzględnia to w tablicach.

Postać gracza, która pada w agonii, jest bezbronna. Przeciwnik postępuje z nią zgodnie ze swoją naturą: może ją dobić, ograbić, pojmać albo zostawić. Jeśli jego reakcja jest niepewna, MG rozstrzyga ją rzutem.

Walka do końca z silniejszym przeciwnikiem jest bardzo niebezpieczna, bo rany się sumują, a każda kolejna utrudnia walkę. Z istotą legendarną kończy się niemal pewną śmiercią: rozsądna postać ucieka albo szuka innego sposobu. MG opisuje przebieg rund tak, żeby gracz widział, kiedy walka idzie źle.

## Przykłady

> Wojownik bez zbroi, postać gracza, schodzi do piwnicy i natyka się na olbrzymiego szczura.

Taktyka gracza: „rąbię go mieczem”. Szczur to słaby przeciwnik (próg trafienia 6, zakres rany 3–4) o bardzo wątłej budowie: cios miecza (rana) zabija go od razu, bo jest o dwa stopnie cięższy (cios śmiertelny). Ugryzienie szczura to draśnięcie. Tablica pierwszej rundy:

| Wynik | Rezultat                                                |
|-------|---------------------------------------------------------|
| 3     | szczur dotkliwie gryzie w nogę (lekka rana), walka trwa |
| 4     | szczur gryzie w nogę (draśnięcie), walka trwa           |
| 5     | obaj chybiają, walka trwa                               |
| 6–18  | wojownik rozpłatuje szczura mieczem                     |

Wypada 5. Gracz nie chce ryzykować ugryzienia i postanawia odpędzić szczura pochodnią. MG układa tablicę następnej rundy dla nowego sposobu walki:

| Wynik | Rezultat                                      |
|-------|-----------------------------------------------|
| 3     | szczur gryzie w rękę (draśnięcie), walka trwa |
| 4–6   | szczur syczy, ale się nie cofa, walka trwa    |
| 7–18  | szczur ucieka w ciemność                      |

Szczur nie jest w stanie poważnie zagrozić wojownikowi: nawet seria ugryzień to najwyżej kilka lekkich ran.

> Nocą postać śpi przy ognisku. Budzi ją trzask gałęzi, a nad nią stoi bandyta z pałką.

MG pyta o taktykę. Gracz odpowiada: „Chwytam miecz, który leżał obok, i zrywam się na nogi”. Bandyta to przeciętny przeciwnik (próg trafienia 9, zakres rany 3–6) o ludzkiej wytrzymałości. Pałka zadaje lekką ranę, a miecz postaci ranę. Postać nie ma na sobie zbroi. Została zaskoczona we śnie, co utrudnia pierwszą rundę o jeden poziom: obie wartości przesuwają się o 2. Wycofać się postać już nie może, ale widzi przeciwnika, więc MG pokazuje tablicę i pyta tylko o Punkty Determinacji:

| Wynik | Rezultat                                               |
|-------|--------------------------------------------------------|
| 3     | bandyta trafia pałką w głowę (rana), walka trwa        |
| 4–8   | bandyta trafia w ramię (lekka rana), walka trwa        |
| 9–10  | postać zrywa się i odpiera atak, walka trwa            |
| 11–16 | postać rani bandytę mieczem (rana), bandyta ucieka     |
| 17–18 | postać ciężko rani bandytę (ciężka rana), bandyta pada |

Gracz uznaje, że to ważna chwila, i wydaje 1 PDT. MG rzuca 4K6 zamiast 3K6 i wypada 6: postać ma 10% zranienia i jest lekko ranna. Zaskoczenie już nie działa, ale lekka rana utrudnia walkę o pół poziomu, więc obie wartości przesuwają się o 1. Gracz walczy dalej tak samo i nie wydaje punktów:

| Wynik | Rezultat                                               |
|-------|--------------------------------------------------------|
| 3     | bandyta trafia pałką w głowę (rana), walka trwa        |
| 4–7   | bandyta trafia (lekka rana), walka trwa                |
| 8–9   | wymiana ciosów bez rozstrzygnięcia, walka trwa         |
| 10–16 | postać rani bandytę mieczem (rana), bandyta ucieka     |
| 17–18 | postać ciężko rani bandytę (ciężka rana), bandyta pada |

Wypada 12: bandyta ucieka ranny. Postać zostaje przy ognisku z 10% zranienia.
