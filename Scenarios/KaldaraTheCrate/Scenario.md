# Skrzynia

Setting: Kaldara

Mikro scenariusz dla jednej postaci na zerowym poziomie doświadczenia, na mniej więcej godzinę gry. Pełny sukces daje 250 punktów doświadczenia (zob. `ExperienceRewards.md`).

Austhavn, początek kwietnia 403 roku po Przybyciu. Postać czeka w mieście na ferd do Grimsfjord, gdzie zbierają się śmiałkowie przed porą zejść. Po południu mija na ulicy wóz ze skrzynią obitą grubym samodziałem, w której coś się tłucze. Dwaj chłopi spod Ulflund złapali żywego pomiota i chcą go sprzedać. Wieczorem pokazują go gościom gospody po łokciu za spojrzenie, a pomiot wyrywa się i ucieka w ciemne miasto. Do świtu zostaje siedem godzin. Kto znajdzie go pierwszy i co z nim zrobi?

Scenariusz jest pierwszą częścią kampanii. Drugą będzie podróż ferdem z Austhavn do Grimsfjord (zob. *Co dalej*).

## Świat

Wszystko, co MG musi wiedzieć o Austhavn, trollach i pieniądzach, jest w settingu: `Settings/Kaldara/Geography.md` (*Austhavn*), `Settings/Kaldara/Trolls.md` (zwłaszcza *Pomioty*, *Ślady trolli*, *Głód*, *Słońce i trolle*, *Światło razi trolle*, *Trolle i ogień*) i `Settings/Kaldara/Economy.md`.

### Czas i światło

Gra toczy się 5 kwietnia 403 roku. Słońce wschodzi około 5:00, a zachodzi około 19:00. **Ciemność**, w której troll może przeżyć pod gołym niebem, trwa od około 20:25 do 3:35 (zob. *Dzień i noc* w `Settings/Kaldara/Mechanics.md`). O 3:35 zaczyna się brzask, a pomiot, który znajdzie się wtedy pod gołym niebem, kamienieje w ciągu jednej rundy.

Postać wie z opowieści, że słońce zamienia trolle w kamień, i widzi, kiedy niebo zaczyna jaśnieć. Dokładnej godziny nie zna, bo ludzie nie liczą godzin (zob. *Miary* w `Settings/Kaldara/Mechanics.md`).

Na ulicach Austhavn nocą jest ciemno. Bez światła działania wymagające wzroku są trudniejsze o poziom, a w piwnicy i pod podłogą o dwa. Pochodnia pali się około godziny, łuczywo kwadrans, kaganek z tranem około czterech godzin.

MG ustawia setting kampanii przy pierwszym wywołaniu zegara (`--setting Kaldara`, zob. *Upływ czasu*), a `Scripts/gm.py czas` wypisuje odtąd porę dnia.

### Przypływ i odpływ

Kanał odpływowy pod nabrzeżem da się przejść tylko przy odpływie (zob. *Stary skład Asmunda*). Tej nocy:

| Godzina     | Morze                      | Wylot kanału                                                 |
|-------------|----------------------------|--------------------------------------------------------------|
| ok. 15:00   | przypływ                   | pod wodą                                                     |
| 19:30–22:00 | odpływ (dno ok. 21:15)     | odsłonięty, da się przecisnąć z plaży                        |
| 22:00–23:00 | woda wraca                 | zalany do połowy; pomiot by się przecisnął, człowiek już nie |
| 23:00–7:30  | przypływ (szczyt ok. 3:30) | pod wodą, nikt nim nie przejdzie                             |
| od ok. 7:30 | odpływ (dno ok. 9:40)      | odsłonięty, ale jest dzień i pomiot nie wyjdzie              |

Następnej nocy, 6 kwietnia, odpływ przypada o około 40 minut później, więc wylot jest odsłonięty mniej więcej od 20:10 do 22:40. Wtedy pomiot, którego nikt nie znalazł, wymyka się kanałem z miasta (zob. *Tajemnice*).

### Pogoda

