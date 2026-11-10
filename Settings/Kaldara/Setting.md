# Kaldara

Kaldara to świat nordyckiej sagi z domieszką baśni i grozy. Zimna, wulkaniczna wyspa wzorowana na Islandii, długie zimy, lodowce, gorące źródła i pola lawy. Ludzie rządzą się tu bez króla, sądzą się na tingu i mszczą przez pokolenia. W górach leżą ruiny zaginionego państwa krasnoludów, a w ruinach mieszkają trolle. Bogowie istnieją naprawdę, ale odpowiadają rzadko i po swojemu.

O człowieku świadczy tu jego imię: co zrobił, komu dotrzymał słowa, kogo pomścił i co skaldowie o nim śpiewają. Śmiałek schodzi w ciemność po złoto i po pieśń, która przetrwa go o sto lat. Los jest silniejszy od ludzi, ale to, jak człowiek go przyjmie, należy do niego. Magia jest cicha, rzadka i niepewna. Potwory pochodzą z sag i ludowych opowieści. Najgroźniejsze są i tak zima, ciemność i drugi człowiek.

## Pliki settingu

- `Setting.md`: przegląd świata, zasady dla MG, nazwy, zejścia, Wolna Wspólnota, klimat, magia i frakcje (ten plik)
- `Geography.md`: wymiary wyspy, podróże, miasta i krainy
- `Dwarves.md`: krasnoludy, co wiedzą o nich ludzie i prawda o ich upadku, której nie zna nikt na wyspie
- `Trolls.md`: trolle, główne zagrożenie wyspy
- `Gods.md`: bogowie i ich kulty
- `Bestiary.md`: potwory z głębin, strażnicy ruin i stwory z powierzchni
- `Diseases.md`: choroby wyspy i ich mechanika, w tym czarny kaszel śmiałków
- `Mechanics.md`: świat przełożony na mechanikę systemu: profesje, zalety i wady, kalendarz, dzień i noc, słońce i trolle, światło, zimno, podróże, przeciwnicy, broń, pancerz, leczenie, magia, przedmioty krasnoludzkie, ceny i prawo
- `MapKaldara.svg`: mapa wyspy w skali 1 piksel = 500 m
- `daylight.json`: wschody, zachody i ciemność z tabeli *Dzień i noc* w `Mechanics.md`, z których `Scripts/gm.py czas --setting Kaldara` wypisuje porę dnia
- `gm_tables.json`: tablice ukrytych rzutów dla `Scripts/gm.py` i `Scripts/roll.py --ukryty` (zob. *Podróż w ferdzie* w `Mechanics.md` i *Zakażenie* w `Diseases.md`)
- `tools/`: narzędzia autora, nie do gry: generator mapy (`make_map.py`) i jego fonty

Mapa wyspy jest jawna. Postać gracza zna ogólną geografię wyspy: miasta, krainy, góry, lodowiec, główne rzeki i trakty. Gracz może więc oglądać `MapKaldara.svg` w całości, a MG nie odsłania jej skryptem `Scripts/fogmap.py`. Na mapie wyspy nie ma ruin ani niczego, czego ludzie na wyspie nie wiedzą. Mapy konkretnych miejsc, np. ruin, mają scenariusze i te MG odsłania zwykłym trybem.

## Zasady dla MG

