# Standard roll

Every uncertain outcome is resolved with a **3d6** roll: roll three six-sided dice and add them up. The total ranges from 3 to 18.

Only the GM rolls, always with the script (see *Scripted rolls*). A roll can also concern a GM character, e.g. whether a guard notices the player character or whether a doctor manages to stop the bleeding.

Each situation is resolved with a single roll, even when several characters take part in it. There are no opposed rolls: the player character and the guard do not roll separately and compare results. The GM sets up one outcome table and takes into account the skills and circumstances of both sides (see *Circumstances*).

The player can improve the odds by spending Determination Points before the roll (see `Rules/Determination.md`).

## When to roll

Roll only when the outcome of a situation is uncertain and matters to the adventure.

- **Trivial situations** are resolved without a roll.
- **Impossible situations** simply fail, also without a roll. The GM describes what happens instead.
- **Situations without risk or time pressure** succeed without a roll if the character can keep trying until they succeed. The only cost is time.
- **A failed action cannot be retried** in the same situation. Another attempt requires the situation to change: a different method, tool, help or the passage of time.

A roll does not have to concern the player character's action. It can resolve:

- the action of an enemy or another GM character (does the guard notice the character, does the archer hit),
- the reaction of a GM character (does the guard believe them, does the boy help),
- a random event (does the bridge hold, does the storm come before dusk),
- a fact about the world the scenario does not settle (is there a smith in the village).

Facts settled by the scenario are not resolved with a roll.

## Outcome table

Before every roll the GM sets up an **outcome table**. It assigns specific consequences to ranges of results, based on the GM's judgement of the situation. The table must cover all results from 3 to 18. Once set, a table is not changed after the roll.

A table can have more than two outcomes, e.g. full success, success at a cost, failure and failure with a wound.

In every table a **high result is good** for the player character and a low one bad, even when the roll concerns an enemy (high result: the guard does not notice the character). Only when no outcome is better or worse for the player character is the order arbitrary.

Tables are **open**: the GM shows the player the table before the result. The GM words the outcomes so that they do not reveal scenario secrets the character does not know, e.g. "the seal works" rather than "the chieftain is imprisoned forever".

### Player's decision

If the roll concerns the player character and the character can realistically judge the odds, the GM first shows the table and does not roll. A roll concerns the player character when its result depends on the character's effort: on their action or on how they cope with a threat. This holds even when the roll is formally made for an enemy, e.g. whether a guard notices the sneaking character.

The player then decides how many Determination Points to spend (see `Rules/Determination.md`) and, if the character can still back out, whether to act at all. The player can:

- **act:** the GM rolls against the table shown, which can no longer be changed, with extra dice for the Determination Points spent,
- **give up:** there is no roll, and giving up is not a failed action, so the character can try later,
- **change the approach:** the GM sets up a new table for the new approach and again waits for a decision.

If the character can no longer back out (a sudden attack, a trap already sprung) but sees the danger, the player can neither give up nor change the approach. They only decide how many Determination Points to spend.

In all other cases the GM rolls at once, without Determination Points, and shows the table together with the result. This covers situations in which the character cannot judge the odds (does not know the bridge is rotten, does not see the archer in ambush) and rolls that do not depend on the character's effort (reactions of GM characters unrelated to the character's action, random events, facts about the world).

### Difficulty

To keep tables consistent between sessions, the GM sets the success threshold by difficulty level:

| Difficulty        | Failure | Success | Chance of success |
|-------------------|---------|---------|-------------------|
| easy              | 3–5     | 6–18    | 95%               |
| average           | 3–8     | 9–18    | 74%               |
| hard              | 3–10    | 11–18   | 50%               |
| very hard         | 3–12    | 13–18   | 26%               |
| nearly impossible | 3–15    | 16–18   | 5%                |

Within failure and success the GM can set apart degrees, e.g. failure with a wound on the lowest results or exceptional success on the highest. The GM can also set the threshold between difficulty levels.

**Levels in points.** Changing difficulty by one level moves the success threshold by 2 points, and by half a level by 1 point. Making an action harder raises the threshold, making it easier lowers it. The table gives the starting thresholds. The extreme levels are wider than 2 points (easy 6, nearly impossible 16), because the 3d6 distribution has few results there, so a shift from them can give a threshold between levels.

An average action (threshold 9) made harder by darkness (a level) and a light wound (half a level) has a threshold of 9 + 2 + 1 = 12.