Noc jest pogodna i wietrzna, a wiatr od fiordu zimny, ale nie ma mrozu. Mokre ubranie nie utrudnia więc działań (zob. *Zimno* w `Settings/Kaldara/Mechanics.md`). Postać, która przejdzie kanałem, jest jednak przemoczona do pasa i trzęsie się z zimna. Jeśli zamiast się wysuszyć spędzi noc pod gołym niebem, MG rozstrzyga ją tablicą z *Zimno* na poziomie przeciętnym.

### Ceny w Austhavn

Postać płaci siekańcami srebra (zob. `Settings/Kaldara/Economy.md`):

| Towar albo usługa                      | Cena       |
|----------------------------------------|------------|
| nocleg z wieczerzą w Wielorybiej Kości | 1 łokieć   |
| dzban piwa                             | pół łokcia |
| pięć pochodni albo dziesięć łuczyw     | 1 łokieć   |
| suszony dorsz albo kawał baraniny      | pół łokcia |
| worek albo kawał sieci rybackiej       | 1 łokieć   |
| lina z foczej skóry, 20 m              | 3 łokcie   |
| spojrzenie na trolla w skrzyni         | 1 łokieć   |
| żywy pomiot (cena braci)               | 5 uncji    |

## Postać gracza

Postać tworzy się według zasad podstawowych i settingu (zob. *Postacie* w `Settings/Kaldara/Mechanics.md`). Może mieć dowolną profesję, ale na zerowym poziomie zwykle nie ma przy sobie więcej niż kilka uncji srebra, więc trolla nie kupi.

Postać przyjechała do Austhavn, żeby z ferdem ruszyć na północ do Grimsfjord. Ferd zbiera się w Wielorybiej Kości i wyrusza za trzy dni. Do tego czasu postać nocuje w gospodzie. Gracz może dopisać, skąd postać przybyła i po co jedzie na północ, ale typowy powód to zbiórka śmiałków przed pierwszym zejściem.

## Miejsca

Austhavn to największe miasto wyspy: drewniane i kamienne domy wokół długiego fiordu, nabrzeża, składy, suszarnie ryb, świątynie i rynek nad portem. Wiele domów stoi na fundamentach krasnoludzkich (zob. *Klimat i życie na wyspie* w `Settings/Kaldara/Setting.md`). Scenariusz dzieje się w czterech miejscach dzielnicy portowej, kilka minut drogi jedno od drugiego.

### 1. Wielorybia Kość

Gospoda przy porcie, w której nocuje postać i zbiera się ferd. Nad bramą wisi żebro wieloryba. Duża izba z paleniskiem, piwo, ryba, baranina, marynarze, kupcy i kilku śmiałków czekających na ferd. Za izbą jest podwórze z klepiskiem, stajnią i bramą na zaułek, który prowadzi w dół do nabrzeży.

Gospodę prowadzi **karczmarz**, gruby, łysy, wiecznie spocony mężczyzna, który boi się tylko tego, że ktoś mu zniszczy gospodę. Na imię ma Svein, a ludzie mówią na niego Svein Gruby.

### 2. Suszarnie ryb i nabrzeże

Długie drewniane rusztowania, na których wiszą rzędami dorsze, a pod nimi skrzynie, beczki z tranem, sieci i łodzie wyciągnięte na kamienie. Nocą nikt tu nie pilnuje, tylko psy przy składach. Woda chlupocze o pale, wszystko cuchnie rybą i tranem. Dalej ciągnie się kamienne nabrzeże, tak stare, że ludzie mówią, że zbudowały je krasnoludy.

### 3. Stary skład Asmunda

Skład tranu na samym końcu nabrzeża, drewniana szopa na kamiennej, krasnoludzkiej podmurówce. Kupiec Asmund wyjechał na wieś, a drzwi są zaryglowane od zewnątrz. W środku stoją beczki z tranem i zwoje lin, a w podłodze jest klapa do piwnicy. Piwnica to dawne krasnoludzkie sklepienie: niska, kamienna, z zatartymi runami na ścianach, zawsze ciemna, wilgotna i zimna. Od strony morza wychodzi z niej stary krasnoludzki kanał odpływowy, przez który przy odpływie można się przecisnąć z plaży pod nabrzeżem.

### 4. Rynek