- Postać gracza to śmiałek, który chodzi na zejścia samotnie. Nie ma stałych towarzyszy ani drużyny. Postacie MG mogą jej towarzyszyć tylko epizodycznie, na krótki czas, i nigdy nie podejmują decyzji ani nie rozwiązują problemów za nią.
- Podczas zejść postać może spotykać innych śmiałków. Mogą okazać się pomocą albo zagrożeniem. MG nie zdradza z góry, kim są i czego chcą.
- Ton gry jest poważny. Świat traktuje się serio, a zagrożenia są prawdziwe. Humor może się pojawić, suchy i oszczędny jak w sagach, ale gra nie jest komedią ani parodią.
- MG opowiada jak saga: rzeczowo i oszczędnie, czynami i słowami ludzi, a nie opisami ich uczuć. Ludzie mówią mało, a to, co mówią, waży. Wielkie rzeczy dzieją się po cichu: cios pada bez zapowiedzi, a obelga zostaje zapamiętana na lata.
- Nadprzyrodzone jest rzadkie i nigdy zwyczajne. Draugr, wieszczba czy runiczny miecz to wydarzenie, o którym opowiada się latami, a nie codzienność.
- Jeśli czegoś nie ma w settingu ani w scenariuszu, MG uzupełnia to w duchu sag i nordyckich podań, dopasowanym do surowego, zimnego i wulkanicznego świata, a nie w duchu fantasy z gier. Uzupełnia tylko świat i klimat, a nie mechanikę: nie przenosi do gry zasad, mechanik ani pojęć z innych systemów RPG.
- Na wyspie żyją tylko ludzie. Nie ma elfów, krasnoludów, niziołków, gnomów ani innych ras grywalnych. Krasnoludy istnieją tylko w ruinach i legendach. Żywe krasnoludy nigdy nie pojawiają się w grze.
- Nikt nie potrafi odczytać krasnoludzkich run ani zrozumieć krasnoludzkiego języka. Żadna postać, księga ani zaklęcie tego nie umożliwia.
- Gracz może znać cały setting, łącznie z prawdą o upadku krasnoludów z `Dwarves.md`. Jego postać wie jednak tylko to, co wiedzą ludzie na wyspie, i gracz odgrywa ją zgodnie z tą wiedzą. MG tak samo odgrywa postacie MG: każda wie tylko to, co mogłaby wiedzieć. Prawdy o upadku krasnoludów nie zna nikt na wyspie. Ślady są w ruinach i postać może łączyć je sama.
- Na wyspie nie ma króla, armii ani straży państwowej. Prawo istnieje, ale wyroki egzekwują poszkodowani, ich rody, wodzowie albo ci, których wynajmą.
- Gra składa się ze scenariuszy dwóch rodzajów. **Zejście** to samotna wyprawa do ruin: droga, eksploracja, walka, łup, powrót. **Historia na powierzchni** dzieje się w osadach, miastach i dziczy: waśnie rodów, sprawy przed tingiem, banici, polowanie na potwora, intrygi wodzów, sprzedaż łupu.
- Świat nie ma jednej wielkiej fabuły, ale scenariusze mogą układać się w kampanię: zejścia przeplatają się z historiami na powierzchni, a skutki jednych (łup, sława, wrogowie, długi) prowadzą do kolejnych.
- Nazwy miejsc są takie jak w `Geography.md`, a imiona bogów takie jak w `Gods.md`. Nowe nazwy i imiona MG tworzy według zasad z rozdziału *Nazwy*.
- Na wyspie są dziesiątki wiosek, osad i dworów wodzów, rozsianych wzdłuż wybrzeża i traktów. Setting ich nie nazywa, a mapa ich nie pokazuje. MG tworzy je według potrzeb scenariusza tam, gdzie wygodnie, zwykle na wybrzeżu, w zatokach, w dolinach rzek i przy traktach.
- Ruin krasnoludzkich i wejść do nich są na wyspie dziesiątki, dużych i małych. Setting żadnej nie nazywa ani nie zaznacza na mapie. MG tworzy je według potrzeb scenariusza, najczęściej w górach i w głębi wyspy.
- Przygody dzieją się na wyspie. Kontynent istnieje, ale pozostaje w tle.
- Pora roku ma znaczenie. Zimą wnętrze wyspy jest praktycznie nie do przebycia.
- Pora dnia ma znaczenie. Za dnia zagrożeniem jest dzicz, nocą i pod ziemią trolle.

## Nazwy

Wszystkie nazwy i imiona na wyspie są ludzkie i brzmią nordycko, jak w sagach: Sigrun, Ragnar, Hallvik, Grimsfjord. MG tworzy nowe nazwy sam, według poniższych zasad.

