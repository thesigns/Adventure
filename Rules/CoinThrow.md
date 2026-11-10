# Coin toss

A coin toss settles an unresolvable dispute between the player and the GM, e.g. about the course of events, the interpretation of a rule or what the character could have known or done. It does not replace the 3d6 roll and is not used to resolve the character's actions or to price advantages and disadvantages (see `Rules/CharacterCreation.md`).

The coin shows only one of two things: **"the GM is right"** or **"the player is right"**. Each has a 50% chance. The decision is final and both sides accept it.

The GM makes the coin toss with the script `Scripts/coin.py`:

```
python Scripts/coin.py --kampania Randuvil --opis "Did the character manage to close the gate" --mg "the gate was open" --gracz "the character closed the gate"
```

- `--kampania` is the name of the campaign folder in `Campaigns/`. It is required, and the folder must already exist.
- `--opis` is a short description of the dispute. It is required.
- `--mg` and `--gracz` are the positions of both sides. They are optional, but worth giving, so that it is clear what the coin decides.

The script prints the result "Rację ma MG" (the GM is right) or "Rację ma gracz" (the player is right) and records the toss in the file `Rolls.log` in the campaign folder.