Plac nad portem, z kamienną studnią pośrodku i świątynią Solvara po jednej stronie. Za dnia targ, nocą pusty, poza świątynią, w której zawsze płonie ogień. Stąd o świcie widać cały port.

## Postacie MG

- **Ketil i Orm**, bracia, synowie Grima, gospodarze spod Ulflund. Ketil jest starszy, chudy i chytry, liczy srebro na palcach. Orm jest młodszy, rosły i porywczy, lubi się popisywać. Pomiota złapali w wilczy dół i chcą na nim zarobić, ile się da. Nie są źli, tylko chciwi i głupi. Jeśli pomiot ucieknie, chcą go z powrotem żywego, bo martwy jest nic niewart, i za żywego obiecują uncję srebra.
  - **Co mówią.** Orm chętnie opowiada, jak złapali pomiota w wilczy dół i że od trzech tygodni go nie karmią, bo boją się otworzyć skrzynię. O ofercie Domu Visara wygada się tylko komuś, kogo polubi, np. temu, kto z nim pije albo podziwia jego zdobycz. Ketil podaje tylko cenę, pięć uncji, i nie mówi nic o kupcach.
  - **Po nocy.** Jeśli postać wyda pomiota komuś innemu albo go zabije, bracia mają do niej żal i to zapamiętają, ale nie sięgają po broń: przeciw ludziom Ragny i całemu miastu nie mają szans.
- **Ragna**, kapłanka Solvara ze świątyni przy rynku, kobieta w średnim wieku, surowa i nieustraszona. Dla niej troll to wróg Solvara, a nie towar. Gdy dowie się o ucieczce, zbiera ludzi z pochodniami i szuka pomiota, żeby o świcie oddać go słońcu. Nie da się jej przekupić, ale da się ją przekonać, zwłaszcza przysięgą przed Solvarem.
- **Pomiot**, który nie ma imienia, które ludzie umieliby wymówić. Troll wielkości dziecka, chudy, sinoszary, z wielkimi uszami (zob. *Pomioty* w `Settings/Kaldara/Trolls.md`). Od trzech tygodni siedzi w skrzyni, wygłodzony, przerażony i zły. Lewa dłoń skamieniała mu od promienia słońca, który wpadł przez szparę między deskami. Porozumiewa się na migi, a mięso jest dla niego cenniejsze niż cokolwiek innego.
  - **Czego chce.** Przeczekać dzień w ciemności i następnej nocy wrócić do swojego stada w Ulflund (zob. *Tajemnice*). Kto go nakarmi, temu przestaje być wrogiem i próbuje mu to pokazać: wskazuje w górę, na niebo, i zasłania oczy (słońce), pokazuje kamienną dłoń (co mu zrobiło słońce), a potem wskazuje na zachód, w stronę lasu, i robi gest biegu. Nie rozumie słów, ale rozumie gest, groźbę i jedzenie.

Karczmarz, goście gospody, ludzie Ragny, rybacy i stróże składów są tłem. MG nadaje imiona tylko tym, o które gracz zapyta.

## Tajemnice

Tylko dla MG. Nie zdradzaj ich graczowi, dopóki postać ich nie odkryje.