- **Pisownia.** Nazwy i imiona zapisuje się tylko literami alfabetu angielskiego, bez znaków skandynawskich (å, æ, ø, ö, ð, þ) i polskich (ą, ć, ę, ł, ń, ó, ś, ź, ż). Piszemy Svartjokul, nie Svartjökull, i Hvitlund, nie Hvítlund. Dzięki temu nazwy brzmią tak samo w każdym języku gry.
- **Bez prawdziwych bogów.** Nie używaj imion prawdziwych nordyckich bogów (Odyn, Thor, Freja, Loki i inni), także jako członów imion i nazw (Thorkel, Freydis). Bogowie wyspy są w `Gods.md`.
- **Imiona** są krótkie, zwykle dwusylabowe albo złożone z dwóch członów. Męskie kończą się często na -ar, -ulf, -mund, -bjorn, -geir, -vard, -stein, -kel (Ragnar, Asmund, Hallvard, Ulfgeir, Grimkel). Żeńskie na -run, -dis, -hild, -veig, -frid, -a (Sigrun, Asdis, Ragnhild, Bergljot, Halla).
- **Ojciec i przydomek.** Ludzie przedstawiają się imieniem i imieniem ojca, rzadziej matki: „Ragnar, syn Ulfa”, „Sigrun, córka Halli”. Ludzie znani mają przydomki, które w odróżnieniu od imion tłumaczy się na język gry: Ragnar Siwobrody, Asdis Jednooka, Hallvard Bez Ziemi.
- **Rody** nazywa się od założyciela albo od dworu: ród Asmunda, ludzie z Hallvik.
- **Nazwy miejsc** składają się z członu opisowego i członu, który mówi, jakie to miejsce, np. Austhavn (wschodni port), Svartjokul (czarny lodowiec). Typowe człony rodzajowe: -vik (zatoka), -fjord (fiord), -havn (port), -nes (cypel), -strand (wybrzeże), -fjell (góra), -dal (dolina), -foss (wodospad), -myr (bagno), -jokul (lodowiec), -hraun (pole lawy), -lund (gaj), -vold (pole, równina), -stad (dwór, gospodarstwo), -borg (warownia), -heim (dom, siedziba), -skard (przełęcz), -gap (rozpadlina), -hall (sala), -gard (zagroda, osada), -vaka (przerębel, oczko wody, które nie zamarza). Typowe człony opisowe: svart (czarny), hvit (biały), raud (czerwony), kald (zimny), brenn (palący), grim (ponury), stein (kamień), hof (świątynia), ting (zgromadzenie), ulf (wilk), ravn (kruk), bjarka (brzoza), dverg (krasnolud), troll (troll), aust, vest, nord i sud (strony świata).
- **Ruiny krasnoludzkie** też noszą ludzkie nazwy, nadane przez osadników od wyglądu, położenia albo legendy, np. Dverghall (krasnoludzka sala) albo Ravnskard (krucza przełęcz). W narracji MG może podać też znaczenie nazwy w języku gry.
- **Trolle** mówią własnym językiem, a znane trolle ludzie nazywają od legowiska albo przezwiskiem w języku gry: troll spod Ravnskard, Czerwony Pysk.
- **Spójność.** Każdą nową nazwę, którą postać poznała i która może wrócić w grze, MG zapisuje w postępie scenariusza albo w dzienniku kampanii z krótką notatką, kto albo co to jest. Przed ponownym użyciem nazwy sprawdza ją tam. Nie nadaje tej samej nazwy dwóm miejscom ani tego samego imienia dwóm ważnym postaciom. Epizodyczne postacie mogą pozostać bezimienne, dopóki gracz nie zapyta o imię albo postać nie stanie się ważna.

## Świat w skrócie

Kaldara to duża wyspa na północnym oceanie, tuż pod kręgiem polarnym, daleko od kontynentu, który leży na wschodzie. Ponad tysiąc lat temu rządziły nią krasnoludy. Ludzie nazywają ich dawne państwo Dvergheim, czyli "dom krasnoludów", i uważają je za imperium, bo nic mniejszego nie zbudowałoby tego, co po nim zostało. Krasnoludy drążyły góry, wydobywały metale i klejnoty, kuły broń w ogniu wulkanów i budowały twierdze, które miały przetrwać wieczność. Potem zniknęły. Ludzie mają wiele teorii: wielka erupcja, zaraza, wojna, ucieczka za morze. Najpopularniejsza opowieść mówi, że kopały za głęboko.

