# Pierwsza noc w Szpitalu Czerniakowskim

Setting: TheStiffs

Scenariusz na jedną albo dwie sesje dla jednej postaci. Noc z 21 na 22 marca 1990 roku, Szpital Czerniakowski przy Stępińskiej na Dolnym Mokotowie (zob. *Szpital Czerniakowski* w `Settings/TheStiffs/Setting.md`). Postać jest pracownikiem nocnej zmiany albo pacjentem. O pierwszej w nocy zmarli wstają, a szpital, pełen chorych, umierających i ciał w kostnicy, staje się jednym z najgorszych miejsc w mieście. Celem jest przeżyć do świtu i wydostać się, sama albo z kimś.

Układ budynku, oddziały, ludzie i wydarzenia są wymyślone na potrzeby scenariusza. Prawdziwy szpital mógł w 1990 roku wyglądać inaczej.

## Tło

Środa, 21 marca 1990 roku, pierwszy dzień wiosny. Rano dzieci topiły Marzannę w Wiśle. Wieczór jest zimny i wietrzny, około dwóch stopni, a na ulicach stoi błoto. Szpital ma zwykły nocny dyżur: mało personelu, dużo chorych, zmęczeni ludzie, zepsuta winda osobowa i telefony, które dzwonią rzadko.

Nikt nie wie, co się stanie. Postać też nie. MG prowadzi pierwszą godzinę jak zwykłą noc w szpitalu i dopiero przez drobne znaki zapowiada to, co nadejdzie (zob. *Prowadzenie sztywnych* w `Settings/TheStiffs/Stiffs.md`).

## Postać gracza

Postać tworzy się według zasad podstawowych i settingu (zob. *Postacie* w `Settings/TheStiffs/Setting.md`). Gracz wybiera jedną z dwóch dróg.

### Pracownik szpitala

Postać jest na nocnym dyżurze. Ma przy sobie fartuch albo mundurek, klucze, które wynikają z jej pracy, latarkę albo zapalniczkę i drobne rzeczy z kieszeni. Reszta jej rzeczy leży w szatni dla personelu w piwnicy. Przykłady:

- **lekarz dyżurny** chirurgii albo interny: zaczyna w dyżurce lekarskiej na pierwszym piętrze; ma stetoskop, klucz do dyżurki i do szafki z lekami na oddziale; może wezwać pomoc przez telefon wewnętrzny,
- **pielęgniarka:** zaczyna w dyżurce pielęgniarskiej swojego oddziału; ma klucz do szafki z lekami, nożyczki, opatrunki,
- **sanitariusz** pogotowia albo szpitalny: zaczyna na izbie przyjęć albo przy karetce na podjeździe; jest silny i przyzwyczajony do pijanych i agresywnych,
- **salowa:** zaczyna w pomieszczeniu gospodarczym oddziału; zna każdy kąt szpitala, schody gospodarcze i windę towarową; nikt nie zwraca na nią uwagi,
- **portier albo palacz:** zaczyna w portierni przy głównym wejściu albo w kotłowni; ma klucze do drzwi, piwnic, strychu i dachu.

W 1990 roku nie ma jeszcze zawodu ratownika medycznego. Ludzi w karetkach nazywa się sanitariuszami, a z nimi jeździ lekarz albo felczer.

### Pacjent

Postać leży w szpitalu. Ma piżamę, szlafrok, kapcie i to, co zmieściło się w szafce przy łóżku: kubek, sztućce, książkę albo gazetę, papierosy, trochę pieniędzy. Ubranie, buty i dokumenty zabrano jej do depozytu na parterze. Gracz wybiera, dlaczego postać leży w szpitalu, a to ustala jej stan na początku gry:

| Powód pobytu                      | Oddział    | Stan na początku                                                                                   |
|-----------------------------------|------------|----------------------------------------------------------------------------------------------------|
| obserwacja po wstrząśnieniu mózgu | neurologia | 5% zranienia, poza tym sprawna                                                                     |
| zapalenie płuc albo ciężka grypa  | interna    | gorączka: wszystkie działania trudniejsze o poziom, aż do wyzdrowienia                             |
| trzeci dzień po operacji wyrostka | chirurgia  | 20% zranienia, szwy na brzuchu: bieg i walka grożą ich rozejściem                                  |
| złamana ręka w gipsie             | urazówka   | uraz przejściowy: jedna ręka unieruchomiona                                                        |
| złamana noga w gipsie             | urazówka   | uraz przejściowy: chodzi o kulach, ucieczka trudniejsza o dwa poziomy                              |
| operacja zaćmy                    | okulistyka | jedno oko zasłonięte opatrunkiem, działania wymagające wzroku trudniejsze o poziom, dopóki go nosi |
| zatrucie, płukanie żołądka        | interna    | 10% zranienia, osłabiona, poza tym sprawna                                                         |