- **Skąd pomiot.** Trzy tygodnie temu bracia zastawili wilczy dół z przynętą z baraniny na skraju Ulflund. Głodny pomiot oderwał się od swojego stada i wpadł do dołu. Bracia przykryli dół skórami, przeczekali w nim do zmroku, wsadzili pomiota w worku do skrzyni i zabili ją gwoździami. Od tamtej pory nie dali mu jeść, bo bali się otworzyć skrzynię.
- **Kupiec.** Bracia byli rano w Domu Visara, gdzie uczeni zaoferowali im dwie uncje. Ketil chce pięć, więc wieczorem urządza pokaz w Wielorybiej Kości, żeby zarobić na spojrzeniach i znaleźć lepszego kupca, np. kupca zza morza, który zbiera dziwy.
- **Nadgryziona deska.** Przez trzy tygodnie pomiot przegryzał od środka narożnik skrzyni. Za dnia nie odważył się wyjść, bo czuł słońce przez sukno. Deska trzyma się już tylko na jednym gwoździu.
- **Ucieczka.** Podczas pokazu Orm podważa wieko, a pijany marynarz podsuwa pochodnię pod samą skrzynię. Światło razi pomiota, ten szarpie się, nadgryziona deska pęka i pomiot wyskakuje przez dziurę. Gryzie Orma w rękę (lekka rana), przemyka między nogami gości i ucieka przez bramę w zaułek, w stronę portu.
- **Droga pomiota.** Najpierw głód: biegnie do suszarni ryb, zrywa i zjada dorsze. Potem szuka ciemnego miejsca na dzień, bo czuje, że do świtu nie zdąży wrócić do Ulflund. Wybiera skład Asmunda, do którego wchodzi kanałem odpływowym od plaży, i chowa się w krasnoludzkiej piwnicy, gdzie światło nigdy nie dociera. Tam zostaje do następnej nocy, jeśli nikt go nie znajdzie, i wymyka się kanałem przy najbliższym odpływie po zmroku (zob. *Przypływ i odpływ*).
- **Tłum Ragny.** Ragna zbiera ludzi w ciągu pół godziny po ucieczce i przeszukuje miasto od rynku w dół, ulica po ulicy, z pochodniami. Na skład Asmunda trafia przed samym świtem, o godzinie z ukrytego rzutu (zob. *Upływ czasu*). Ludzie Ragny wykurzają pomiota z piwnicy dymem z płonących szmat. Pomiot ucieka przez skład i nabrzeże w górę na rynek, szukając ciemności, i tam łapie go brzask. Rano na rynku stoi kamienny posąg pomiota, a wokół niego tłum gapiów.
- **Stado.** Stado, od którego oderwał się pomiot, wciąż żyje w Ulflund, przy trakcie na północ. To ważne w drugim scenariuszu (zob. *Co dalej*).

## Upływ czasu

MG śledzi godzinę od początku gry. Przejście między miejscami zajmuje kilka minut, wypytanie ludzi albo przeszukanie miejsca około kwadransa do pół godziny.

- **Około 16:00, początek gry.** MG ustawia zegar świata i setting kampanii:

  ```
  python Scripts/gm.py --kampania <kampania> czas --data 0403-04-05 --teraz 16:00 --setting Kaldara
  ```

  Jeśli zegar świata w kampanii jest już ustawiony, MG pomija `--data`, a jeśli setting jest już zapamiętany, także `--setting`. Postać idzie ulicą przy porcie. Mija ją wóz ze skrzynią obitą grubym samodziałem, w której coś się tłucze i drapie. Na koźle siedzą Ketil i Orm. Gdy postać się zainteresuje, Orm z dumą mówi, że to żywy troll, a Ketil, że sprzedadzą go za pięć uncji srebra. Skrzyni za dnia nie otworzą („Chcesz go zabić? Słońce zrobi z niego kamień!”), ale zapraszają na pokaz wieczorem w Wielorybiej Kości, po łokciu za spojrzenie.
- **Wieczór.** Wieść o pokazie roznosi się po porcie. W gospodzie jest tłoczno i głośno, a skrzynia stoi w stajni na podwórzu.
- **Około 20:30, pokaz.** Zaraz po zapadnięciu ciemności bracia wynoszą skrzynię na podwórze, a goście płacą i ustawiają się w kolejce. Około 20:45 dochodzi do ucieczki (zob. *Tajemnice*). Jeśli postać jest na podwórzu, może spróbować zatrzymać pomiota (zob. *Propozycje tablic*). Jeśli nie jest, słyszy krzyki, łoskot i wycie Orma.
- **20:45.** Gdy pomiot ucieknie, MG ustawia ukryty czas, w którym tłum Ragny trafi na skład Asmunda:

  ```
  python Scripts/gm.py --kampania <kampania> czas --teraz 20:45
  python Scripts/gm.py --kampania <kampania> timer --etykieta n1 --tablica tc1 --od 20:45 --opis tłum
  ```

  Przy każdym przesunięciu czasu MG wywołuje `czas --teraz`, a skrypt powie mu, kiedy tłum dotrze do składu.