Około czterystu lat temu na wyspę przypłynęli ludzie z kontynentu. Wielu z nich uciekało przed władzą tamtejszych królów i nie chciało nad sobą nowego. Zastali puste wybrzeża, milczące góry i ruiny, w których mieszkały trolle. Pierwsze statki przybiły do wschodnich fiordów, ale ich ludzie opłynęli wyspę i najlepszą ziemię znaleźli na zachodzie. Tam założyli pierwsze dwory, z których wyrosły najstarsze rody. Późniejsi przybysze musieli zadowolić się wschodem i zostali przy morzu i handlu. Wszyscy trzymali się wybrzeża, a zamiast królestwa stworzyli Wolną Wspólnotę: wodzów, wspólne prawo i doroczne zgromadzenie. Kontakt z kontynentem z biegiem lat osłabł. Dziś pływają tam tylko nieliczne statki kupieckie z Austhavn, a dla większości mieszkańców wyspy kontynent to odległa kraina z opowieści.

Cywilizacja na Kaldarze to miasta, wioski i dwory rozsiane wzdłuż wybrzeża, połączone niebezpiecznymi traktami i drogą morską. Wnętrze wyspy to dzicz: góry, lodowce, pola lawy, wulkany i ruiny Dvergheimu. W ruinach wciąż leżą skarby krasnoludów. Co roku śmiałkowie ruszają po nie na zejścia, każdy sam, na własną rękę i na własne ryzyko, bez niczyjej zapłaty i niczyjego rozkazu. Schodzą do kopalń i grobowców krasnoludów, walczą z trollami i ze sobą nawzajem, wynoszą złoto i runiczne przedmioty, i albo giną młodo, albo trafiają do sag.

## Zejścia

Zejście to samotna wyprawa do krasnoludzkich ruin po skarby. Na zejścia chodzą śmiałkowie: młodsi synowie bez spadku, zubożali gospodarze, wojownicy szukający sławy, banici, którzy nie mają nic do stracenia.

- Nikt nie zleca zejść i nikt za nie nie płaci. Śmiałkowie idą po złoto, krasnoludzkie przedmioty i sławę.
- Na zejście chodzi się samemu. Tak każe obyczaj i zdrowy rozsądek: w ruinach wspólnicy częściej zabijają się nawzajem o złoto, niż giną od trolli. Kto bierze kogoś ze sobą, uchodzi za tchórza albo za głupca.
- Według prawa Wspólnoty łup z ruin należy do tego, kto go wyniósł. Ani wódz, ani ród, ani nikt inny nie może się o niego upominać.
- W ruinach nie ma świadków. To, co zdarzy się między śmiałkami pod ziemią, rzadko trafia przed sąd.
- W jednej ruinie bywa naraz kilku śmiałków. Spotkanie pod ziemią zawsze jest niepewne. Inny śmiałek może pomóc, podzielić się wiedzą, zawrzeć krótkie przymierze przeciw trollom, wymienić się zapasami. Może też śledzić, okraść, zastawić pułapkę albo zabić, żeby zabrać łup. Często zrobi jedno i drugie.
- W ruinach leżą też ciała śmiałków, którym się nie udało, razem z ich ekwipunkiem i tym, co zdążyli znaleźć.
- Krasnoludzkie złoto i klejnoty śmiałkowie sprzedają albo wymieniają w miastach, najchętniej w Austhavn, gdzie płacą najwięcej. Krasnoludzką broń i zbroje często zatrzymują dla siebie.
- Udane zejście daje sławę. Skaldowie układają o nim pieśni, a imiona śmiałków trafiają do sag.
- Złoto z zejść zmienia porządek na wyspie. Bogaty śmiałek może kupić tytuł wodza i zebrać stronników. Niejeden dzisiejszy ród zaczął od jednego udanego zejścia, a stare rody patrzą na nowych bogaczy z pogardą i obawą.
- Większość zejść kończy się porażką albo śmiercią. Mówi się, że z pierwszego zejścia wraca jeden śmiałek na trzech.
- Zejścia odbywają się głównie latem. Śmiałkowie zbierają się wiosną, najczęściej w Grimsfjord, i wracają przed zimą. Wiosną noce są jeszcze ciemne, więc już sama droga na zbiórkę bywa niebezpieczna.
- Wielki Ting wypada w środku pory zejść. Wielu śmiałków jedzie na niego sprzedać łup, pochwalić się, posłuchać pieśni o sobie albo załatwić sprawy przed sądem, ale za każdy tydzień na Tingu płaci tygodniem lata straconym dla ruin.