Urazy i choroby z tej tablicy nie są wadami i nie zmieniają PDT (zob. *Urazy* w `Rules/Health.md`). Są ceną za to, że postać zaczyna w samym środku szpitala. Pacjent nie zna szpitala tak jak personel: wie tylko, jak dojść do swojej sali, toalety, palarni i windy.

Bez rzeczy z depozytu pacjent wychodzi w marcową noc w piżamie i kapciach albo boso. Bez butów ucieczka i skradanie po ulicy, gruzie i szkle są trudniejsze o poziom. Bez ciepłego ubrania po mniej więcej godzinie na dworze wszystkie działania są trudniejsze o poziom, dopóki postać się nie ogrzeje. Bez dokumentów w pierwszych dniach trudniej o pomoc milicji, wojska i urzędów.

## Szpital

Szpital to czteropiętrowy gmach z lat pięćdziesiątych, z piwnicą, strychem i płaskim dachem, oraz niski pawilon gospodarczy na tyłach, połączony z gmachem podziemnym korytarzem. Przed gmachem jest podjazd dla karetek i mały parking, za nim podwórze gospodarcze z wjazdem od bocznej ulicy. Całość otacza siatka z dwiema bramami.

### Mapa

Plan szpitala jest w pliku `MapHospital.svg` w folderze scenariusza (północ u góry, 1 kratka = 1 m). Na jednym arkuszu są rzuty wszystkich kondygnacji: od strychu i dachu, przez cztery piętra i parter, po piwnicę, a także pawilon gospodarczy z podwórzem. To mapa dla MG, z czerwonymi kodami obszarów. Graczowi MG pokazuje mapę z mgłą wojny (zob. *Mapy* w `AGENTS.md`), na której widać od początku tylko nagłówki kondygnacji i legendę.

Obszary do odsłaniania:

| Kod              | Obszar                                           |
|------------------|--------------------------------------------------|
| `dach`           | strych i dach                                    |
| `4-neurologia`   | IV piętro: neurologia                            |
| `4-laryngologia` | IV piętro: laryngologia, okulistyka, sala dzieci |
| `3-interna`      | III piętro: interna                              |
| `3-umierajacy`   | III piętro: sala dla umierających                |
| `2-urazowka`     | II piętro: urazówka, z gablotą przeciwpożarową   |
| `2-gipsownia`    | II piętro: gipsownia                             |
| `1-chirurgia`    | I piętro: chirurgia                              |
| `1-blok`         | I piętro: blok operacyjny                        |
| `1-intensywna`   | I piętro: sala intensywnej opieki                |
| `0-hol`          | parter: hol, portiernia i korytarz               |
| `0-izba`         | parter: izba przyjęć                             |
| `0-apteka`       | parter: apteka                                   |
| `0-dyrektor`     | parter: gabinet dyrektora                        |
| `0-przychodnia`  | parter: rejestracja i przychodnia                |
| `0-depozyt`      | parter: depozyt                                  |
| `0-zabiegowy`    | parter: gabinet zabiegowy przychodni             |
| `0-podjazd`      | teren przed gmachem: wejście główne i podjazd    |
| `P-korytarz`     | piwnica: korytarz i klatki schodowe              |
| `P-magazyn`      | piwnica: magazyn bielizny                        |
| `P-warsztat`     | piwnica: warsztat konserwatora                   |
| `P-wezel`        | piwnica: węzeł cieplny                           |
| `P-szatnie`      | piwnica: szatnie personelu                       |
| `P-kostnica`     | piwnica: kostnica i prosektorium                 |
| `P-tunel`        | piwnica: wejście do tunelu                       |
| `G-tunel`        | tunel z piwnicy do pawilonu                      |
| `G-kuchnia`      | pawilon: kuchnia                                 |
| `G-pralnia`      | pawilon: pralnia                                 |
| `G-kotlownia`    | pawilon: kotłownia                               |
| `G-garaz`        | pawilon: garaż z nyską                           |
| `G-podworze`     | podwórze gospodarcze i brama                     |

