# Kampania 1: plan roboczy

Plan roboczy kampanii, czyli ciągu powiązanych scenariuszy w settingu Generia. Pisany po polsku; gotowe scenariusze trafią do `Scenarios/` po angielsku.

## Założenia

- **Kingsbridge jako centrum:** duże kampanie zaczynają się i kończą w Kingsbridge. Miasto leży w centrum kontynentu nieprzypadkowo.
- **Start:** postać na poziomie 0, początkujący śmiałek albo ktoś, kto jedzie do stolicy załatwić własne sprawy.
- **Tydzień świąteczny:** nowy rok (1 Tiriwen) i tydzień zabaw aż do pierwszego Lumiel (10 Tiriwen). Do Kingsbridge zjeżdżają się podróżni z całego królestwa, a nawet spoza niego: kupcy, magowie, awanturnicy. W stolicy można wtedy dostać praktycznie wszystko.
- **Dowolna postać:** kampanię da się zagrać dowolną postacią; scenariusze nie są pisane pod konkretnego bohatera.
- **Scenariusze niezależne:** każdy scenariusz stoi na własnych nogach i nie zależy od wątków poprzednich. MG może na własną rękę wpleść wątki z wcześniejszych przygód, zależnie od tego, jak się skończyły.

## Kalendarz otwarcia

| Data | Dzień | Księżyce | Co się dzieje |
|---|---|---|---|
| 29 Caerwen | Ithiel | | przedostatni dzień roku, przygoda 1 w gospodzie |
| 30 Caerwen | Lumiel | | ostatni dzień roku, przyjazd do Kingsbridge |
| 1 Tiriwen | Duriel | | nowy rok, równonoc wiosenna, początek zabaw |
| 5 Tiriwen | Nimel | podwójny nów | duże święto Noctary w środku tygodnia świątecznego |
| 10 Tiriwen | Lumiel | | koniec zabaw |
| 20 Tiriwen | Lumiel | podwójna pełnia | duże święto Solariusa, noc wilkołaków |

Pora roku: koniec zimy, odpowiednik połowy marca. W Caerwen śnieg zaczyna topnieć, drogi zamieniają się w błoto, a zapasy się kończą (przednówek). Z nowym rokiem przychodzi wiosna, a w Fenmarch powodzie.

## Scenariusze

| Nr | Rozmiar | Miejsce | Zarys |
|---|---|---|---|
| 1 | mikro | gospoda pół dnia drogi od Kingsbridge | postać jedzie do stolicy na tydzień świąteczny; przedostatni dzień roku |
| 2 | duży | Kingsbridge | tydzień świąteczny, napad na krasnoludzki bank, zawiązanie grubszej intrygi |
| 3 | średni | droga | „powieść drogi”: podróż do miejsca z przygody 4 |
| 4 | duży | cel podróży z przygody 3 | do ustalenia |
| dalej | | | zależy od konkretnych pomysłów; finał wielkiej kampanii znów w Kingsbridge |

PD przy pełnych sukcesach po czterech przygodach: 250 + (1000 lub 2000) + 1000 + 2000 = 4250–5250, czyli poziom 3, blisko 4 albo tuż za nim (poziom 4 od 5000).

## Przygoda 1: gospoda

Gotowy scenariusz: `Scenarios/TheStringOfSausages/` (mikro, poziom 0, 250 PD). Zatłoczona gospoda pół dnia drogi przed Kingsbridge, 29 Caerwen; w nocy w stodole bohater spotyka zbiegłego kłusownika Pansho. Jeśli bohater jedzie dalej po ciemku, przygoda się nie odbywa i gra przechodzi od razu do przygody 2.

Wątki, które mogą wrócić w Kingsbridge:

- Pansho: dłużnik bohatera albo wisielec, zależnie od wyboru; leśnik Osric Hale i jego dobre słowo.
- Goście gospody, wszyscy jadą na tydzień świąteczny: gnom Pell z broszką-krukiem, kuglarze Burrows, złodziej Wendel z pierścieniem niewidzialności (szukają go Saltmen z Port Seravel), łowca Aldous Crane, krasnoludy ze złotem dla bankierów, mag Ambrose Ashdown na zgromadzeniu w Arcane College.
- Sekret gospodarza Edrica: przemycane wino z Greenhollow.

