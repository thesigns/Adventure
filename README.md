# Adventure

Adventure to system jednoosobowej gry fabularnej, w którym Mistrzem Gry jest
agent AI (np. Claude Code), a graczem człowiek. Repozytorium zawiera
podręcznik z zasadami, instrukcje dla agenta i skrypty do rzutów kośćmi.

System jest generyczny i nadaje się do każdego gatunku: fantasy, science
fiction, cyberpunku, horroru i innych. Nie zakłada konwencji heroicznej, więc
postać gracza może zginąć. Ma własną, prostą mechanikę i nie korzysta z zasad
D&D.

## Jak grać

1. Otwórz repozytorium w Claude Code albo innym agencie, który czyta plik
   `AGENTS.md`.
2. Poproś o rozpoczęcie gry, np. „Zagrajmy w scenariusz *Krypta*”.
3. Agent czyta zasady i scenariusz, pomaga stworzyć postać i prowadzi grę.
   Ty opisujesz, co robi twoja postać.

Agent rzuca kośćmi wyłącznie skryptami, nigdy w pamięci. Przed każdym rzutem
pokazuje tablicę rezultatów, czyli to, co oznacza każdy możliwy wynik. Stan
postaci, przebieg gry i wszystkie rzuty zapisuje w folderze kampanii, dzięki
czemu grę można wznowić w nowej rozmowie, a ten sam scenariusz mogą niezależnie
rozegrać różne postacie.

## Mechanika w skrócie

- **Rzut standardowy:** każdą niepewną sytuację rozstrzyga jeden rzut 3K6
  według tablicy rezultatów, którą MG ustala i pokazuje przed rzutem. Wysoki
  wynik jest zawsze korzystny dla gracza.
- **Punkty Determinacji (PDT):** pula wysiłku i szczęścia postaci. Każdy
  wydany punkt to dodatkowa kość, a najsłabsze kości się odrzuca. Pula
  odnawia się po porządnym wypoczynku.
- **Cechy:** zalety ułatwiają albo umożliwiają działania, a wady je
  utrudniają albo wykluczają. Wady dają postaci więcej PDT, a zalety mniej.
- **Zdrowie:** zamiast punktów życia każda istota ma poziom zranienia od 0%
  do 100%. Rany go podnoszą, a od niego zależą kary do działań.
- **Walka:** toczy się w rundach. Każda runda to jeden rzut z tablicą, która
  opisuje skutki dla obu stron. Walka trwa do rozstrzygnięcia.
- **Ekwipunek:** nie ma statystyk. Broń, pancerz i narzędzia działają jak
  okoliczności, które MG uwzględnia w tablicy rezultatów.

## Struktura repozytorium

| Ścieżka      | Zawartość                                                                      |
|--------------|--------------------------------------------------------------------------------|
| `AGENTS.md`  | instrukcje dla agenta prowadzącego grę                                         |
| `Rules/`     | zasady podstawowe, wspólne dla wszystkich światów                              |
| `Settings/`  | settingi, czyli opisy światów, każdy w folderze z głównym plikiem `Setting.md` |
| `Scenarios/` | scenariusze, każdy w folderze z głównym plikiem `Scenario.md`                  |
| `Campaigns/` | kampanie: karta postaci, dziennik, postęp scenariuszy i rzuty                  |
| `Scripts/`   | skrypty Pythona do rzutów                                                      |

Pliki zasad w `Rules/`:

| Plik                   | Zawartość                                              |
|------------------------|--------------------------------------------------------|
| `Rules.md`             | przegląd mechaniki z odsyłaczami do pozostałych plików |
| `StandardThrow.md`     | rzut standardowy, tablice rezultatów, trudność         |
| `Determination.md`     | Punkty Determinacji                                    |
| `Health.md`            | zdrowie, rany, leczenie i śmierć                       |
| `Combat.md`            | walka                                                  |
| `Traits.md`            | cechy postaci: zalety i wady                           |
| `Equipment.md`         | ekwipunek                                              |
| `CoinThrow.md`         | rzut monetą, który rozstrzyga spory gracza z MG        |
| `CharacterCreation.md` | tworzenie postaci                                      |
| `CharacterTemplate.md` | szablon karty postaci                                  |

## Skrypty

Skrypty wymagają Pythona 3 i korzystają tylko z biblioteki standardowej.
Nazwa kampanii (`--kampania`) jest obowiązkowa, a każdy rzut trafia do
`Campaigns/<kampania>/Rolls.log`.

Rzut 3K6 z tablicą rezultatów (opcjonalnie z wydanymi PDT):

```
python Scripts/roll.py --kampania Randuvil --opis "Wspinaczka na mur" --pdt 1 "3-4:upadek, lekka rana" "5-8:upadek, draśnięcie" "9-18:sukces"
```

Rzut monetą w sporze między graczem a MG:

```
python Scripts/coin.py --kampania Randuvil --opis "Czy postać zdążyła zamknąć bramę" --mg "brama była otwarta" --gracz "postać zamknęła bramę"
```

Mapa gracza z mgłą wojny, na której MG odsłania miejsca odkryte przez postać.
Podgląd w przeglądarce odświeża się sam:

```
python Scripts/fogmap.py --kampania Randuvil --mapa Scenarios/Krypta/MapCrypt.svg --odkryj 1 2 --otworz
```

## Scenariusze i settingi

Scenariusz może napisać człowiek, agent albo obaj razem. Plik `Scenario.md`
zawsze podaje setting: nazwę folderu z `Settings/` albo krótki opis świata,
np. „świat low fantasy, przygoda dzieje się we wsi odciętej od świata
i w pobliskiej krypcie”.

Repozytorium zawiera na razie jeden testowy scenariusz, **Krypta**
(`Scenarios/Krypta/`). To krótka mini-przygoda w świecie low fantasy, opisanym
w samym scenariuszu: postać schodzi do krypty pod wzgórzem, żeby odnaleźć
zaginionego pastucha. Scenariusz ma mapę krypty z mgłą wojny dla gracza
i skrypt losujący skarby. Settingów na razie nie ma.

## Licencja

Projekt jest udostępniony na licencji MIT, zob. [LICENSE](LICENSE).