Mapę gracza MG prowadzi skryptem `Scripts/fogmap.py`, z nazwą kampanii postaci:

- Na początku gry MG odsłania obszar, w którym postać zaczyna, i otwiera graczowi podgląd mapy, który odtąd odświeża się sam. Pracownik zna szpital, więc MG odsłania mu od razu wszystkie piętra, parter i piwnicę bez kostnicy, tunelu i pawilonu, chyba że jego praca wymaga ich znajomości (salowa, portier, palacz). Pacjentowi MG odsłania tylko jego piętro i parter, przez który przyszedł.

  ```
  python Scripts/fogmap.py --kampania <kampania> --mapa Scenarios/TheStiffsHospital/MapHospital.svg --odkryj 3-interna 0-hol --otworz
  ```

- Za każdym razem, gdy postać zobaczy kolejne miejsce albo się o nim dowie, np. od pani Zofii o tunelu, MG odsłania je bez `--otworz`.
- Opcja `--lista` wypisuje obszary i stan odkrycia.

Na każdym piętrze jest długi korytarz z salami po obu stronach, dyżurka pielęgniarek, dyżurka lekarska, pomieszczenie gospodarcze, łazienka, toalety i palarnia na końcu korytarza. Piętra łączą trzy drogi:

- **główna klatka schodowa** przy wejściu,
- **schody gospodarcze** na końcu gmachu, wąskie i ciemne, od piwnicy po strych,
- **winda osobowa**, od tygodnia zepsuta, i **winda towarowa** na łóżka i wózki, od piwnicy do czwartego piętra, wolna i głośna. Kto jej używa, słyszy ją każdy na każdym piętrze, także sztywni.

### Drzwi, okna i telefony

- **Drzwi sal** są drewniane, z zamkiem. W mniej więcej trzech czwartych z nich klucz tkwi od środka. Czy jest w drzwiach danej sali, MG rozstrzyga rzutem jako okoliczność świata (3–8: nie ma klucza, 9–18: jest). Dyżurki, gabinety i pomieszczenia gospodarcze zamyka się na klucze, które ma personel. Drzwi kostnicy, apteki i wejścia do tunelu są stalowe.
- **Okna** są stare, skrzynkowe i dają się otworzyć. Od południa wychodzą na podjazd, wejście główne i parking, a od północy na podwórze gospodarcze i pawilon. Okna parteru od strony podjazdu i apteki są okratowane.
- **Rynny:** po elewacjach, na narożnikach i co kilkanaście metrów, biegną blaszane rury spustowe na zardzewiałych obejmach, także tuż przy oknach skrajnych sal. Zejście po rurze z pierwszego albo drugiego piętra jest przeciętne, a z trzeciego albo czwartego trudne. Ciężki człowiek obciąża obejmy, więc na najniższych wynikach któraś się wyrywa.
- **Pasy:** na internie, neurologii i izbie przyjęć są skórzane pasy do przypinania pobudzonych chorych do łóżek (zob. *Trzymanie i wiązanie* w `Settings/TheStiffs/Setting.md`).
- **Telefony:** w każdej dyżurce jest telefon wewnętrzny. Telefon miejski jest tylko w portierni i w gabinecie dyrektora.

### Piwnica

- **Kostnica i prosektorium.** Chłodnia z szufladami, stół sekcyjny, pomieszczenie dla rodzin, kantorek prosektoryjnego. Z korytarza prowadzą tu drzwi z zamkiem i winda towarowa. W chłodni leży pięć ciał (zob. *Kostnica*).
- **Szatnie personelu** z szafkami: ubrania, buty, torby, papierosy, czasem butelka.
- **Magazyn** bielizny, materacy i środków czystości, a za nim **warsztat** konserwatora z narzędziami: młotki, klucze, łom, siekiera do rąbania skrzyń.
- **Węzeł cieplny** z rurami i zaworami.
- **Wejście do podziemnego korytarza** do pawilonu gospodarczego. Drzwi zamyka się na kłódkę, a klucz mają portier, palacz i konserwator.

### Parter

