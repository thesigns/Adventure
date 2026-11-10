# Kaldara

Nordycka saga z domieszką baśni i grozy. Zimna, wulkaniczna wyspa wzorowana na Islandii: długie zimy, lodowce, gorące źródła, pola lawy. Ludzie rządzą się bez króla, sądzą się na tingu i mszczą przez pokolenia. W górach leżą ruiny zaginionego państwa krasnoludów, a w ruinach mieszkają trolle. Bogowie istnieją, ale odpowiadają rzadko i po swojemu.

O człowieku świadczy jego imię: co zrobił, komu dotrzymał słowa, kogo pomścił i co śpiewają o nim skaldowie. Śmiałek schodzi w ciemność po złoto i po pieśń, która go przetrwa. Najgroźniejsze są zima, ciemność i drugi człowiek.

## Pliki settingu

- `Setting.md`: przegląd świata, zasady dla MG, nazwy, zejścia, Wolna Wspólnota, życie na wyspie i frakcje (ten plik)
- `Geography.md`: wymiary wyspy, miasta i krainy
- `Travel.md`: miary drogi, tempo, trakt, podróże morskie, kontynent, spotkania w drodze, nocleg, ferd
- `Dwarves.md`: krasnoludy, co wiedzą o nich ludzie i prawda o ich upadku, której nie zna nikt na wyspie
- `Trolls.md`: trolle, główne zagrożenie wyspy: słońce, światło i ogień, walka i statystyki
- `Gods.md`: bogowie i ich kulty
- `Bestiary.md`: pozostałe istoty i ludzie, ze statystykami walki
- `Diseases.md`: choroby i ich mechanika: czarny kaszel, gorączka z rany, gnilec, ślepota śnieżna, czerwonka, zapalenie płuc
- `Magic.md`: magia, kapłani i wieszczki, zdolności nadprzyrodzone, klątwy i krasnoludzkie przedmioty z mocą
- `Economy.md`: gospodarka, waluta, czym się płaci, ceny, sprzedaż łupu, sakiewka na start
- `Mechanics.md`: profesje, zalety i wady, kalendarz, dzień i noc, światło, zimno, broń, pancerz, leczenie, przedmioty krasnoludzkie bez mocy i prawo
- `Maps/MapKaldara.svg`: mapa wyspy w skali 1 piksel = 500 m
- `Tables/Daylight.json`: wschody, zachody i ciemność z tabeli *Dzień i noc* w `Mechanics.md`, z których `Scripts/gm.py czas --setting Kaldara` wypisuje porę dnia
- `Tables/GmTables.json`: tablice ukrytych rzutów dla `Scripts/gm.py` i `Scripts/roll.py --ukryty` (zob. *Ferd* w `Travel.md` i `Diseases.md`)
- `Tools/`: narzędzia autora, nie do gry: generator mapy (`make_map.py`) i jego fonty

Mapa wyspy jest jawna: postać zna miasta, krainy, góry, lodowiec, główne rzeki i trakty. Gracz może oglądać ją w całości, a MG nie odsłania jej skryptem `Scripts/fogmap.py`. Na mapie nie ma ruin ani niczego, czego ludzie nie wiedzą. Mapy ruin mają scenariusze i te MG odsłania zwykłym trybem.

## Zasady dla MG