### Circumstances

The GM judges difficulty at once, taking into account all circumstances that matter. The reference point is an average member of the species and profession of whoever acts (see `Rules/CharacterCreation.md`), rested and prepared to act. Reading a scroll is easier for a wizard than for a peasant, and tracking is easier for a hunter than for a townsman. Each significant circumstance changes difficulty usually by one level (2 points of threshold), and an exceptionally strong one by two (4 points). The same circumstance counts only once. Several means especially effective against the same enemy, e.g. silver and fire against a wraith, count as one circumstance.

An action easier than easy is trivial and needs no roll. An action harder than nearly impossible is impossible.

Typical circumstances:

| Makes easier                                 | Makes harder                                                                    |
|----------------------------------------------|---------------------------------------------------------------------------------|
| an advantage that fits the action            | a disadvantage that fits the action                                             |
| a good tool or preparation                   | an improvised weapon or tool                                                    |
| surprising the enemy                         | darkness, fog, downpour                                                         |
| favourable terrain                           | unfavourable terrain                                                            |
| means especially effective against the enemy | wounds (see *Wound levels* in `Rules/Health.md`), fatigue, hunger, intoxication |
| a weakened enemy (wounded, exhausted)        | every additional enemy                                                          |

## Examples

> The player character climbs a three-metre stone wall without a rope, slippery with rain.

For an average human this would be hard, but the character has the advantage *acrobat*, so the GM judges the action as average. The GM sets up the outcome table:

| Result | Outcome            |
|--------|--------------------|
| 3–4    | falls, light wound |
| 5–8    | falls, scratch     |
| 9–18   | success            |

The roll is 7: the character falls off the wall and is scratched (5% wound level).

> Later the character sneaks at night past a guard dozing by a campfire.

The GM rolls whether the guard notices them. The darkness and the dozing guard make it easier, but the fire lights part of the yard, so the GM judges slipping past unnoticed as average. High results are good for the player character, which means the guard does not notice them:

| Result | Outcome                                              |
|--------|------------------------------------------------------|
| 3–5    | the guard notices the character and raises the alarm |
| 6–8    | the guard hears something and gets up to check       |
| 9–18   | the guard notices nothing                            |

## Scripted rolls

The GM makes every roll with the script `Scripts/roll.py`. The outcome table is given in the command, so it is fixed before the roll:

```
python Scripts/roll.py --campaign Randuvil --desc "Climbing the wall" "3-4:falls, light wound" "5-8:falls, scratch" "9-18:success"
```

- `--campaign` is the name of the campaign folder in `Campaigns/`. It is required, and the folder must already exist.
- `--desc` is a short description of what the roll is about.
- `--dp` is the number of Determination Points spent (default 0). The script then rolls that many more dice, drops the lowest and adds up the best three.
- Each table entry has the form `from-to:outcome` or `result:outcome`. The ranges must cover all results from 3 to 18, with no gaps and no overlaps.
- `--rounds` is the maximum number of rolls in a series with the same table (default 1), and `--stop` lists the results that end the series, e.g. `--stop 3-5,17-18`. In a series `--dp` applies to each roll separately. Series are used for consecutive rounds of combat (see *Series of rounds* in `Rules/Combat.md`).
- `--table NAME` takes a named table from the `Tables/GmTables.json` file of the setting or scenario instead of entries in the command.
- `--preview` prints only the table with the chance of each outcome for 0, 1, 2 and 3 DP spent (or up to the number in `--dp`, if higher), without rolling and without an entry in `Rolls.log`. The GM uses it when showing the player a table before their decision (see *Player's decision*) and quotes the chances from the preview, never computed in their head.
- `--hidden --label E` is a roll hidden from the player, when the world or scenario says to hide it. The script does not print the result, only saves it in the campaign's hidden state (see *Sekrety MG* in `AGENTS.md`). The table is then given with `--table`, so that the command reveals nothing.

The script prints the table with the chance of each outcome (with DP spent, also the chance without them), the dice rolled, the dice dropped, the result and the outcome. It records every roll in the file `Rolls.log` in the campaign folder.

Example with 2 DP spent:

```
python Scripts/roll.py --campaign Elandir --desc "Climbing a rope up the temple wall" --dp 2 "3:falls, serious wound" "4:falls, medium wound" "5-6:falls, light wound" "7-11:climbs, but someone notices him" "12-18:climbs unnoticed"
```