- **Izba przyjęć** z poczekalnią, gabinetem zabiegowym i dwiema kozetkami. Od podjazdu wjeżdżają tu karetki przez podwójne drzwi.
- **Portiernia** przy głównym wejściu, z telefonem miejskim, tablicą z kluczami i radiem.
- **Depozyt** z ubraniami i rzeczami pacjentów, zamknięty na klucz, który ma portier i pielęgniarka z izby przyjęć.
- **Apteka szpitalna**, zamknięta na dwa zamki i kratę. Klucze ma kierowniczka apteki, która nocą jest w domu, a zapasowy komplet leży w sejfie w gabinecie dyrektora. W aptece są leki, opatrunki, spirytus i zamknięta szafka z morfiną.
- **Rejestracja i przychodnia**, nocą zamknięte i ciemne.
- **Gabinet dyrektora** z sejfem, telefonem i biurkiem pełnym papierów.

### Pierwsze piętro: chirurgia

- **Oddział chirurgii** z czterema salami po sześć łóżek.
- **Blok operacyjny** za podwójnymi drzwiami: dwie sale operacyjne, sterylizatornia, narzędzia chirurgiczne.
- **Sala intensywnej opieki** na cztery łóżka, przy bloku operacyjnym, z aparaturą i własną pielęgniarką.

### Drugie piętro: urazówka

- **Oddział chirurgii urazowo-ortopedycznej** z salami pełnymi ludzi w gipsach, na wyciągach i o kulach.
- **Gipsownia** z piłą do gipsu, nożycami i workami gipsu.
- **Gablota przeciwpożarowa** na korytarzu: gaśnica, wąż i siekiera strażacka za szybką z napisem „W razie pożaru zbić szybkę”. Taka gablota jest na każdym piętrze, ale siekiera wisi tylko w tej. Z pozostałych dawno zginęły.

### Trzecie piętro: interna

- **Oddział chorób wewnętrznych**, największy w szpitalu, z salami starych ludzi z sercem, płucami i cukrzycą. Tu najczęściej ktoś umiera.
- **Sala dla umierających** na końcu korytarza, za parawanem.

### Czwarte piętro: neurologia, laryngologia i okulistyka

- **Neurologia** z ludźmi po udarach, sparaliżowanymi i nieprzytomnymi.
- **Laryngologia i okulistyka** z mniejszymi salami, w tym salą dla dzieci po wycięciu migdałków.

### Strych i dach

Ze schodów gospodarczych prowadzą zamknięte drzwi na strych, a ze strychu metalowa drabinka i klapa na płaski dach. Z dachu widać cały Dolny Mokotów, Siekierki z kominami elektrociepłowni, skarpę, Łazienki i Wisłę. Nie ma z niego zejścia, chyba że po rynnie albo po linie.

### Pawilon gospodarczy

Niski budynek za gmachem, na podwórzu gospodarczym: kuchnia z zapasami na kilka dni dla całego szpitala, pralnia, kotłownia z palaczem i garaż z jedną nyską sanitarną, starą, ale na chodzie. Kluczyki do nyski wiszą w portierni. Z pawilonu prowadzi brama na boczną ulicę.

## Postacie MG