## Przygoda 2: napad w karnawale

Szkic do korekty. Duży scenariusz, poziom 0–1, w Kingsbridge przez cały tydzień świąteczny (1–10 Tiriwen). W środku karnawału, w tłumie masek, zuchwały napad na największy krasnoludzki bank w mieście. Bohater wplątuje się przypadkiem, idzie tropem złodziei i odkrywa intrygę większą, niż się spodziewał.

### Oś: dwa szczyty

| Dni | Co się dzieje |
|---|---|
| noc 30 Caerwen / 1 Tiriwen | noc noworoczna: bohater podsłuchuje sąsiadów, o 3:00 włam do banku; pościg kanałami, jeśli bohater ruszy od razu |
| 1–2 Tiriwen | ranek po napadzie: miasto huczy, krasnoludy szukają winnych, trop łupu; pierwszy „loch” |
| 3–4 Tiriwen | śledztwo w mieście: gildia złodziei, bank, kryjówka bandy; złodzieje znalezieni martwi, czyli za nimi stoi ktoś większy |
| 5 Tiriwen | podwójny nów, pierwszy szczyt: rytuał kultu w lochu pod miastem; bohater go przerywa albo nie zdąży |
| 6–9 Tiriwen | pogoń za mocodawcą, który zaciera ślady; kult był tylko narzędziem |
| 10 Tiriwen | drugi szczyt: bal maskowy na zakończenie karnawału, demaskowanie mocodawcy dosłownie i w przenośni |

Najpierw akcja w lochu, potem intryga w towarzystwie. Kalendarz wydarzeń przez `gm.py`, jak w przygodzie 1: każdy dzień ma swoją atrakcję karnawału i ruch frakcji, który dzieje się bez względu na bohatera.

### Napad

- **Noc noworoczna:** w nocy z 30 Caerwen na 1 Tiriwen miasto świętuje do późna: dzwony o północy, ognie, iluzje Arcane College nad rzeką, pijani na ulicach. Hałas kryje ostatnie prace w przekopie, a o 3:00, kiedy zabawa przygasa i straż jest zmęczona, ekipa włamuje się do skarbca.
- **Dwie grupy:** ekipa podziemna przekopała się z kanałów pod skarbiec i robi włam. Trzech **odbiorców** czeka w karczmie bohatera na łup, przebranych za trupę karnawałową. Po włamie ekipa przynosi im szkatułę kanałami, a rano odbiorcy wynoszą ją w przebraniu, w maskach, w noworocznym pochodzie, i przekazują „panu w masce”. Złoto ekipa zabiera dla siebie.
- **Roztopy:** koniec zimy, kanały wzbierają. Woda to naturalny zegar i zagrożenie.

### Wplątanie bohatera: komórka za ścianą

Przygoda ma działać nawet wtedy, gdy gracz chce cały karnawał przesiedzieć w karczmie: przygoda przychodzi do niego.