- **Około 21:00.** Ketil obiecuje uncję srebra temu, kto przyprowadzi pomiota żywego. Pół godziny później w porcie pojawiają się Ragna i kilkunastu ludzi z pochodniami. Zaczynają od rynku i schodzą ulica po ulicy w stronę nabrzeży.
- **Między 21:00 a 22:00.** Pomiot obżera się w suszarniach ryb, a potem przemyka nabrzeżem do składu Asmunda. Jeśli postać idzie tropem szybciej, zob. *Postać dogania pomiota*.
- **Od około 22:00.** Pomiot siedzi w piwnicy składu, najedzony, ale wciąż wygłodzony po trzech tygodniach.
- **Godzina z ukrytego rzutu, przed świtem.** Ludzie Ragny docierają do składu Asmunda. Jeśli pomiot wciąż tam jest, wykurzają go dymem i o brzasku pomiot kamienieje na rynku (zob. *Tajemnice*). Jeśli postać jest wtedy w składzie, ludzie Ragny zastają ją przy pomiocie.
- **3:35, brzask.** Każdy troll pod gołym niebem kamienieje.

Ludzie Ragny przeszukują miasto po kolei, więc postać, która zgubi ich trop albo pośle ich w złą stronę, opóźnia ich. MG może wtedy usunąć zdarzenie (`gm.py usun --etykieta n1`) i ustawić nowe z późniejszą godziną `--od`. Jeśli postać sama zaprowadzi ich do składu, docierają tam razem z nią, a dalej zob. *Ragna zna kryjówkę*.

## Trop

Postać, która chce znaleźć pomiota, może iść jego śladami (zob. *Ślady trolli* w `Settings/Kaldara/Trolls.md`) albo pytać ludzi. MG opisuje ślady jak każdy szczegół miejsca, bez wskazywania, co z nich wynika.

- **Zaułek za bramą gospody:** mokre odciski małych, płaskich stóp w błocie, prowadzące w dół, ku portowi. Na kamieniu ślad krwi Orma.
- **Suszarnie ryb:** zerwane i przegryzione sznury, na ziemi ogryzione do ości dorsze, rozsypane łuski. Psy przy składach ujadają w stronę nabrzeża, a szczury zniknęły. Stary rybak, który nocuje w swojej łodzi, widział „dziecko, które biegło na czworakach” w stronę końca nabrzeża.
- **Nabrzeże:** na mokrych kamieniach rybie łuski i ślady prowadzące do schodków na plażę pod nabrzeżem. Przy odpływie widać pod nabrzeżem kamienny wylot krasnoludzkiego kanału, a w szlamie przed nim świeże odciski.
- **Skład Asmunda:** drzwi zaryglowane od zewnątrz, więc pomiot nie wszedł drzwiami. Ze szpar w podłodze czuć słaby smród. Kto przyłoży ucho do klapy, usłyszy chrobot i mlaskanie.

Kto zamiast śladów pyta ludzi, trafia do tych samych miejsc wolniej, bo w nocy mało kto jest na nogach, ale łatwiej: stróż przy składach, rybak w łodzi i marynarz wracający z gospody coś widzieli albo słyszeli.

### Postać dogania pomiota

Łowca albo postać, która od razu ruszy tropem z pochodnią, może dojść do suszarni około 21:00, gdy pomiot wciąż tam je. Pomiot widzi światło z daleka. Postać zobaczy tylko szary kształt, który znika między rusztowaniami, i ości jeszcze mokre od śliny, a pomiot ucieka nabrzeżem prosto do kanału i do piwnicy. Trop prowadzi dalej jak zwykle, a pomiot jest w piwnicy kilkanaście minut przed postacią, najedzony tylko trochę.

Postać, która skrada się bez światła, może podejść do jedzącego pomiota. Skradanie w ciemności między rusztowaniami jest trudne, a pomiot jest zajęty jedzeniem, więc przeciętne. Jeśli się uda, postać zaskakuje go na otwartym terenie: ma przez pierwszą rundę przewagę zaskoczenia (zob. *Trudność walki* w `Rules/Combat.md`), ale walczy po ciemku, a pomiot, który nie jest tu osaczony, ucieka po pierwszej ranie albo przy pierwszej okazji, nabrzeżem do kanału. Złapanie go siecią albo workiem rozstrzyga tablica *Pojmanie pomiota żywcem* z ciemnością.