- **Dr Andrzej Kozłowski**, chirurg, lekarz dyżurny szpitala, pięćdziesiąt lat. Zmęczony, cyniczny, kompetentny. W szufladzie dyżurki trzyma spirytus. Do końca próbuje leczyć, bo nie umie inaczej. Gdy zrozumie, co się dzieje, będzie chciał ratować pacjentów, a nie siebie.
- **Siostra Halina Wójcik**, pielęgniarka oddziałowa interny, pięćdziesiąt pięć lat, pobożna i stanowcza. Ma klucze do szafek z lekami na internie. Nie zostawi chorych. Zmarłych, którzy wstają, uzna za znak końca świata i będzie się modlić, ale nie ucieknie.
- **Maria Sobczak**, nocna pielęgniarka neurologii, czterdzieści lat. Ciepła, zmęczona, z dziewięcioletnim stażem u boku siostry Haliny. Jej mąż Zbyszek jest kierowcą autobusu. Pilnuje też laryngologii i okulistyki na tym samym piętrze. Na pozostałych oddziałach dyżuruje po jednej pielęgniarce, której imię MG nadaje sam.
- **Ewa Lis**, stażystka na internie, dwadzieścia sześć lat. Pierwszy samodzielny dyżur. Przerażona, ale bystra: pierwsza zrozumie, że ugryzieni umierają od ran, a nie od „wścieklizny”.
- **Pani Zofia Gajewska**, salowa, sześćdziesiąt lat. Zna każdy kąt szpitala, klucze do schowków i podziemny korytarz. Nikt jej nie słucha, a ona wie najwięcej.
- **Pan Kazimierz Sowa**, portier, emerytowany podoficer, sześćdziesiąt pięć lat. Ma klucze do wszystkiego, radio tranzystorowe i stary pistolet sygnałowy w szufladzie. Słucha rozkazów, więc w chaosie szuka kogoś, kto je wyda.
- **Kapral Robert Nowicki**, milicjant z patrolu, trzydzieści lat. O północy przywozi na izbę przyjęć pobitego pijaka i zostaje, żeby spisać zeznania. Ma pistolet P-64 z sześcioma nabojami w magazynku i drugim magazynkiem. Uważa, że panuje nad sytuacją. Myli się.
- **Zdzisław „Zdzichu” Malec**, pobity pijak, którego przywiózł milicjant, czterdzieści lat, cinkciarz z Jarmarku Europa. W skarpecie ma zwitek dolarów. Gdy wytrzeźwieje, okaże się sprytny i gotów na wszystko, żeby przeżyć.
- **Pan Edward Kamiński**, pacjent sali dla umierających na internie, osiemdziesiąt lat, rak płuc. Umrze tej nocy (zob. *Przebieg nocy*). Czeka na księdza.
- **Ksiądz Tadeusz**, wikary z pobliskiej parafii, wezwany do pana Edwarda. Przychodzi po północy z olejami świętymi. Młody, odważny, nie wierzy w upiory, dopóki ich nie zobaczy.
- **Pan Stefan Rogala**, prosektoryjny, pięćdziesiąt lat, nocą pilnuje kostnicy. Siedzi w kantorku przy chłodni z butelką wódki i radiem.
- **Kasia**, ośmioletnia dziewczynka po wycięciu migdałków, na laryngologii. Jej mama wyszła wieczorem do domu. Kasia boi się ciemności i płacze, kiedy się budzi (zob. *Nieświadomi hałasujący* w `Settings/TheStiffs/Setting.md`).

## Tajemnice

Tylko dla MG. Nie zdradzaj ich graczowi, dopóki postać ich nie odkryje.

- **Godzina zero.** O 1:00 w nocy z 21 na 22 marca zmarli wstają na całym świecie naraz (zob. *Noc z 21 na 22 marca 1990* w `Settings/TheStiffs/Poland.md`). Wstają wtedy wszystkie ciała z niezniszczonym mózgiem, w tym pięć w kostnicy. Każdy, kto umrze później, wstaje po czasie, który MG rozstrzyga rzutem (zob. *Powstawanie zmarłych* w `Settings/TheStiffs/Setting.md`).
- **Kostnica.** W chłodni leży pięć ciał. Dwa leżą od tygodnia i czekają na rodziny, które nie mogą ich odebrać, więc mimo chłodu zaczął się rozkład: wstaną jako wzdęci. Trzy są z wczoraj i dzisiaj i wstaną jako świeżaki, w tym mężczyzna po wypadku samochodowym i starsza kobieta z interny. O 1:00 wstają w zamkniętych szufladach i walą w drzwiczki. Pan Stefan, pijany, otwiera pierwszą szufladę, żeby sprawdzić, co się dzieje, i ginie. Kwadrans po pierwszej sam wstaje jako świeżak. Drzwi kostnicy na korytarz są zamknięte na zamek, więc świeżaki nie wyjdą tamtędy, ale winda towarowa stoi otwarta w piwnicy, a świeżak potrafi wejść do kabiny. Gdy ktoś wezwie windę z góry, przywiezie sobie sztywnych.
- **Pan Edward** umiera o 0:40, kilka minut po ostatnim namaszczeniu. Siostra Halina zakrywa go prześcieradłem i zostawia za parawanem do rana. Wstaje po czasie z rzutu liczonym od śmierci, ale nie wcześniej niż o godzinie zero (`gm.py timer --od 0:40 --nie-wczesniej 1:00`), w sali pełnej śpiących starych ludzi.
- **Sala intensywnej opieki.** Młody mężczyzna po wypadku motocyklowym umiera o 1:30 mimo reanimacji. Wstaje po czasie z rzutu, gdy lekarz i pielęgniarka wciąż stoją nad łóżkiem.
- **Karetki.** Od około 1:30 karetki i taksówki przywożą z Mokotowa, Czerniakowa i Sielc pogryzionych, „pijanych w szale”, rannych w bójkach i ich rodziny. Część umiera na izbie przyjęć i wstaje. Od 3:00 izba przyjęć jest pełna, a podjazd zastawiony.
- **Telefony.** Do 1:30 działają normalnie. Potem linie pogotowia i milicji są zajęte, a telefon miejski w portierni dzwoni bez przerwy: ludzie pytają, czy szpital przyjmie ich bliskich. Prąd, woda i ogrzewanie działają przez całą noc.
- **Pistolet milicjanta.** Kapral Nowicki strzela na izbie przyjęć około 2:00 do „pijanego, który rzucił się na lekarza”. Strzał w pierś niczego nie zmienia, a huk niesie się po całym gmachu. Jeśli nikt mu nie pomoże, Nowicki ginie najpóźniej o 2:30, a jego pistolet leży na podłodze izby przyjęć.
- **Siekiera strażacka** wisi w gablocie na drugim piętrze. Zbicie szybki to głośna czynność.
- **Podziemny korytarz** z piwnicy do pawilonu gospodarczego to najbezpieczniejsza droga na zewnątrz, bo omija izbę przyjęć i podjazd. Wiedzą o nim pani Zofia, pan Kazimierz, palacz i konserwator.
- **Nyska** w garażu pawilonu jest na chodzie i ma pół baku. Kluczyki wiszą w portierni. Brama na boczną ulicę jest zamknięta na kłódkę, a klucz jest w pęku pana Kazimierza.
- **Dolary Zdzicha** to około trzystu dolarów w skarpecie. Zdzichu zaoferuje je za pomoc w ucieczce, a gdy będzie miał okazję, zostawi postać w potrzebie.
- **Ambasada ZSRR** przy Belwederskiej jest niedaleko. Około 4:00 od strony skarpy słychać serie z karabinu maszynowego: to Rosjanie strzelają do każdego, kto zbliży się do ich ogrodzenia (zob. *Rosjanie* w `Settings/TheStiffs/Setting.md`).

