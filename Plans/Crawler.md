# Crawler: plan roboczy

Roboczy tytuł nowego settingu, a może i rozszerzenia zasad. Miasteczko i loch, jak w roguelike'ach i grach typu hack and slash, ale grany jak klasyczna sesja RPG: jeden gracz, Claude Code jako MG. Pisany po polsku; gotowe pliki trafią do `Settings/` (i ew. `Rules/`) po angielsku.

## Założenia

- **Setting, nie nowy podręcznik:** zaczynamy od settingu z własnymi zasadami, które rozszerzają rdzeń (pierwszeństwo zasad pozwala). Nowe zasady rdzenia dopiero, gdy playtest pokaże, że rdzeń przeszkadza.
- **Świat osobny i mroczny,** nie część Generii; nie obowiązuje zasada sztampy.
- **Inspiracje klimatu** (tylko nastrój, bez nazw, postaci, miejsc i mechanik z tych dzieł):
  - *Diablo 1:* jedno miasteczko nad zejściem w coraz głębszy, coraz gorszy mrok; gotycki horror; mała, znajoma obsada na powierzchni,
  - *Warhammer Fantasy Roleplay:* świat ponury i niebezpieczny, zwykli ludzie zamiast herosów, brud, zepsucie, czarny humor, wczesna nowożytność,
  - *Deadwood:* miasteczko z gorączki złota bez prawa, szara moralność, walka o władzę i pieniądze, wyraziste, nieidealne postacie.
- **Śmierć permanentna,** jak w roguelike'ach: poległa postać nie wraca. Po śmierci gra zaczyna się od nowa: nowa postać, nowe Miasteczko i nowy Loch. Jedna rozgrywka (od powstania postaci do jej śmierci albo zwycięstwa) to jedna kampania w `Campaigns/`.
- **Bez nazw własnych:** Miasteczko to po prostu Miasteczko, a Loch to po prostu Loch (po angielsku *the Town* i *the Dungeon*). Celowo, inaczej niż w Generii, gdzie gołe rzeczowniki jako nazwy są zakazane.
- **Każda droga do dna:** grę da się przejść czystym magiem, czystym wojownikiem i postacią mieszaną. Strefy martwej magii to tylko pojedyncze komnaty; czysty mag może je obejść albo poradzić sobie niemagicznymi środkami (kostur, alchemia, mikstury ziołowe, najemnicy).
- **Rdzeń pasuje:** zmęczenie, głód i światło (pochodnie i racje jako zasoby), rany i śmierć bez ochrony postaci, walka z grupami i rojami, ekwipunek, doświadczenie, ukryte rzuty.

## Miasteczko

- **Gorączka złota:** miasteczko na pograniczu, założone kilka lat temu. Poszukiwacze złota w kopalni przebili się do Lochu.
- **Kopalnia stanęła,** kiedy z dołu zaczęło coś wychodzić. Jedni chcą zasypać szyb, inni zarabiają na śmiałkach. Miasteczko może zbankrutować albo rozkwitnąć, zależnie od tego, co gracz zrobi w Lochu: postęp kampanii widać też na powierzchni (lepszy towar, rozbudowana karczma, nowe twarze).
- **Pogranicze:** mało prawa, szybkie pieniądze, szybkie noże; każdy przybył tu z jakiegoś powodu.
- **Mieszkańcy:** większość to bezimienni górnicy, poszukiwacze i awanturnicy w namiotach i chałupach z bali. Nazwani są tylko stali mieszkańcy (zob. *Pętla gry*).
- **Stopnie głębokości:** najpłytsze poziomy to sztolnie kopalni, znajome i porzucone w pośpiechu (narzędzia, wózki); niżej właściwy Loch, stary, obcy i coraz gorszy. Gracz czuje moment przekroczenia granicy.

## Klimat i technologia

