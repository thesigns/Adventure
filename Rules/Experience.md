# Doświadczenie

Postać gracza zdobywa doświadczenie, przechodząc kolejne scenariusze. Mierzą je dwie wartości na karcie postaci: **poziom doświadczenia** i **punkty doświadczenia**. Mają je tylko postacie graczy.

## Poziom doświadczenia

Postać zaczyna grę na zerowym poziomie doświadczenia. Wyjątkiem jest postać, która już na początku ma za sobą bogate doświadczenie, np. stary, doświadczony mag. Taka postać może zacząć na wyższym poziomie, np. siódmym. Poziom startowy ustala MG razem z graczem przy tworzeniu postaci i musi on wynikać z historii postaci. Scenariusz albo setting może wskazać poziom startowy, np. scenariusz przeznaczony dla doświadczonych postaci.

Każdy poziom doświadczenia daje postaci 1 bazowy Punkt Determinacji i podnosi o 1 górny limit bazowych PDT. Postać bez zalet i wad ma więc 10 + poziom bazowych PDT, a jej bazowe PDT musi się mieścić w zakresie od 5 do 15 + poziom. Dolny limit się nie zmienia.

## Awans

Przejście na poziom *n* kosztuje *n* × 1000 punktów doświadczenia, np. awans z 7 na 8 poziom kosztuje 8000 punktów.

| Poziom | Koszt awansu | Łącznie od poziomu 0 | Bazowe PDT bez cech | Zakres bazowych PDT |
|--------|--------------|----------------------|---------------------|---------------------|
| 0      | —            | —                    | 10                  | 5–15                |
| 1      | 1000         | 1000                 | 11                  | 5–16                |
| 2      | 2000         | 3000                 | 12                  | 5–17                |
| 3      | 3000         | 6000                 | 13                  | 5–18                |
| 4      | 4000         | 10000                | 14                  | 5–19                |
| 5      | 5000         | 15000                | 15                  | 5–20                |
| 6      | 6000         | 21000                | 16                  | 5–21                |
| 7      | 7000         | 28000                | 17                  | 5–22                |
| 8      | 8000         | 36000                | 18                  | 5–23                |
| 9      | 9000         | 45000                | 19                  | 5–24                |
| 10     | 10000        | 55000                | 20                  | 5–25                |

Punkty doświadczenia wydaje się jak walutę. Gdy postać ma dość punktów, gracz może awansować ją na następny poziom: odejmuje koszt awansu od zebranych punktów, a reszta zostaje na kolejne awanse. Awansuje się zawsze o jeden poziom, ale postać, która ma dość punktów, może awansować kilka razy z rzędu, płacąc za każdy poziom osobno.

Postać może awansować w dowolnej chwili, jeśli ma dość punktów doświadczenia. MG przyznaje je jednak dopiero po rozegraniu scenariusza, a nie w jego trakcie (zob. *Przyznawanie punktów doświadczenia*), więc w praktyce postać awansuje zwykle na koniec scenariusza albo na początku następnego.

Przy awansie bazowe PDT, bieżące PDT i górny limit bazowych PDT rosną o 1. MG zapisuje nowy poziom, pozostałe punkty doświadczenia i nowe PDT na karcie postaci.

Gerald jest na 3 poziomie doświadczenia i ma 4300 punktów doświadczenia. Przejście na 4 poziom kosztuje 4 × 1000 = 4000 punktów, więc Gerald może awansować. Wydaje 4000 punktów i jest teraz na 4 poziomie z 4300 − 4000 = 300 punktami doświadczenia. Do 5 poziomu, który kosztuje 5 × 1000 = 5000 punktów, brakuje mu 4700.

Gerald jest na zerowym poziomie doświadczenia i ma 12 bazowych PDT, a zakres bazowych PDT wynosi 5–15. Awansuje na 1 poziom. Ma teraz 13 bazowych PDT, a zakres bazowych PDT wynosi 5–16.

## Przyznawanie punktów doświadczenia

MG przyznaje punkty doświadczenia na koniec scenariusza. Za co i ile, określa scenariusz. Nagroda może dotyczyć konkretnego dokonania, np. pokonania określonego wroga, uratowania kogoś, rozwiązania zagadki, uniknięcia pułapki albo wydostania się z oblężenia, albo dokonań powtarzalnych, np. każdego zabitego zombie.

Za dokonanie, którego scenariusz nie przewiduje, MG sam ocenia, czy przyznać punkty doświadczenia i ile, kierując się nagrodami, które scenariusz daje za podobne dokonania. Jeśli scenariusz w ogóle nie określa nagród, ustala je MG.

Orientacyjnie, jedna prosta miniprzygoda daje średnio około 300–400 punktów doświadczenia. Nagrody rosną tylko z rozmachem i trudnością scenariusza, a nie z poziomem doświadczenia postaci, dla których scenariusz jest przeznaczony. Koszt awansu rośnie z każdym poziomem, więc postać awansuje coraz wolniej.

Scenariusz opisuje nagrody zwykle w osobnym pliku `ExperienceRewards.md` w swoim folderze, bo są potrzebne dopiero na koniec scenariusza.

Przyznając punkty, MG podaje graczowi ich sumę i wymienia dokonania, za które je przyznał. Nie zdradza jednak tajemnic, których postać nie odkryła, np. pułapki, którą ominęła, nie wiedząc o niej. Punkty za takie dokonania podaje łącznie, bez wyjaśnienia. Przyznane punkty i dokonania, które gracz poznał, MG zapisuje w postępie scenariusza w folderze kampanii, a nowy stan punktów na karcie postaci (zob. *Kampanie* w `AGENTS.md`).

## Przykład

> Najemniczka wydostaje się ze stacji orbitalnej opanowanej przez zbuntowane roboty. Wyprowadza z niej rannego technika, po drodze niszczy cztery roboty bojowe, a z przemytnikami, którzy zajęli hangar, dogaduje się bez walki.

Scenariusz przewiduje 150 punktów doświadczenia za wydostanie się ze stacji, 100 za uratowanie technika, 20 za każdy zniszczony robot bojowy i 100 za wyłączenie reaktora. Najemniczka reaktora nie wyłączyła. Scenariusz nie przewiduje nagrody za układ z przemytnikami, ale MG uznaje go za dokonanie i przyznaje za nie 50 punktów. Najemniczka dostaje 150 + 100 + 4 × 20 + 50 = 380 punktów doświadczenia.

Najemniczka jest na zerowym poziomie doświadczenia i miała już 700 punktów, więc ma teraz 1080. Awansuje na 1 poziom za 1000 punktów i zostaje jej 80. Jej bazowe PDT rośnie z 11 do 12, a zakres bazowych PDT wynosi teraz 5–16.