## Przebieg nocy

MG śledzi czas od początku gry. Przejście przez jedno piętro korytarzem zajmuje kilka minut, przeszukanie sali albo gabinetu około kwadransa (zob. *Przeszukanie* w `Settings/TheStiffs/Setting.md`).

- **23:30, początek gry.** Zwykły nocny dyżur. Pracownik zaczyna w swoim miejscu pracy, pacjent budzi się w swojej sali, bo nie może spać. Za oknem wieje, w poczekalni izby przyjęć siedzi kilka osób. Psy w okolicy wyją dłużej niż zwykle.
- **0:00.** Kapral Nowicki przywozi na izbę przyjęć pobitego Zdzicha. Dr Kozłowski zszywa mu łuk brwiowy.
- **0:20.** Na internę przychodzi ksiądz Tadeusz do pana Edwarda.
- **0:30.** Kasia budzi się na laryngologii i płacze, bo w sali jest ciemno, a mamy nie ma. Płacz słychać na całym czwartym piętrze. Pielęgniarka z neurologii idzie ją uspokoić, a Kasia budzi się i płacze odtąd co godzinę.
- **0:40.** Pan Edward umiera. Siostra Halina zakrywa go prześcieradłem. MG rzuca, kiedy wstanie.
- **1:00, godzina zero.** W kostnicy pięć ciał wstaje w szufladach i wali w drzwiczki. Pan Stefan, pijany, otwiera jedną z nich. W mieście wstają zmarli w mieszkaniach, domach opieki i innych szpitalach.
- **1:15.** Pan Stefan wstaje jako świeżak. Kostnica jest pełna sztywnych, a winda towarowa stoi otwarta w piwnicy.
- **1:30.** Na sali intensywnej opieki umiera motocyklista. Przyjeżdża pierwsza karetka z pogryzionym starszym mężczyzną z Sielc: „sąsiadka go zaatakowała, chyba wścieklizna”. Telefony pogotowia i milicji stają się zajęte.
- **2:00.** Na izbie przyjęć jeden z przywiezionych umiera i wstaje. Kapral Nowicki strzela. Huk słychać w całym gmachu.
- **2:30.** Chaos na izbie przyjęć. Personel próbuje obezwładniać „agresywnych chorych”, a ludzie z poczekalni uciekają w głąb szpitala. Jeśli nikt mu nie pomógł, kapral Nowicki nie żyje.
- **3:00.** Izba przyjęć i parter należą do sztywnych. Kolejne karetki przyjeżdżają i ich załogi wchodzą prosto w tłum. Na internie i neurologii umierają pierwsi chorzy, którzy przestraszyli się albo zostali pogryzieni. Na każdym piętrze MG korzysta z tablicy spotkań dla późniejszego okresu (zob. *Spotkania* i *Miejsca zapalne* w `Settings/TheStiffs/Setting.md`).
- **4:00.** Od strony skarpy słychać serie z karabinu maszynowego. Na ulicach przed szpitalem są pierwsze porzucone samochody.
- **5:00.** Zaczyna szarzeć. Na piętrach zostali żywi, którzy się zabarykadowali, sztywni i ci, którzy jeszcze nie zdecydowali, gdzie są bezpieczniejsi.
- **5:35, świt.** Słońce wschodzi. Sztywnym to nie przeszkadza (zob. *Zmysły i zachowanie* w `Settings/TheStiffs/Stiffs.md`).
- **6:00.** Radio w portierni nadaje mgliste komunikaty o „zamieszkach i przypadkach agresji” (zob. *Co wiedzą ludzie* w `Settings/TheStiffs/Stiffs.md`).