- **Weird west jako klimat, nie sprzęt:** miasteczko z gorączki złota, saloon, kaznodzieja, szeryf z pistoletem i rapierem, pogranicze bez prawa i coś pradawnego na dnie Lochu.
- **Technologia wczesnonowożytna** (fantasy czarnoprochowe, jak Europa XVI wieku). Miecze, topory, halabardy i kusze są wciąż powszechne. Broń czarnoprochowa istnieje (pistolety kołowe, arkebuzy, garłacze), ale jest droga, głośna, wolno się ładuje i zawodzi w wilgoci, za to mocno rani. Druk, kompasy, mechanizmy zegarowe; bez broni powtarzalnej.
- **Wzór do pliku settingu:**

  > **Technology:** early modern, like 16th-century Europe. Swords, axes, halberds and crossbows remain the common weapons. Black-powder firearms exist: wheellock pistols, arquebuses, blunderbusses. They are costly, loud, slow to reload and fail in the damp, but hit hard. Printing, compasses and clockwork; no repeating firearms.

- **Skutki dla gry:**
  - **jeden strzał na walkę:** przeładowanie trwa kilka rund, więc pistolet to mocne otwarcie, potem broń ręczna; broń ręczna jest niezbędna,
  - **proch i kule to zasób** obok pochodni i racji; proch w wilgotnych sztolniach może zamoknąć,
  - **ciężka zbroja traci sens,** bo kula ją przebija: kirysy, hełmy, skórznie.
- **Ludy tubylcze:** własne, wymyślone ludy i dawni mieszkańcy Lochu, bez sięgania po prawdziwe kultury i ich stereotypy.

## Pętla gry

Miasteczko → zejście → walka i łupy → powrót → sprzedaż, leczenie, zakupy → głębiej.

- **Głębokość jako trudność:** trudność to liczba od 0 do 1: numer poziomu podzielony przez liczbę poziomów Lochu. W Miasteczku 0, na dnie zawsze 1; np. w Lochu z 15 poziomami poziom 1 ma 1/15 ≈ 0,07, a poziom 12 ma 12/15 = 0,8. Od trudności zależą potwory, pułapki i łupy: tabele mają progi w zakresie 0–1 (np. stwór pojawia się od trudności 0,4). Trudność jest sekretem: zdradza głębokość Lochu, więc skrypty liczą ją same i nigdy jej nie wypisują.
- **Łupy:** dużo przedmiotów, część magicznych i nieznanych do identyfikacji (np. u Wiedźmy za opłatą).
- **Stali mieszkańcy:** sześć postaci, każda z własną usługą w pętli gry i własnym wątkiem, który rozwija się między zejściami:
  Mieszkańcy to archetypy: rola i usługa są stałe, a imiona, wygląd, charakter i osobiste wątki losuje się od nowa w każdej rozgrywce (skrypt, z sekretami ukrytymi jak w `Gm.json`).
  - **Kowal:** broń i zbroje, naprawy, ulepszanie.
  - **Karczmarz:** nocleg (odnowienie PD), jedzenie, plotki, najemnicy.
  - **Wiedźma:** mikstury na drogę, identyfikacja magicznych przedmiotów, zdejmowanie klątw i trucizn; wie rzeczy, o których kapłan woli nie mówić.
  - **Kupiec:** skupuje łupy, sprzedaje rzeczy codzienne (pochodnie, olej, liny, racje).
  - **Kapłan:** leczenie ciężkich ran i chorób, błogosławieństwa, pogrzeby.
  - **Burmistrz:** zadania i nagrody, historia Lochu i Miasteczka; powód, by schodzić głębiej niż po złoto. Najwięcej stracił, kiedy kopalnia stanęła.
- **Cel:** na dnie coś ostatecznego, żeby gra nie była niekończącym się grindem.

## Loch