Postać może iść do składu przez drzwi, jeśli zdejmie rygiel, co jest głośne, ale bez rzutu, albo kanałem od plaży: ciasno, ciemno, po kolana w zimnej wodzie, z pochodnią, która może zgasnąć.

## Pomiot w piwnicy

Pomiot to słaby przeciwnik o wątłej wytrzymałości (zob. *Pomioty* w `Settings/Kaldara/Trolls.md`). Tej nocy ma trzy okoliczności:

- **Ciasnota:** piwnica jest niska, więc dorosły człowiek walczy w niej pochylony, a pomiot jest w swoim żywiole. Walka jest trudniejsza o poziom.
- **Światło:** pochodnia albo kaganek razi pomiota z bliska, więc walka jest łatwiejsza o poziom (zob. *Światło razi trolle* w `Settings/Kaldara/Trolls.md`).
- **Głód i osaczenie:** pomiot nie cofa się przed ogniem, bo jest wygłodzony i nie ma dokąd uciec, poza kanałem za plecami postaci, jeśli ta weszła kanałem (zob. *Trolle i ogień* w `Settings/Kaldara/Trolls.md`).

Ciasnota i światło się znoszą, więc walka z pomiotem jest łatwa, jak z każdym słabym przeciwnikiem: próg trafienia 6, zakres rany 3–4. Pomiot gryzie i drapie, od draśnięcia do lekkiej rany. Postać, która wejdzie bez światła, walczy o dwa poziomy trudniej i nie widzi, co ją gryzie.

Pomiot zrozumie gest, groźbę i jedzenie. Na widok mięsa albo ryby przestaje warczeć i patrzy. Kto rzuci mu jedzenie, kupi od niego czas i spokój (zob. *Głód* w `Settings/Kaldara/Trolls.md`).

## Co postać może zrobić

Każde rozwiązanie jest w porządku i każde ma swoją cenę. MG nie podpowiada żadnego.

- **Zabić pomiota** w piwnicy albo wcześniej. Łatwo, ale Ketil nic za niego nie zapłaci, a Ragna pochwali postać przy rynku.
- **Złapać go żywego**, np. w worek albo sieć, i oddać braciom za uncję. Trzeba go jeszcze przenieść przez miasto, w którym szukają go ludzie Ragny, a ci chcą go spalić albo oddać słońcu.
- **Wystawić go na świt**, np. wywlec na nabrzeże przed brzaskiem. Pomiot ginie bez walki, a Ragna uznaje to za dzieło Solvara.
- **Ukryć go**, np. zostawić w piwnicy, zamknąć klapę i odwieść ludzi Ragny od składu. Następnej nocy pomiot sam wymyka się kanałem z miasta i wraca do Ulflund. Postać nic na tym nie zarabia i ryzykuje, że bracia albo Ragna się dowiedzą.
- **Wydać go ludziom Ragny**, np. zaprowadzić ich do kryjówki albo zatrzymać pomiota w piwnicy, dopóki nie przyjdą. Ragna oddaje go słońcu, a postać nic nie zarabia poza dobrym imieniem i gościną świątyni (zob. *Ragna zna kryjówkę*). Bracia mają do niej żal.
- **Przekonać Ragnę**, że pomiota należy zostawić przy życiu albo oddać braciom. To bardzo trudne, chyba że postać ma mocny argument, np. przysięgę przed Solvarem, że wyprowadzi trolla z miasta.

Jeśli postać nic nie zrobi albo nie zdąży, ludzie Ragny wykurzają pomiota, a brzask zrobi z niego posąg na rynku.

## Ragna zna kryjówkę

Gdy Ragna dowie się, gdzie jest pomiot, zanim jej ludzie sami trafią na skład, np. od postaci, nie wchodzi za nim w ciemność. Pomiot w krasnoludzkiej piwnicy jest bezpieczny przed słońcem, a pchanie się do niego z widłami w ciasnocie to głupia śmierć. Ragna chce tylko, żeby nie uciekł przed świtem:

- przy wylocie kanału każe palić ogień i stawia dwóch ludzi, choć w nocy przypływ i tak go zamyka (zob. *Przypływ i odpływ*),
- zdejmuje rygiel ze składu, a przy klapie stawia trzech ludzi z ogniem, którzy zmieniają się do rana,
- gdy zacznie szarzeć, każe otworzyć klapę i wykurzyć pomiota dymem z płonących szmat. Pomiot wybiega przez skład na nabrzeże, w światło brzasku, i kamienieje po kilku krokach.

Pomiot nie przejdzie obok płonącej pochodni w ciasnym wylocie kanału, dopóki ma ciemną kryjówkę: głód przełamuje jego strach przed ogniem dopiero wtedy, gdy nie ma dokąd uciec. Postać, która wcześniej zostawiła ogień przy kanale, zamknęła mu więc tę drogę.

Ragna nie płaci za trolle, bo to nie towar. Postaci, która go znalazła, daje to, co ma:

- **dobre imię:** rano na rynku mówi przy ludziach, kto znalazł trolla, a w Austhavn to wiele znaczy (zob. *Prawo, waśń i dobre imię* w `Settings/Kaldara/Mechanics.md`),
- **gościnę świątyni:** ogień, koc, wieczerzę i posłanie przy palenisku tej nocy i każdej następnej aż do odjazdu ferdu, bez zapłaty. Noc w świątyni jest porządnym wypoczynkiem,
- **przychylność:** postać może później prosić Ragnę o radę albo o modlitwę nad rannym bez ofiary (zob. *Zdrowie i leczenie* w `Settings/Kaldara/Mechanics.md`).

## Propozycje tablic

**Zatrzymanie pomiota na podwórzu**, gdy postać stoi w kręgu pokazu i rzuca się na niego (bardzo trudne: ciemność poza kręgiem pochodni, tłok, pomiot jest mały i zwinny). Wszystko dzieje się w mgnieniu oka, ale gracz decyduje, czy postać się rzuca, więc MG pokazuje tablicę przed rzutem:

| Wynik | Rezultat                                                          |
|-------|-------------------------------------------------------------------|
| 3–4   | pomiot gryzie postać w rękę (lekka rana) i ucieka                 |
| 5–12  | pomiot wyślizguje się postaci i znika w zaułku                    |
| 13–18 | postać przygniata pomiota do ziemi i trzyma go, a ten szarpie się |

**Trop w porcie**, gdy postać idzie śladami (przeciętne z pochodnią, trudne bez światła, łatwe dla łowcy i postaci z zaletą *zna ruiny*):

| Wynik | Rezultat                                                                          |
|-------|-----------------------------------------------------------------------------------|
| 3–5   | postać gubi trop przy suszarniach i traci godzinę na przeszukiwanie łodzi         |
| 6–8   | postać dochodzi do suszarni i wie, że pomiot poszedł nabrzeżem, ale nie wie dokąd |
| 9–18  | postać dochodzi śladami do schodków na plażę i wylotu kanału                      |

**Kanał od plaży**, gdy postać przeciska się nim z pochodnią (przeciętne; tylko przy odpływie, zob. *Przypływ i odpływ*):

| Wynik | Rezultat                                                      |
|-------|---------------------------------------------------------------|
| 3–8   | pochodnia gaśnie w wodzie, postać jest w całkowitej ciemności |
| 9–18  | postać przechodzi z płonącą pochodnią                         |

**Pojmanie pomiota żywcem**, gdy postać ma worek, sieć albo linę (taktyka walki, w której postać nie rani pomiota; przeciętne w świetle, trudne bez niego):

| Wynik | Rezultat                                                        |
|-------|-----------------------------------------------------------------|
| 3–4   | pomiot gryzie postać (lekka rana) i wyrywa się, walka trwa      |
| 5–8   | pomiot wyślizguje się, walka trwa                               |
| 9–18  | pomiot jest w worku albo w sieci, szarpie się, ale nie ucieknie |

**Uspokojenie pomiota jedzeniem**, gdy postać rzuca mu rybę albo mięso i nie podchodzi (łatwe; bez jedzenia niemożliwe):