- Postać gracza to śmiałek, który chodzi na zejścia samotnie, bez stałych towarzyszy. Postacie MG towarzyszą jej tylko epizodycznie i nigdy nie decydują ani nie rozwiązują problemów za nią.
- Inni śmiałkowie mogą okazać się pomocą albo zagrożeniem. MG nie zdradza z góry, kim są i czego chcą.
- Ton jest poważny, a zagrożenia prawdziwe. Humor bywa suchy i oszczędny jak w sagach, ale gra nie jest komedią.
- MG opowiada jak saga: rzeczowo, czynami i słowami ludzi, a nie opisami uczuć. Ludzie mówią mało, a to, co mówią, waży. Cios pada bez zapowiedzi, a obelgę pamięta się latami.
- Nadprzyrodzone jest rzadkie: draugr, wieszczba czy runiczny miecz to wydarzenie, a nie codzienność.
- Czego nie ma w settingu ani w scenariuszu, MG uzupełnia w duchu sag i nordyckich podań, a nie fantasy z gier. Uzupełnia tylko świat, nie mechanikę: nie przenosi zasad ani pojęć z innych systemów RPG.
- Na wyspie żyją tylko ludzie. Nie ma elfów, krasnoludów ani innych ras grywalnych. Żywe krasnoludy nigdy nie pojawiają się w grze.
- Nikt nie potrafi odczytać krasnoludzkich run ani zrozumieć krasnoludzkiego języka, i żadna postać, księga ani zaklęcie tego nie zmienia.
- Gracz może znać cały setting, także prawdę o upadku krasnoludów z `Dwarves.md`, ale postać wie tylko to, co wiedzą ludzie na wyspie. Postacie MG wiedzą tylko to, co mogłyby wiedzieć.
- Nie ma króla, armii ani straży. Wyroki egzekwują poszkodowani, ich rody, wodzowie albo najemnicy.
- Dwa rodzaje scenariuszy. **Zejście:** samotna wyprawa do ruin, czyli droga, eksploracja, walka, łup, powrót. **Historia na powierzchni:** waśnie rodów, sprawy przed tingiem, banici, polowanie na potwora, intrygi wodzów, sprzedaż łupu.
- Nie ma jednej wielkiej fabuły. Scenariusze układają się w kampanię, a łup, sława, wrogowie i długi z jednych prowadzą do kolejnych.
- Wioski, osady i dwory wodzów (dziesiątki, wzdłuż wybrzeża i traktów) oraz ruiny krasnoludzkie (dziesiątki, najczęściej w górach i w głębi wyspy) MG tworzy według potrzeb scenariusza. Setting ich nie nazywa, a mapa ich nie pokazuje.
- Przygody dzieją się na wyspie. Kontynent jest w tle.
- Pora roku ma znaczenie: zimą wnętrze wyspy jest praktycznie nie do przebycia. Pora dnia też: za dnia zagrożeniem jest dzicz, nocą i pod ziemią trolle.

## Nazwy

Nazwy i imiona są ludzkie i brzmią nordycko: Sigrun, Ragnar, Hallvik, Grimsfjord. Nazwy miejsc są w `Geography.md`, imiona bogów w `Gods.md`, a nowe MG tworzy według tych zasad:

- **Pisownia:** tylko litery alfabetu angielskiego, bez znaków skandynawskich i polskich: Svartjokul, nie Svartjökull.
- **Bez prawdziwych bogów:** żadnych imion nordyckich bogów (Odyn, Thor, Freja, Loki i inni), także jako członów (Thorkel, Freydis).
- **Imiona** krótkie, zwykle dwusylabowe albo dwuczłonowe. Męskie często na -ar, -ulf, -mund, -bjorn, -geir, -vard, -stein, -kel (Ragnar, Asmund, Hallvard, Ulfgeir, Grimkel). Żeńskie na -run, -dis, -hild, -veig, -frid, -a (Sigrun, Asdis, Ragnhild, Bergljot, Halla).
- **Ojciec i przydomek:** „Ragnar, syn Ulfa”, „Sigrun, córka Halli”. Znani ludzie mają przydomki tłumaczone na język gry: Ragnar Siwobrody, Asdis Jednooka, Hallvard Bez Ziemi.
- **Rody** od założyciela albo od dworu: ród Asmunda, ludzie z Hallvik.
- **Nazwy miejsc:** człon opisowy i rodzajowy, np. Austhavn (wschodni port), Svartjokul (czarny lodowiec).
  - Rodzajowe: -vik (zatoka), -fjord (fiord), -havn (port), -nes (cypel), -strand (wybrzeże), -fjell (góra), -dal (dolina), -foss (wodospad), -myr (bagno), -jokul (lodowiec), -hraun (pole lawy), -lund (gaj), -vold (pole, równina), -stad (dwór), -borg (warownia), -heim (siedziba), -skard (przełęcz), -gap (rozpadlina), -hall (sala), -gard (zagroda, osada), -vaka (przerębel, oczko wody, które nie zamarza).
  - Opisowe: svart (czarny), hvit (biały), raud (czerwony), kald (zimny), brenn (palący), grim (ponury), stein (kamień), hof (świątynia), ting (zgromadzenie), ulf (wilk), ravn (kruk), bjarka (brzoza), dverg (krasnolud), troll (troll), aust, vest, nord, sud (strony świata).
