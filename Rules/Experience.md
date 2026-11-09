# Doświadczenie

Postać gracza zdobywa doświadczenie, przechodząc kolejne scenariusze. Mierzą je dwie wartości na karcie postaci: **poziom doświadczenia** i **punkty doświadczenia**. Mają je tylko postacie graczy.

## Poziom doświadczenia

Postać zaczyna grę na zerowym poziomie doświadczenia. Wyjątkiem jest postać, która już na początku ma za sobą bogate doświadczenie, np. stary, doświadczony mag. Taka postać może zacząć na wyższym poziomie, np. siódmym. Poziom startowy ustala MG razem z graczem przy tworzeniu postaci i musi on wynikać z historii postaci. Scenariusz albo setting może wskazać poziom startowy, np. scenariusz przeznaczony dla doświadczonych postaci.

Każdy poziom doświadczenia daje postaci 1 bazowy Punkt Determinacji i podnosi o 1 górny limit bazowych PDT. Postać bez zalet i wad ma więc 10 + poziom bazowych PDT, a jej bazowe PDT musi się mieścić w zakresie od 5 do 15 + poziom. Dolny limit się nie zmienia.

## Awans

Przejście na poziom *n* kosztuje *n* × 500 punktów doświadczenia: awans na 1 poziom kosztuje 500 punktów, a każdy następny o 500 więcej, np. awans z 7 na 8 poziom kosztuje 4000 punktów.

| Poziom | Koszt awansu | Łącznie od poziomu 0 | Bazowe PDT bez cech | Zakres bazowych PDT |
|--------|--------------|----------------------|---------------------|---------------------|
| 0      | —            | —                    | 10                  | 5–15                |
| 1      | 500          | 500                  | 11                  | 5–16                |
| 2      | 1000         | 1500                 | 12                  | 5–17                |
| 3      | 1500         | 3000                 | 13                  | 5–18                |
| 4      | 2000         | 5000                 | 14                  | 5–19                |
| 5      | 2500         | 7500                 | 15                  | 5–20                |
| 6      | 3000         | 10500                | 16                  | 5–21                |
| 7      | 3500         | 14000                | 17                  | 5–22                |
| 8      | 4000         | 18000                | 18                  | 5–23                |
| 9      | 4500         | 22500                | 19                  | 5–24                |
| 10     | 5000         | 27500                | 20                  | 5–25                |

Punkty doświadczenia wydaje się jak walutę. Gdy postać ma dość punktów, gracz może awansować ją na następny poziom: odejmuje koszt awansu od zebranych punktów, a reszta zostaje na kolejne awanse. Awansuje się zawsze o jeden poziom, ale postać, która ma dość punktów, może awansować kilka razy z rzędu, płacąc za każdy poziom osobno.

Postać może awansować w dowolnej chwili, jeśli ma dość punktów doświadczenia. MG przyznaje je jednak dopiero po rozegraniu scenariusza, a nie w jego trakcie (zob. *Przyznawanie punktów doświadczenia*), więc w praktyce postać awansuje zwykle na koniec scenariusza albo na początku następnego.

Przy awansie bazowe PDT, bieżące PDT i górny limit bazowych PDT rosną o 1. MG zapisuje nowy poziom, pozostałe punkty doświadczenia i nowe PDT na karcie postaci.

Gerald jest na 3 poziomie doświadczenia i ma 2300 punktów doświadczenia. Przejście na 4 poziom kosztuje 4 × 500 = 2000 punktów, więc Gerald może awansować. Wydaje 2000 punktów i jest teraz na 4 poziomie z 2300 − 2000 = 300 punktami doświadczenia. Do 5 poziomu, który kosztuje 5 × 500 = 2500 punktów, brakuje mu 2200.

Gerald jest na zerowym poziomie doświadczenia i ma 12 bazowych PDT, a zakres bazowych PDT wynosi 5–15. Awansuje na 1 poziom. Ma teraz 13 bazowych PDT, a zakres bazowych PDT wynosi 5–16.

## Przyznawanie punktów doświadczenia

MG przyznaje punkty doświadczenia na koniec scenariusza. Za co i ile, określa scenariusz. Nagroda może dotyczyć konkretnego dokonania, np. pokonania określonego wroga, uratowania kogoś, rozwiązania zagadki, uniknięcia pułapki albo wydostania się z oblężenia, albo dokonań powtarzalnych, np. każdego zabitego zombie.