- **Ostatni kąt w mieście:** Kingsbridge jest pełne, łóżek brak. Bohater dostaje ostatnie, co karczmarz ma: małą komórkę z prowizorycznym łóżkiem pod ścianą, w której normalnie nikt nie śpi.
- **Luźna deska:** w ścianie jest luźna deska, a za nią większy pokój trzech odbiorców. Bohater przychodzi do miasta 30 Caerwen, wieczorem świętuje albo kładzie się wcześnie, a w nocy budzą go szepty zza ściany.
- **Szepty:** odbiorcy nie śpią, czekają na łup i szepczą, zdenerwowani. Z rozmowy wynika dość, żeby działać: który bank, że ekipa wchodzi „o trzeciej, kiedy pijacy pójdą spać”, że przekop pod skarbiec jest gotowy, że wezmą złoto brodaczy, które właśnie przyszło, i że potem przyniosą „to” tutaj. Do tego strzępy, których bohater nie zrozumie: „szkatuła idzie do pana w masce”, „w pochodzie nikt nie zajrzy pod kukłę”. Bohater słyszy to wszystko bez rzutu: szepty napędzają całą fabułę, więc nie mogą zależeć od kości. Dokładna godzina włamu, około 3:00, to ukryty timer.
- **Mało czasu:** bohater słyszy szepty około 1:00–2:00, więc ma godzinę czy dwie. Karczma stoi niedaleko banku, a ulice są pełne pijanych i resztek zabawy.
- **Wybór bohatera:**
  - **Straż:** strażnica pełna noworocznych pijaków, sierżant nie wierzy obcemu z karczmy, przekonanie go to rzut. Patrol dociera do banku na czas albo za późno (zegar), w najlepszym razie na ogon ekipy, która ucieka do kanałów.
  - **Bank:** zamknięty na noc, krasnoludzcy strażnicy za kratą. Uwierzą szybciej, bo nie ufają nikomu, i zejdą do skarbca, może z bohaterem: walka z ekipą w przekopie i pościg kanałami, pierwszy „loch” od razu.
  - **Konfrontacja z sąsiadami:** trzech na jednego. To paserzy, nie zabijaki, ale uzbrojeni: walczą, przekupują albo uciekają przez okno. Włam i tak się odbywa, a ekipa, która przyniesie łup do pustego pokoju, zastaje tam bohatera.
  - **Sen:** świat toczy się bez bohatera. Ekipa przynosi szkatułę przed świtem, rano odbiorcy wychodzą w pochodzie, a miasto budzi się z wieścią o napadzie.
- **Deska działa w obie strony:** odbiorcy wzięli ten pokój, bo komórka za ścianą stała pusta i miała posłużyć za skrytkę. Karczmarz, wynajmując ją bohaterowi, pokrzyżował im plany.
- **Odbiorcy zauważają podsłuch:** skrzypnięcie deski, kaszel, światło przez szparę. Wtedy przychodzą do bohatera: grożą, przekupują albo proponują udział.
- **Udaremniony napad:** jeśli bohater ostrzeże bank albo straż na czas, włam się nie udaje. Bohater zyskuje uznanie, nagrodę i przyjaźń krasnoludów. Ale mocodawca ma plan B i relikt i tak trafia do kultu, więc wszystkie warianty schodzą się 3–4 Tiriwen na tropie reliktu. Propozycje planu B:
  - **Ostrzeżony bank przenosi relikt** w bezpieczniejsze miejsce, a mocodawca, który ma ucho w banku albo w straży, napada na ten transport. Ostrzeżenie bohatera nieświadomie pomaga kultowi.
  - **Ktoś w straży jest kupiony** i uprzedza ekipę, która zdąży wyjść ze szkatułą, ale bez złota. O donosiciela z komórki odbiorcy zaczynają pytać.
  - **Część ekipy wpada:** pojmany złodziej mówi tylko tyle, ile wie, a reszta ucieka ze szkatułą kanałami. Pościg w kanałach tak czy inaczej.
- **Dalsze haki, gdy gracz dalej siedzi:** Halvar Stonehelm przychodzi do karczmy, bo bohater widział skrzynię w gospodzie i mieszka obok bandy; nocą po relikt przychodzą Quiet Hands, a potem kultyści.
- **Bierny gracz:** jeśli bohater mimo wszystko nic nie robi, świat toczy się bez niego: rytuał 5 Tiriwen się udaje, mocodawca triumfuje 10 Tiriwen, a skutki wracają w kolejnych przygodach.

### „Lochy”

1. **Kanały i akwedukty Aurelionu:** pościg, przekop pod skarbiec, kryjówka bandy.
2. **Skarbiec banku:** oględziny po napadzie, krasnoludzkie zabezpieczenia i to, czego bankierzy nie chcą pokazać.
3. **Most Kingsbridge:** stary most z czasów Aurelionu, zabudowany domami, od którego miasto wzięło nazwę. Pościg po dachach, ukryte komory w filarach.
4. **Katakumby:** ossuarium Gravewardenów, a pod nim stara nekropolia Aurelionu z ukrytą świątynią Noctary. Finał 5 Tiriwen.
5. **Rezydencja mocodawcy w czasie balu:** loch towarzyski, czyli infiltracja, maski i straże.