- **Ruiny** mają nazwy nadane przez osadników: Dverghall (krasnoludzka sala), Ravnskard (krucza przełęcz). MG może podać ich znaczenie w języku gry.
- **Znane trolle** nazywa się od legowiska albo przezwiskiem w języku gry: troll spod Ravnskard, Czerwony Pysk.
- **Spójność:** każdą nową nazwę, która może wrócić w grze, MG zapisuje z krótką notatką w postępie scenariusza albo w dzienniku kampanii i sprawdza ją tam przed ponownym użyciem. Nie nadaje tej samej nazwy dwóm miejscom ani tego samego imienia dwóm ważnym postaciom. Epizodyczne postacie mogą pozostać bezimienne.

## Świat w skrócie

- **Wyspa:** duża, na północnym oceanie, tuż pod kręgiem polarnym. Kontynent leży daleko na wschodzie, a na zachodzie jest tylko ocean, z którego nie wrócił żaden statek. Geografia: `Geography.md`.
- **Krasnoludy:** ponad tysiąc lat temu rządziły wyspą. Ich państwo ludzie nazywają Dvergheim. Drążyły góry, kuły broń i budowały twierdze, a potem zniknęły. Teorie: erupcja, zaraza, wojna, ucieczka za morze. Najpopularniejsza mówi, że kopały za głęboko. Prawda: `Dwarves.md`.
- **Przybycie:** ok. 400 lat temu ludzie z kontynentu, wielu uciekających przed królami, zastali puste wybrzeża i ruiny pełne trolli. Najlepszą ziemię zajęli na zachodzie i tam wyrosły najstarsze rody. Późniejsi przybysze osiedli na wschodzie, przy morzu i handlu. Zamiast królestwa stworzyli Wolną Wspólnotę. Kontakt z kontynentem osłabł.
- **Cywilizacja:** miasta, wioski i dwory na wybrzeżu, połączone traktami i morzem. Wnętrze to dzicz: góry, lodowce, pola lawy, uśpione wulkany i ruiny.
- **Trolle:** główne zagrożenie, rozumne i okrutne istoty z Głębin. Słońce zamienia je w kamień. Opis: `Trolls.md`.
- **Pozostałe istoty:** draugry, mary, nykry, wilki, niedźwiedzie polarne, tursy na lodowcu, runiczni strażnicy w ruinach, a pod Brennfell śpi smok z sag. Opis: `Bestiary.md`.
- **Bogowie** istnieją i dają moc kapłanom. Najważniejsi to Solvar, bóg słońca i wróg trolli, oraz Eldra, bogini ognia i wulkanów. Opis: `Gods.md`.
- **Magia** jest rzadka, cicha i niepewna. Opis: `Magic.md`.
- **Ludzie:** tylko ludzie, potomkowie osadników. Przybysze zza morza zdarzają się rzadko, w Austhavn. Postać gracza jest człowiekiem z wyspy i ma profesję, a nie klasę (zob. *Profesje* w `Mechanics.md`).

## Zejścia

Samotna wyprawa do krasnoludzkich ruin po skarby. Chodzą na nie śmiałkowie: młodsi synowie bez spadku, zubożali gospodarze, wojownicy szukający sławy, banici.

