# Rzut monetą

Rzut monetą rozstrzyga nierozwiązywalny spór między graczem a MG, np. o przebieg wydarzeń, interpretację zasady albo to, co postać mogła wiedzieć lub zrobić. Nie zastępuje rzutu 3K6 i nie służy do rozstrzygania działań postaci ani wyceny zalet i wad (zob. `Rules/CharacterCreation.md`).

Moneta wskazuje tylko jedno z dwóch: **„Rację ma MG”** albo **„Rację ma gracz”**. Każda możliwość ma szansę 50%. Rozstrzygnięcie jest ostateczne i obie strony je przyjmują.

Rzut monetą MG wykonuje skryptem `Scripts/coin.py`:

```
python Scripts/coin.py --kampania Randuvil --opis "Czy postać zdążyła zamknąć bramę" --mg "brama była otwarta" --gracz "postać zamknęła bramę"
```

- `--kampania` to nazwa folderu kampanii w `Campaigns/`. Jest obowiązkowa, a folder musi już istnieć.
- `--opis` to krótki opis sporu. Jest obowiązkowy.
- `--mg` i `--gracz` to stanowiska obu stron. Są opcjonalne, ale warto je podać, żeby było jasne, co rozstrzyga moneta.

Skrypt wypisuje rezultat „Rację ma MG” albo „Rację ma gracz” i zapisuje rzut w pliku `Rolls.log` w folderze kampanii.