MG nie musi trzymać się tych godzin co do minuty, ale nie przyspiesza godziny zero i nie zmienia jej. Wydarzenia, przy których postać nie była, toczą się dalej bez niej.

### Sztywni i hałas w kolejnych godzinach

Szpital rozkręca się stopniowo (zob. *Pierwsza noc w miejscu zapalnym* w `Settings/TheStiffs/Setting.md`). MG korzysta z tablic hałasu i spotkań tak:

| Godzina   | Gdzie                     | Tablica                            |
|-----------|---------------------------|------------------------------------|
| do 1:00   | cały szpital              | pierwsze 24 godziny, bez sztywnych |
| 1:00–2:30 | cały szpital              | pierwsze 24 godziny                |
| od 2:30   | parter, podjazd i piwnica | pierwszy miesiąc                   |
| od 3:00   | cały szpital              | pierwszy miesiąc                   |

Do 2:30 przychodzą tylko sztywni, którzy już wstali i mogą dojść:

- z kostnicy tylko windą towarową, gdy ktoś ją wezwie, bo drzwi na korytarz są zamknięte,
- pan Edward z interny od chwili powstania,
- motocyklista z sali intensywnej opieki od chwili powstania,
- zmarli z izby przyjęć od 2:00,
- każdy, kto zginął przy postaci albo w miejscu, przez które przeszła, od chwili powstania.

Jeśli rzut daje więcej sztywnych, niż może dojść, przychodzą ci, którzy mogą, a resztę zastępują przerażeni żywi: pacjenci, personel, ludzie z poczekalni.

## Haczyki

Każde piętro daje postaci powód, żeby nie uciekać od razu, i coś, czego potrzebuje. MG wprowadza je do gry, zanim postać opuści szpital, ale nie zmusza jej do niczego:

- **czwarte piętro:** płacz Kasi od 0:30 (zob. *Przebieg nocy*); pacjent z tego piętra słyszy ją, gdy tylko wyjdzie na korytarz,
- **trzecie piętro:** siostra Halina, która nie zostawi chorych, i pan Edward,
- **drugie piętro:** pacjenci na wyciągach, którzy nie mogą uciec i wołają o pomoc, oraz siekiera strażacka,
- **pierwsze piętro:** dr Kozłowski, sala intensywnej opieki i torba z lekami,
- **parter:** depozyt z ubraniem, butami i dokumentami pacjentów, telefon miejski w portierni, z którego można zadzwonić do bliskich, i kluczyki do nyski,
- **piwnica:** szatnie z ubraniami personelu, warsztat z narzędziami i tunel do pawilonu.

Pacjent zaczyna bez butów i ciepłego ubrania (zob. *Pacjent*), więc depozyt albo szatnie to jego naturalny cel.

## Przeciwnicy

Wszyscy sztywni tej nocy to świeżaki, poza dwoma wzdętymi z kostnicy (zob. *Sztywni w walce* w `Settings/TheStiffs/Setting.md`). Każdy był kimś: pan Edward w szpitalnej koszuli, motocyklista z bandażem na głowie, pan Stefan w fartuchu prosektoryjnego, staruszka z interny z obrączką na palcu, sanitariusz z karetki.

Pierwszej nocy nikt nie wie, z czym walczy. Personel i pacjenci biorą świeżaki za chorych w szale, pijanych albo „wściekłych”. Próbują ich trzymać, uspokajać i wiązać, i giną.

## Ekwipunek w szpitalu