## Wolna Wspólnota

Ludzie na Kaldarze nie mają króla. Rządzą się sami, według wspólnego prawa.

- **Wodzowie** to najpotężniejsi ludzie na wyspie. Jest ich kilkudziesięciu. Władza wodza to tytuł, który można odziedziczyć, kupić albo sprzedać, ale bez ludzi jest nic niewart. Wódz jest tak silny, jak jego majątek, rodzina, przyjaciele i stronnicy.
- **Stronnicy** to wolni gospodarze, którzy wybrali sobie wodza. Wódz broni ich interesów, oni stają przy nim z bronią w razie sporu i jeżdżą z nim na zgromadzenia. Gospodarz może odejść do innego wodza, więc wodzowie konkurują o ludzi hojnością, sprytem i opieką.
- Wyspa dzieli się na cztery **ćwierci**: Zachodnią, Północną, Wschodnią i Południową. Każdej wiosny wodzowie każdej ćwierci zbierają się na tingu, żeby rozstrzygać miejscowe spory.
- Raz w roku, latem, w białe noce, ludzie z całej wyspy zjeżdżają na **Wielki Ting** na polu Tingvold. Przez dwa tygodnie wodzowie stanowią i zmieniają prawo, sądy rozstrzygają sprawy, a reszta handluje, swata, pije, załatwia porachunki i słucha skaldów. To jedyny czas, kiedy cała wyspa jest w jednym miejscu. Z najdalszych krańców wyspy jedzie się tu konno dwa tygodnie.
- **Głosiciel Prawa** wybierany jest przez wodzów na trzy lata. Zna prawo na pamięć i co roku recytuje je ze **Skały Prawa** w środku Tingvold. To najbardziej szanowany urząd na wyspie, ale bez żadnej siły.
- Sądy wydają wyroki, ale nikt ich nie wykonuje za poszkodowanego. Wyrok egzekwuje sam poszkodowany, jego ród albo wódz. Kto jest za słaby, może odsprzedać swoje roszczenie komuś silniejszemu.
- Najczęstsza kara to **główszczyzna**, czyli zapłata za krzywdę lub zabójstwo. Najsurowsza to **wyjęcie spod prawa**: banita traci wszystko, nikt nie może mu pomóc, a każdy może go zabić bezkarnie. Banici kryją się w lesie Bjarkalund i w kryjówkach przy głównych traktach albo próbują dostać się na statek do kontynentu. W głąb wyspy nie uciekają, bo nie ma tam co jeść, a nocą polują trolle.
- Spory między rodami często zamieniają się w krwawe waśnie, ciągnące się pokoleniami. Prawo i sądy są po to, żeby je zakończyć, ale udaje się to tylko czasem.
- W ostatnich latach kilka najbogatszych rodów skupuje coraz więcej tytułów wodzowskich. Starzy ludzie mówią, że tak zaczynają się królestwa.

## Klimat i życie na wyspie