- Nikt ich nie zleca i nikt za nie nie płaci. Śmiałkowie idą po złoto, krasnoludzkie przedmioty i sławę.
- Chodzi się samemu: w ruinach wspólnicy częściej zabijają się o złoto, niż giną od trolli. Kto bierze kogoś ze sobą, uchodzi za tchórza albo głupca.
- Łup należy do tego, kto go wyniósł. Nikt nie może się o niego upominać.
- W ruinach nie ma świadków. Co zdarzy się między śmiałkami pod ziemią, rzadko trafia przed sąd.
- W jednej ruinie bywa kilku śmiałków. Inny śmiałek może pomóc, podzielić się wiedzą, zawrzeć przymierze przeciw trollom albo wymienić zapasy. Może też śledzić, okraść, zastawić pułapkę albo zabić dla łupu. Często robi jedno i drugie.
- W ruinach leżą ciała śmiałków, którym się nie udało, z ekwipunkiem i tym, co zdążyli znaleźć.
- Złoto i klejnoty sprzedaje się w miastach, najlepiej w Austhavn (zob. `Economy.md`). Krasnoludzką broń i zbroje śmiałkowie często zatrzymują.
- Udane zejście daje sławę i pieśni skaldów. Bogaty śmiałek może kupić tytuł wodza. Niejeden ród zaczął od jednego zejścia, a stare rody patrzą na nowych bogaczy z pogardą i obawą.
- Większość zejść kończy się porażką albo śmiercią. Mówi się, że z pierwszego zejścia wraca jeden śmiałek na trzech.
- Zejścia odbywają się latem. Śmiałkowie zbierają się wiosną, najczęściej w Grimsfjord, i wracają przed zimą. Wiosną noce są jeszcze ciemne, więc już droga na zbiórkę bywa niebezpieczna.
- Wielki Ting wypada w środku pory zejść. Śmiałkowie jadą tam sprzedać łup, posłuchać pieśni o sobie albo stanąć przed sądem, ale każdy tydzień na Tingu to tydzień lata stracony dla ruin.

## Wolna Wspólnota

- **Wodzowie:** kilkudziesięciu najpotężniejszych ludzi wyspy. Tytuł wodza można odziedziczyć, kupić albo sprzedać, ale bez ludzi jest nic niewart. Wódz jest tak silny, jak jego majątek, rodzina, przyjaciele i stronnicy.
- **Stronnicy:** wolni gospodarze, którzy wybrali sobie wodza. Wódz broni ich interesów, a oni stają przy nim z bronią. Gospodarz może odejść do innego wodza, więc wodzowie konkurują hojnością i opieką.
- **Ćwierci:** Zachodnia, Północna, Wschodnia i Południowa. Każdej wiosny wodzowie ćwierci zbierają się na tingu i rozstrzygają miejscowe spory.
- **Wielki Ting:** raz w roku, w białe noce, na polu Tingvold, przez dwa tygodnie. Wodzowie stanowią prawo, sądy rozstrzygają sprawy, a reszta handluje, swata, pije, załatwia porachunki i słucha skaldów. Jedyny czas, kiedy cała wyspa jest w jednym miejscu.
- **Głosiciel Prawa:** wybierany przez wodzów na trzy lata. Zna prawo na pamięć i co roku recytuje je ze Skały Prawa. Najbardziej szanowany urząd, ale bez żadnej siły.
- **Wyroki** egzekwuje sam poszkodowany, jego ród albo wódz. Słabszy może odsprzedać roszczenie silniejszemu.
- **Kary:** najczęściej główszczyzna, czyli zapłata za krzywdę albo zabójstwo. Najsurowsza to wyjęcie spod prawa: banita traci wszystko, nikt nie może mu pomóc, a każdy może go zabić bezkarnie. Mechanika: *Prawo, waśń i dobre imię* w `Mechanics.md`.
- **Waśnie** między rodami ciągną się pokoleniami. Sądy próbują je kończyć, ale udaje się to tylko czasem.
- Kilka najbogatszych rodów skupuje coraz więcej tytułów wodzowskich. Starzy ludzie mówią, że tak zaczynają się królestwa.

## Klimat i życie na wyspie