To, co postać może znaleźć, MG rozstrzyga zasadami szabrowania (zob. *Szabrowanie* w `Settings/TheStiffs/Setting.md`), ale w szpitalu leży też dużo rzeczy na wierzchu:

- **broń improwizowana:** skalpele i nożyczki (krótkie pchnięcie), statyw do kroplówki i kij od szczotki (broń z zasięgiem, improwizowana), kule ortopedyczne, gaśnica, młotki i łom z warsztatu, siekiera do skrzyń z warsztatu i siekiera strażacka z gabloty,
- **leki i opatrunki:** w szafkach na oddziałach, w gabinecie zabiegowym i w aptece,
- **światło:** latarki w dyżurkach i portierni, świece w kaplicy przy kostnicy,
- **jedzenie:** w kuchni pawilonu gospodarczego, a na oddziałach tylko herbata, cukier i suchary,
- **ubrania:** w depozycie i w szatniach personelu.

Broń improwizowana utrudnia walkę o poziom (zob. *Broń* w `Rules/Equipment.md`).

## Propozycje tablic

**Zbicie szybki gabloty i zdjęcie siekiery.** Głośna czynność, bez rzutu, jeśli nikt nie przeszkadza. Potem MG rzuca na hałas.

**Uspokojenie Kasi**, gdy postać chce ją zabrać ze sobą (przeciętne, dla pielęgniarki łatwe, dla pacjenta, którego Kasia nie zna, trudne):

| Wynik | Rezultat                                                         |
|-------|------------------------------------------------------------------|
| 3–5   | Kasia wpada w panikę i krzyczy, MG rzuca na hałas                |
| 6–8   | Kasia idzie, ale popłakuje: skradanie z nią trudniejsze o poziom |
| 9–18  | Kasia ufa postaci i jest cicho                                   |

**Przekonanie dr. Kozłowskiego do ucieczki** (bardzo trudne do 2:30, potem trudne, a jeśli postać pokaże mu sztywnego, który wstał po śmierci, przeciętne): na niskich wynikach lekarz odmawia i wraca do chorych, na wysokich idzie z postacią i bierze torbę z lekami.

**Wezwanie windy towarowej z piwnicy po 1:15.** Postać nie wie, co stoi w kabinie. MG rzuca od razu:

| Wynik | Rezultat                                                |
|-------|---------------------------------------------------------|
| 3–6   | w kabinie są dwa świeżaki z kostnicy                    |
| 7–10  | w kabinie jest jeden świeżak                            |
| 11–18 | kabina jest pusta, ale na podłodze i ścianach jest krew |

## Zakończenia

Scenariusz kończy się, gdy postać opuści szpital, zabarykaduje się do rana w bezpiecznym miejscu albo zginie.

- **Ucieczka przed świtem.** Najbezpieczniej podziemnym korytarzem do pawilonu gospodarczego, a stamtąd nyską albo pieszo przez boczną bramę. Główne wejście i podjazd po 2:30 są pełne sztywnych. Postać wychodzi w miasto, w którym nikt jeszcze nie wie, co się dzieje.
- **Wczesna ucieczka.** Postać może wyjść główną bramą jeszcze przed 2:30, zanim podjazd się zapełni. To też jest zakończenie, ale ma swoją cenę: pacjent wychodzi bez ubrania, butów i dokumentów, nikogo nie ratuje i nie wie, co stało się z tymi, których zostawił. MG nie zatrzymuje postaci w szpitalu na siłę, ale przed jej wyjściem wprowadza do gry haczyki (zob. *Haczyki*).
- **Do rana na dachu albo w zamkniętej sali.** Postać przeżyła noc, ale szpital jest pełen sztywnych, a każde wyjście trzeba będzie wywalczyć albo wykraść.
- **Kogo postać wyprowadzi:** Kasię, dr. Kozłowskiego, siostrę Halinę, Ewę Lis, panią Zofię, Zdzicha. Każdy żywy towarzysz to pomoc i ciężar. Ci, których postać zostawi, zginą albo wstaną.
- **Śmierć.** Postać, która umrze w szpitalu, wstaje jak każdy (zob. *Powstawanie zmarłych* w `Settings/TheStiffs/Setting.md`).

Skutki, które mogą przejść do dalszej kampanii: towarzysze, którzy przeżyli, dolary Zdzicha, nyska, pistolet kaprala Nowickiego, wiedza, że zmarli wstają, i to, że Szpital Czerniakowski jest odtąd miejscem zapalnym na Dolnym Mokotowie.