- Klimat jest zimny i wietrzny. Lato jest krótkie i chłodne, z białymi nocami. Zima jest długa, ciemna i śnieżna, z zorzami na niebie.
- Wyspa leży tuż pod kręgiem polarnym. Mniej więcej od początku maja do początku sierpnia noc nie ciemnieje do końca (zob. *Dzień i noc* w `Mechanics.md`). W środku zimy dzień trwa kilka godzin, a na północnym wybrzeżu słońce ledwo wychyla się zza horyzontu.
- Wyspa żyje z morza i owiec: rybołówstwo, wieloryby, wełna, suszone ryby. Zboże rośnie tylko na nizinach zachodniej ćwierci i jest drogie.
- Na wyspie hoduje się małe, krępe i wytrzymałe konie. To podstawowy środek podróży po lądzie. Kto nie ma konia, chodzi pieszo i jest biedakiem.
- Domy są z kamienia i darni, w miastach także z drewna sprowadzanego zza morza. Drewno jest cenne. Wiele budowli stoi na fundamentach krasnoludzkich albo jest z nich zbudowanych.
- Ogień w palenisku to życie. W każdym domu płonie bez przerwy przez całą zimę, a jego wygaśnięcie uchodzi za bardzo zły znak.
- Gorące źródła są wszędzie. Ludzie kąpią się w nich, gotują w nich i ogrzewają nimi domy. Przy źródłach często stoją kapliczki Eldry.
- Wulkany wybuchają co kilka lub kilkanaście lat, ziemia regularnie drży. Popiół, trujące opary i lawa to część życia.
- Lato to pora zejść. Zimą wyprawy w głąb wyspy kończą się zwykle śmiercią, więc śmiałkowie zimują w miastach i przepijają łupy.
- Białe noce chronią przed trollami: niebo nie ciemnieje wtedy do końca, więc trolle nie wychodzą na powierzchnię. Długie zimowe noce to czas, kiedy trolle najczęściej podchodzą pod osady.
- Na zachód od wyspy jest tylko otwarty ocean. Nikt tam nie pływa, a statki, które próbowały, nie wróciły.
- Mieszkańcy są twardzi, małomówni i praktyczni. Cenią honor, hojność i dotrzymane słowo. Opowiadają sagi o pierwszych osadnikach, o waśniach, o śmiałkach, krasnoludach i trollach.
- Gościnność to obowiązek. Wędrowca, który zapuka zimą, wpuszcza się do ognia i karmi, nawet jeśli to wróg. Gość, który nadużyje gościny, i gospodarz, który skrzywdzi gościa, tracą dobre imię na zawsze.
- Słowo ma wagę. Przysięgi składa się na pierścień, na broń albo przy ogniu, a złamana przysięga hańbi cały ród. Obelga wymaga odpowiedzi, a zniesławiający wiersz skalda potrafi zaszkodzić bardziej niż miecz.
- Ludzie wierzą w los. Co komu przeznaczone, to go spotka, więc nie ma sensu się bać. Liczy się tylko, jak człowiek przyjmie swój los i co zostanie po nim w pamięci ludzi.
- Ludzie wierzą w znaki: sny, kruki, ptaki lecące nad dworem, krew na księżycu, ogień, który przygasa bez powodu. Przed ważną decyzją pyta się wieszczkę albo rzuca losy.

## Krasnoludy

Ponad tysiąc lat temu wyspą rządziły krasnoludy. Zniknęły, a po nich zostały ruiny pełne skarbów, runy, których nikt nie umie odczytać, i strażnicy, którzy wciąż bronią korytarzy. Żywych krasnoludów nie ma i nigdy nie pojawiają się w grze.

Opis krasnoludów i prawda o ich upadku są w `Dwarves.md`.

## Trolle

Trolle to główne zagrożenie wyspy: rozumne, dzikie i okrutne istoty z Głębin, które żyją samotnie w krasnoludzkich ruinach i gromadzą wszystko, co błyszczy. Światło słońca zamienia je w kamień, więc na powierzchnię wychodzą tylko w ciemności, a ognia się boją.

Opis trolli jest w `Trolls.md`, a ich mechanika w `Mechanics.md`.

## Geografia

Kaldara ma około 500 km ze wschodu na zachód i 320 km z północy na południe. Cywilizacja trzyma się wybrzeża: cztery miasta, Austhavn na wschodzie, Hofvik na zachodzie, Grimsfjord na północy i Myrvaka na południu, oraz dziesiątki wiosek i dworów. Wnętrze wyspy to dzicz: wulkany i ruiny gór Dvergfjell w centrum, lodowiec Svartjokul na południu i pola lawy Pustkowi Hraun wokół gór.