Za dokonanie, którego scenariusz nie przewiduje, MG sam ocenia, czy przyznać punkty doświadczenia i ile, kierując się nagrodami, które scenariusz daje za podobne dokonania. Jeśli scenariusz w ogóle nie określa nagród, ustala je MG.

Scenariusz opisuje nagrody zwykle w osobnym pliku `ExperienceRewards.md` w swoim folderze, bo są potrzebne dopiero na koniec scenariusza.

Przyznając punkty, MG podaje graczowi ich sumę i wymienia dokonania, za które je przyznał. Nie zdradza jednak tajemnic, których postać nie odkryła, np. pułapki, którą ominęła, nie wiedząc o niej. Punkty za takie dokonania podaje łącznie, bez wyjaśnienia. Przyznane punkty i dokonania, które gracz poznał, MG zapisuje w postępie scenariusza w folderze kampanii, a nowy stan punktów na karcie postaci (zob. *Kampanie* w `AGENTS.md`).

### Rozmiar scenariusza

Wysokość nagród zależy od rozmiaru scenariusza. Orientacyjne wartości podaje tabela dla pełnego sukcesu, czyli dla postaci, która zrobiła wszystko, co przewiduje fabuła scenariusza, i dostaje najwięcej punktów, jakie scenariusz daje. Nagrody za dokonania powtarzalne liczy się do limitu, który ustala scenariusz, np. za najwyżej 10 zabitych zombie.

| Rozmiar    | Czas gry     | Przykład                                                                                        | Pełny sukces |
|------------|--------------|-------------------------------------------------------------------------------------------------|--------------|
| mikro      | do 1 godziny | krótka historia, jedno miejsce z 3–4 pomieszczeniami, 2–3 postacie MG                           | ok. 250      |
| mini       | ok. 2 godzin | krótka historia, jedno miejsce z 6–8 pomieszczeniami, 4–8 postaci MG                            | ok. 500      |
| przeciętny | ok. 4 godzin | rozbudowana historia, kilka miejsc, w tym jedno wielopoziomowe z co najmniej 10 pomieszczeniami | ok. 1000     |
| duży       | do 6 godzin  | bez ograniczeń                                                                                  | ok. 2000     |

Rozmiar wyznacza przede wszystkim czas gry, a liczby pomieszczeń i postaci MG są tylko przykładem. Miejscem mogą być np. podziemia, budynek albo statek kosmiczny. Dłuższe kampanie dzieli się na scenariusze tych rozmiarów.

Nagrody nie zależą od trudności scenariusza ani od poziomu doświadczenia postaci. Scenariusz jest zbalansowany pod poziom postaci, dla których jest przeznaczony, więc nie ma scenariuszy wyjątkowo zabójczych, za które należałaby się premia. Scenariusz podaje swój rozmiar i poziom albo zakres poziomów doświadczenia postaci, dla których jest przeznaczony. Postać, która gra scenariusz przeznaczony dla niższego poziomu, dostaje tyle samo punktów, ale łatwiej jej je zdobyć.

Koszt awansu rośnie z każdym poziomem, więc postać awansuje coraz wolniej. Przy pełnych sukcesach postać zdobywa około 250 punktów na godzinę gry, czyli dochodzi do poziomu *n* po mniej więcej *n* × (*n* + 1) godzinach gry.

## Przykład

> Najemniczka wydostaje się ze stacji orbitalnej opanowanej przez zbuntowane roboty. Wyprowadza z niej rannego technika, po drodze niszczy cztery roboty bojowe, a z przemytnikami, którzy zajęli hangar, dogaduje się bez walki.

Scenariusz przewiduje 150 punktów doświadczenia za wydostanie się ze stacji, 100 za uratowanie technika, 20 za każdy zniszczony robot bojowy i 100 za wyłączenie reaktora. Najemniczka reaktora nie wyłączyła. Scenariusz nie przewiduje nagrody za układ z przemytnikami, ale MG uznaje go za dokonanie i przyznaje za nie 50 punktów. Najemniczka dostaje 150 + 100 + 4 × 20 + 50 = 380 punktów doświadczenia.

Najemniczka jest na zerowym poziomie doświadczenia i miała już 300 punktów, więc ma teraz 680. Awansuje na 1 poziom za 500 punktów i zostaje jej 180. Jej bazowe PDT rośnie z 11 do 12, a zakres bazowych PDT wynosi teraz 5–16.
