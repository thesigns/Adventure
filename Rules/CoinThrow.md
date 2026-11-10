# Coin toss

A coin toss settles an unresolvable dispute between the player and the GM, e.g. about the course of events, the interpretation of a rule or what the character could have known or done. It does not replace the 3d6 roll and is not used to resolve the character's actions or to price advantages and disadvantages (see `Rules/CharacterCreation.md`).

The coin shows only one of two things: **"the GM is right"** or **"the player is right"**. Each has a 50% chance. The decision is final and both sides accept it.

The GM makes the coin toss with the script `Scripts/coin.py`:

```
python Scripts/coin.py --campaign Randuvil --desc "Did the character manage to close the gate" --gm "the gate was open" --player "the character closed the gate"
```

- `--campaign` is the name of the campaign folder in `Campaigns/`. It is required, and the folder must already exist.
- `--desc` is a short description of the dispute. It is required.
- `--gm` and `--player` are the positions of both sides. They are optional, but worth giving, so that it is clear what the coin decides.

The script prints the result "The GM is right" or "The player is right" and records the toss in the file `Rolls.log` in the campaign folder.