Opis geografii, miast i krain jest w `Geography.md`.

## Ludzie

Na wyspie żyją tylko ludzie, potomkowie osadników z kontynentu. W Austhavn można spotkać przybyszów zza morza, ale to rzadkość.

Postać gracza jest zawsze człowiekiem z wyspy. Ma profesję, a nie klasę, np. wojownik, łowca, kapłan, wieszczka, skald, wielorybnik, kowal albo zubożały gospodarz (zob. *Podstawowe informacje* w `Rules/CharacterCreation.md`).

## Magia

- Magia istnieje naprawdę, ale jest rzadka, cicha i niepewna. Nikt nie ciska ogniem ani piorunami. Moc przychodzi jako błogosławieństwo, przepowiednia, klątwa, zaklęta pieśń albo znak, często nie od razu i nigdy na pewno. Nie ma czarodziejów, ksiąg zaklęć ani magii, której można się wyuczyć bez boga albo natury.
- **Kapłani i kapłanki** służą bogom w świątyniach i przy kapliczkach. Składają ofiary, odprawiają obrzędy, błogosławią, leczą i zamykają kurhany. Nieliczni dostają od swoich bogów prawdziwą moc.
- **Wieszczki** czerpią moc z natury, najczęściej w służbie Ylvy. Wędrują od dworu do dworu i siadają na wysokim siedzisku, żeby przepowiadać los, pogodę i połów. Zaklinają zwierzęta, rany i wiatr. Ludzie przyjmują je z szacunkiem i lękiem. Wieszczami bywają też mężczyźni, ale rzadko, a ludzie patrzą na nich podejrzliwie i uważają taką moc za niemęską.
- Moc kapłana albo wieszczki jest zaletą postaci, która daje zdolność nadprzyrodzoną (zob. *Zdolności nadprzyrodzone* w `Rules/Traits.md` i *Magia* w `Mechanics.md`). Sama profesja kapłana albo wieszczki bez tej zalety oznacza wiarę, wiedzę i obrzędy, ale nie moc.
- Kapłani, wieszczki i zielarki przygotowują napary, maści i amulety. Te, które naprawdę działają, działają raz albo przez krótki czas, więc są przedmiotami zużywalnymi (zob. *Przedmioty zużywalne* w `Rules/Equipment.md`). Nie kupuje się ich jak towaru na targu: o pomoc świątyni albo wieszczki prosi się za ofiarę, dar albo przysługę. Na wsi jest najwyżej kapliczka i zielarka.
- Krasnoludzkie przedmioty z mocą są rzadkie i cenne. Wszystkie pochodzą z ruin Dvergheimu i są pokryte runami. Ludzie nie umieją ich wytwarzać ani naprawiać. Nie ma magicznych zwojów. W grze działają jak przedmioty niezwykłe (zob. *Przedmioty niezwykłe* w `Rules/Equipment.md`).
- Ponieważ runy są nieczytelne, nikt nie wie z góry, co robi krasnoludzki przedmiot. Jego moc odkrywa się, używając go, czasem z bolesnym skutkiem. Część przedmiotów nie działa wcale albo działa tylko w określonych warunkach, których nikt nie rozumie.
- Moc kapłanek Eldry jest silniejsza w pobliżu wulkanów. Mówią, że to jej oddech płynie pod wyspą i że dlatego krasnoludy potrafiły tu kuć to, czego nikt inny nie umiał.
- Światło słońca, które kapłani Solvara wypraszają modlitwą, działa na trolle tak samo jak prawdziwe słońce, ale jest słabe i krótkotrwałe. Zwykły ogień ani żadne inne światło nie zamienia trolli w kamień.

## Bogowie