### Pansho

Noworoczna łaska królewska: 1 Tiriwen, rano po napadzie, na rynku sądzi się skazańców. Tłum na placu żyje już wieścią o włamie, a odbiorcy idą z łupem w pochodzie obok szubienicy. Co bohater widzi, zależy od przygody 1:

- **oddany, poddanie zatajone:** Pansho wisi na rynku w chwili napadu;
- **oddany, Osric zgłosił poddanie:** król go ułaskawia, tłum wiwatuje, Osric Hale na placu kiwa bohaterowi głową;
- **puszczony albo bez wieści:** wisi jakiś rozbójnik; jeśli ukryty rzut kampanii mówi, że leśnicy złapali Pansho, to wisi on.

### Krasnoludy

Halvar i Kori Stonehelm zdeponowali skrzynię złota 30 Caerwen i napad ją zabiera. Klan odpowiada za depozyt, więc to sprawa honoru.

- Halvar zna bohatera z gospody, a bohater widział skrzynię: najpierw podejrzany, po wyjaśnieniu zleceniodawca („znajdź nasze złoto”).
- Dają dostęp do banku i do krasnoludzkich bankierów, którzy coś ukrywają.

### Goście z gospody w karnawale

Epizody: bohater może ich spotkać, ale nie grają ważnej roli w intrydze.

- **Pell Ambergear:** stragan z cudami na jarmarku. Broszka-kruk w tłumie kracze bez przerwy, więc Pell zawiesił na niej kartkę „nie działa”.
- **Kuglarze Burrows:** pokazy na placach, ich wielka kukła idzie w pochodzie noworocznym. Daisy wypatruje kogoś w tłumie i jest smutna.
- **Wendel:** rozpłynął się. O niziołka w meloniku z piórem pytają małomówni ludzie z portu (Saltmen); bohater może mignąć melonik w tłumie.
- **Ambrose Ashdown:** zgromadzenie w Arcane College. College pokazuje noworoczne iluzje nad rzeką, a Ambrose prowadzi publiczną dysputę o ruinach Aurelionu. Może rozpoznać relikt, ale nie jest śledczym.
- **Aldous Crane:** odbiera nagrodę za wilka w Adventurers' Guild i startuje w turnieju łuczniczym. Dobry świadek, może zauważyć ślady w kanałach.

### Intryga (propozycja)

- **Co skradziono:** złoto jest przykrywką. Prawdziwy cel to zastaw zubożałego rodu, aureliański relikt, np. zamknięta szkatuła z czarnego żelaza. Bank o nim milczy.
- **Złodzieje:** zawodowcy z zewnątrz, działający bez zgody Quiet Hands. Gildia złodziei Kingsbridge też ich ściga: groźna konkurencja albo niewygodny sojusznik. Po robocie mocodawca ich likwiduje.
- **Kult Noctary:** potrzebuje reliktu do rytuału w nekropolii w noc podwójnego nowiu 5 Tiriwen, np. żeby obudzić pogrzebanego tam aureliańskiego czarnoksiężnika. Maski karnawału kryją kultystów. Zalążek wątku Aurelionu na przygody 3–4.
- **Mocodawca:** szlachcic z dworu, który finansuje kult, bo widzi w nim drogę do władzy w walce o sukcesję. Zgodnie z zasadą kliszy wygląda na złoczyńcę. Książę i księżniczka są czyści, ale jego wpływy sięgają do jednego ze stronnictw.

## Otwarte pytania

- Przygoda 2: nazwa banku i klanu bankierów.
- Przygoda 2: co dokładnie budzi rytuał i co się dzieje, jeśli się uda?
- Przygoda 2: kim jest mocodawca i do którego stronnictwa sięga?
- Przygoda 2: co się dzieje między 6 a 9 Tiriwen?
- Przygoda 2: nazwa karczmy, gdzie stoi (na moście?) i kim jest karczmarz.
- Przygoda 2: który plan B mocodawcy wybrać, gdy bohater doniesie o napadzie (zob. *Wplątanie bohatera*)?
- Przygody 3–4: dokąd prowadzi droga?

## Notatki