- **Generowany, ale trwały w rozgrywce:** skrypt (np. `make_level.py`) tworzy poziom przy pierwszym zejściu i zapisuje go w kampanii. Postać, wracając, zastaje poziom takim, jakim go zostawiła.
- **Zgodny z `fogmap.py`:** generator tworzy od razu SVG i `.areas.json`, więc mgła wojny i `--plan` działają bez zmian.
- **Sekrety:** gracz widzi konsolę, więc generator nie może wypisywać zawartości pokoi. Zawartość zapisana ukryta (zaciemniona jak `Gm.json`), a komenda w rodzaju `crawl.py --enter 7` ujawnia pokój dopiero, gdy postać do niego wchodzi. MG nie trzyma lochu w pamięci ani w kontekście: źródłem prawdy jest plik.

- **Strefy martwej magii:** w niektórych komnatach magia nie działa (nigdy na całym poziomie), np. za ścianami z obsydianu. Nie działają tam też portale i teleportacja. Nie działa żadna magia, także przedmioty magiczne i magiczne mikstury. Działają tylko zwykłe wywary ziołowe i maści, bo nie są wzmocnione magią: mikstury dzielą się na ziołowe (słabsze, działają wszędzie) i magiczne (mocniejsze, zawodzą w strefach martwej magii). Przedmioty magiczne tracą moc, ale zostają tym, czym są: magiczny topór rani jak zwykły topór, magiczna zbroja chroni jak zwykła zbroja.

## Walka

- **Automatyczna domyślnie:** odwracamy domyślność *Series of rounds* z `Rules/Combat.md`. Gracz ustala taktykę, walka toczy się sama do pierwszego zdarzenia przerywającego: rana postaci, upadek lub ucieczka wroga, nowy wróg, wzrost zmęczenia, wyczerpanie budżetu PD.
- **Przy przerwie** gracz decyduje: walczy dalej, pije miksturę, zmienia taktykę, ucieka. Na życzenie gracza (np. z bossem) walka runda po rundzie.
- **Skrypt walki** (np. `fight.py`): zna kategorie wrogów, śledzi rany obu stron, sam przelicza tabelę po każdej ranie i zatrzymuje się na zdarzeniach. MG ustala taktykę i okoliczności, potem opisuje przebieg. Przy kilkunastu walkach na sesję ręczne przeliczanie tabel to za dużo okazji do błędu.
- **Szybkie potyczki:** większość spotkań krótka; pełna walka na bossów i spotkania, które coś znaczą.

## Punkty determinacji zamiast staminy

Stamina wydawana na walkę przy odnawianiu raz na dzień byłaby tym samym co PD. Zamiast nowego współczynnika:

- **PD odnawiają się tylko w Miasteczku** albo w rzadkim bezpiecznym miejscu w lochu. Zejście staje się wyprawą na wyczerpanie zasobów: każda walka zjada pulę, aż trzeba wracać.
- **Budżet walki:** przed walką gracz deklaruje, ile PD wydaje na rundę i ile najwyżej na całą walkę. Pasuje do walki automatycznej, bo gracz nie decyduje co rundę.
- **Osobna stamina tylko, jeśli playtest pokaże potrzebę:** wtedy jako fizyczny oddech (zmęczenie w walce jako licznik zerowany krótkim odpoczynkiem), czyli krótki zegar obok długiego (PD i rany). Ryzyko: kolejna liczba do pilnowania przy każdej walce.

## Otwarte pytania

- **Głębokość (wstępnie):** skończona, ale losowa, np. 2k6+8 poziomów (10–20, najczęściej 15), losowana ukrycie na początku rozgrywki. Osobnych znaków zbliżania się do dna nie ma: są nimi mocniejsze stwory, przedmioty i pułapki, które wynikają z trudności. Długość rozgrywki (ile sesji, wielkość poziomów, liczba poziomów) ustalimy w playtestach.
- **Generator czy ręcznie:** wszystko losowe czy kilka poziomów ręcznie (Miasteczko, kluczowe poziomy, dno), a reszta generowana?
- **Powrót na powierzchnię:** pieszo po schodach, a także zwojami i czarami (magiczny portal, teleportacja). Do ustalenia: czy portal działa w obie strony (powrót w to samo miejsce Lochu), jak rzadkie i drogie są zwoje.

## Notatki