- Zimno i wietrznie. Lato krótkie i chłodne, z białymi nocami. Zima długa, ciemna i śnieżna, z zorzami. W środku zimy dzień trwa kilka godzin (zob. *Dzień i noc* w `Mechanics.md`).
- Domy z kamienia i darni, w miastach także z drewna zza morza. Wiele budowli stoi na krasnoludzkich fundamentach albo jest z nich zbudowanych.
- Ogień w palenisku płonie przez całą zimę. Jego wygaśnięcie to bardzo zły znak.
- Gorące źródła są wszędzie: ludzie kąpią się w nich, gotują i ogrzewają domy. Przy źródłach stoją kapliczki Eldry.
- Wulkany śpią i od Przybycia żaden nie wybuchł. Ziemia czasem drży, z rozpadlin bije para, a w zagłębieniach zbierają się trujące opary. Ludzie wierzą, że pod górami śpi gniewna Eldra (zob. `Gods.md`).
- Lato to pora zejść. Zimą śmiałkowie siedzą w miastach i przepijają łupy.
- Białe noce chronią przed trollami. Długie zimowe noce to czas, kiedy trolle najczęściej podchodzą pod osady.
- Mieszkańcy są twardzi, małomówni i praktyczni. Cenią honor, hojność i dotrzymane słowo.
- **Gościnność** to obowiązek: wędrowca, który zapuka zimą, wpuszcza się do ognia i karmi, nawet wroga. Gość, który nadużyje gościny, i gospodarz, który skrzywdzi gościa, tracą dobre imię na zawsze.
- **Słowo** ma wagę. Przysięga na pierścień, broń albo przy ogniu wiąże cały ród. Obelga wymaga odpowiedzi, a zniesławiający wiersz skalda szkodzi bardziej niż miecz.
- **Los:** co komu przeznaczone, to go spotka. Liczy się tylko, jak człowiek go przyjmie i co zostanie po nim w pamięci ludzi.
- **Znaki:** sny, kruki, ptaki nad dworem, krew na księżycu, ogień przygasający bez powodu. Przed ważną decyzją pyta się wieszczkę albo rzuca losy.

## Frakcje

- **Paserzy z Austhavn:** sieć, a nie gildia: kupcy z rady miasta, zarządcy, właściciele składów, zbiry do wynajęcia. Skupują krasnoludzkie przedmioty bez pytań, wiedzą, kto wrócił z łupem, i nasyłają na niego ludzi. Przemycają banitów za morze. Mają ludzi w każdym mieście, ale nikt nie wie, kto nimi rządzi.
- **Dom Visara:** świątynia boga wiedzy w Austhavn. Kapłani, skaldowie i uczeni zbierają wiedzę o krasnoludach, przerysowują runy, spisują opowieści śmiałków i rysują mapy ruin. Kupują krasnoludzkie przedmioty i badają je kosztem zdrowia uczniów.
- **Zaprzysiężeni Solvara:** bractwo wojowników, którzy wyrzekli się ziemi i rodu. Mieszkają w warowni w Myrvace, a kilku przy świątyni w Hofvik. Tropią draugry, trolle i wiedźmy. To jedyna siła na wyspie podobna do wojska i nie słucha żadnego wodza, więc część wodzów patrzy na nią podejrzliwie.
- **Banici:** wyjęci spod prawa. Kryją się w Bjarkalund i przy głównych traktach, żyją z rabunku, kłusownictwa i kradzieży owiec. W głąb wyspy nie uciekają, bo nie ma tam co jeść, a nocą polują trolle. Niektórzy chodzą na zejścia, inni czyhają na wracających z nich śmiałków.
- **Rozbójnicy:** na głównych traktach i w Bjarkalund, tam, gdzie żaden wódz nie pilnuje dróg. Najchętniej napadają na zmęczonych i rannych śmiałków z łupem.
- **Morscy łupieżcy:** załogi łodzi ukrytych w zatoczkach Nordstrand i fiordów wschodu. Napadają na wioski wielorybników, statki kupieckie i odcięte gospodarstwa. Łatwo ich wynająć i łatwo im się narazić.
- **Wiedźmy:** wieszczki, które odeszły od Ylvy i zdziczały. Moc czerpią z bagien i z umarłych w kurhanach, mieszkają na odludziu, najczęściej na bagnach. Rzucają klątwy, warzą trucizny i budzą draugry. Ludzie boją się ich, ale czasem po cichu proszą je o pomoc. Czary: *Klątwy i czary wrogów* w `Magic.md`.