Bogów jest wielu i istnieją naprawdę: dają moc swoim kapłanom i odpowiadają na modlitwy. Osadnicy przywieźli kult swoich bogów z kontynentu. Tylko Durgrima poznali dopiero na wyspie, z wizerunków w krasnoludzkich ruinach. Najważniejsi to Solvar, bóg słońca i wróg trolli, oraz Eldra, bogini ognia i wulkanów.

Opis bogów jest w `Gods.md`.

## Potwory

Z głębin przychodzą trolle i ich zwierzęta: pod ziemią są zawsze, na powierzchni tylko nocą. W ruinach czekają też krasnoludzcy strażnicy, którzy nigdy ich nie opuszczają. Dzicz ma własne niebezpieczeństwa: zimę, wilki i niedźwiedzie, draugry z kurhanów, mary, nykry w wodach, tursy w górach i na lodowcu, a w kraterze Brennfell smoka, o którym opowiadają sagi. Groźnych ludzi, takich jak banici, rozbójnicy, morscy łupieżcy i wiedźmy, opisuje rozdział *Frakcje*.

Opis potworów jest w `Bestiary.md`.

## Frakcje

- **Paserzy z Austhavn** – nie gildia, tylko sieć ludzi, którzy znają się nawzajem: kilku kupców z rady miasta, ich zarządcy, właściciele składów i zbiry do wynajęcia. Skupują krasnoludzkie przedmioty bez pytania o pochodzenie, wiedzą, który śmiałek wrócił z łupem, i nasyłają na niego ludzi. Za odpowiednią cenę przemycają banitów za morze. Mają swoich ludzi w każdym mieście, ale nikt nie umie powiedzieć, kto nimi rządzi.
- **Dom Visara** – świątynia boga wiedzy w Austhavn, w której kapłani, skaldowie i uczeni ludzie od pokoleń zbierają wiedzę o krasnoludach. Przerysowują runy i bezskutecznie próbują je odczytać, spisują opowieści śmiałków i rysują ich mapy ruin. Kupują krasnoludzkie przedmioty i badają je, często kosztem zdrowia swoich uczniów, którzy sprawdzają ich działanie na sobie.
- **Zaprzysiężeni Solvara** – bractwo wojowników, którzy przysięgli Solvarowi wierność do śmierci, wyrzekli się ziemi i rodu i żyją razem w warowni w Myrvace, a kilku z nich także przy świątyni w Hofvik. Tropią draugry, trolle i wiedźmy. Część wodzów patrzy na nich podejrzliwie, bo bractwo to jedyna siła na wyspie, która przypomina wojsko, i nie słucha żadnego wodza.
- **Banici** – ludzie wyjęci spod prawa. Stracili wszystko, nikt nie może im pomóc, a każdy może ich zabić bezkarnie. Kryją się w lesie Bjarkalund i w kryjówkach przy głównych traktach, bo tylko tam mają z czego żyć: z rabunku, kłusownictwa i kradzieży owiec. Nie mają nic do stracenia, więc są niebezpieczni. Niektórzy sami chodzą na zejścia, a inni czyhają przy traktach na śmiałków, którzy z nich wracają.
- **Rozbójnicy** – rabusie na głównych traktach między osadami i w lesie Bjarkalund, najczęściej tam, gdzie żaden wódz nie pilnuje dróg. W głębi wyspy ich nie ma, bo nie ma tam kogo rabować. Najchętniej napadają na śmiałków wracających z zejść, bo ci są zmęczeni, ranni i niosą łup.
- **Morscy łupieżcy** – załogi łodzi ukrytych w zatoczkach Nordstrand i fiordów wschodu. Napadają na wioski wielorybników, kupieckie statki i odcięte gospodarstwa na wybrzeżu. Łatwo ich wynająć, a jeszcze łatwiej im się narazić.
- **Wiedźmy** – wieszczki, które odeszły od Ylvy i zdziczały. Moc czerpią z bagien i z umarłych w kurhanach. Mieszkają na odludziu, najczęściej na bagnach. Rzucają klątwy, warzą trucizny, budzą draugry z kurhanów i wiedzą rzeczy, których nie powinny wiedzieć. Ludzie z okolicy boją się ich, ale czasem po cichu proszą je o pomoc.