| Wynik | Rezultat                                                                          |
|-------|-----------------------------------------------------------------------------------|
| 3–5   | pomiot rzuca się na jedzenie, a potem na postać, walka zaczyna się od zaskoczenia |
| 6–18  | pomiot je i patrzy na postać, nie atakuje, dopóki ta nie podejdzie zbyt blisko    |

**Przekonanie Ragny**, żeby zostawiła pomiota postaci (bardzo trudne; przysięga przed Solvarem albo poparcie kogoś, kogo Ragna szanuje, ułatwia o poziom każde):

| Wynik | Rezultat                                                                             |
|-------|--------------------------------------------------------------------------------------|
| 3–5   | Ragna każe swoim ludziom zabrać pomiota siłą, a postać uważa za jego wspólnika       |
| 6–12  | Ragna odmawia, ale nie zatrzymuje postaci, tylko każe ludziom pilnować, co ta zrobi  |
| 13–18 | Ragna się zgadza, ale pod warunkiem: do następnego zmierzchu troll ma być za miastem |

**Zmylenie ludzi Ragny**, gdy postać chce ich odwieść od składu (trudne):

| Wynik | Rezultat                                                                   |
|-------|----------------------------------------------------------------------------|
| 3–5   | ktoś zauważa, że postać kłamie, i ludzie Ragny idą prosto do składu        |
| 6–8   | ludzie Ragny nie wierzą do końca i zostawiają przy składzie jednego stróża |
| 9–18  | ludzie Ragny odchodzą w inną stronę i wracają dopiero po świcie            |

## Zakończenia

Scenariusz kończy się o świcie albo wtedy, gdy los pomiota się rozstrzygnie.

- **Pomiot oddany braciom żywy.** Ketil płaci uncję, a nazajutrz sprzedaje pomiota Domowi Visara albo kupcowi zza morza. Postać ma srebro na ferd i opinię kogoś, kto złapał trolla w Austhavn.
- **Pomiot zabity albo wystawiony na świt przez postać.** Ragna chwali postać przed ludźmi przy rynku. Bracia są wściekli, ale nic nie mogą zrobić. Rano na rynku albo na nabrzeżu stoi posąg pomiota, a dzieci rzucają w niego kamieniami.
- **Pomiot ukryty albo wyprowadzony za miasto.** Postać nic nie zarabia. Jeśli bracia albo Ragna się dowiedzą, ma wrogów w Austhavn. Pomiot następnej nocy wraca do Ulflund.
- **Pomiot wydany ludziom Ragny.** Ragna wykurza go dymem o brzasku, a pomiot kamienieje na nabrzeżu. Rano na rynku Ragna mówi przy ludziach, kto go znalazł, i daje postaci gościnę świątyni do odjazdu ferdu (zob. *Ragna zna kryjówkę*). Bracia mają do postaci żal.
- **Pomiot skamieniały na rynku bez udziału postaci.** Miasto ma nowy posąg i nową opowieść, ale postać nie ma w niej żadnej roli.

To, co ludzie mówią o postaci po tej nocy, MG zapisuje w dzienniku kampanii jako jej imię (zob. *Prawo, waśń i dobre imię* w `Settings/Kaldara/Mechanics.md`), np. „złapała trolla w Austhavn” albo „to przez nią uciekł troll z Wielorybiej Kości”.

## Co dalej

Trzy dni po tej nocy ferd rusza z Wielorybiej Kości na północ, do Grimsfjord. To drugi scenariusz kampanii. Trakt z Austhavn biegnie tuż obok Ulflund, a stado, od którego oderwał się pomiot, wciąż tam żyje. Pierwszej nocy ferd obozuje pod lasem. MG zapisuje w postępie scenariusza, jak skończyła się ta noc, bo w drugim scenariuszu ma to znaczenie:

- czy pomiot przeżył i wrócił do stada,
- czy postać go uratowała, zabiła, oddała braciom albo zostawiła ludziom Ragny,
- czy Ketil i Orm albo Ragna są postaci wrogami, dłużnikami czy przyjaciółmi,
- co ludzie mówią o postaci w Austhavn.
