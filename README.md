# Adventure

Adventure is a solo role-playing game system in which the Game Master is an
AI agent (e.g. Claude Code) and the player is a human. The repository
contains a rulebook, instructions for the agent and scripts for dice rolls,
maps and the GM's secrets.

The system is generic and suits any genre: fantasy, science fiction,
cyberpunk, horror and others. It does not assume any particular convention,
and the player character can die. It has its own simple mechanics and does
not use D&D rules.

The rules, settings and scripts are in English, but the game itself is played
in Polish: the GM translates the rules and descriptions in the narration.

## How to play

1. Open the repository in Claude Code or another agent that reads
   `AGENTS.md`.
2. Ask to start a game, e.g. "Let's play the *Crypt* scenario".
3. The agent reads the rules and the scenario, helps you create a character
   and runs the game. You describe what your character does.

The agent rolls dice only with scripts, never mentally. Before every roll it
shows the outcome table, i.e. what each possible result means. It records the
character's state, the course of play and all rolls in the campaign folder,
so the game can be resumed in a new conversation, and the same scenario can
be played independently by different characters.

## Mechanics in brief

- **Standard roll:** every uncertain situation is resolved with a single 3d6
  roll against an outcome table, which the GM sets and shows before the
  roll. A high result is always good for the player.
- **Determination Points (DP):** the character's pool of effort and luck.
  Each point spent is an extra die, and the lowest dice are dropped. The pool
  refreshes after proper rest.
- **Traits:** advantages make actions easier or possible, and disadvantages
  make them harder or impossible. Disadvantages give the character more DP,
  and advantages fewer.
- **Health:** instead of hit points every creature has a wound level from 0%
  to 100%. Wounds raise it, and it sets the penalties to actions.
- **Combat:** fought in rounds. Each round is a single roll with a table
  that describes the consequences for both sides. The fight goes on until it
  is decided.
- **Equipment:** has no statistics. Weapons, armour and tools act as
  circumstances the GM takes into account in the outcome table.
- **Experience:** at the end of a scenario the character gets experience
  points, which are spent on advancement. Each level gives an extra DP.

## Repository structure

| Path         | Contents                                                                  |
|--------------|---------------------------------------------------------------------------|
| `AGENTS.md`  | instructions for the agent running the game                               |
| `Rules/`     | core rules, shared by all worlds                                          |
| `Settings/`  | settings, i.e. descriptions of worlds, each in a folder with `Setting.md` |
| `Scenarios/` | scenarios, each in a folder with `Scenario.md`                            |
| `Campaigns/` | campaigns: character sheet, log, scenario progress and rolls              |
| `Scripts/`   | Python scripts for rolls, coin tosses, maps and the GM's secrets          |

Rules files in `Rules/`:

| File                   | Contents                                                        |
|------------------------|-----------------------------------------------------------------|
| `Rules.md`             | overview of the mechanics with links to the other files         |
| `StandardThrow.md`     | the standard roll, outcome tables, difficulty                   |
| `Determination.md`     | Determination Points                                            |
| `Health.md`            | health, wounds, healing and death                               |
| `Combat.md`            | combat                                                          |
| `Traits.md`            | character traits: advantages and disadvantages                  |
| `Experience.md`        | experience and advancement                                      |
| `Equipment.md`         | equipment                                                       |
| `CoinThrow.md`         | coin toss, which settles disputes between the player and the GM |
| `CharacterCreation.md` | character creation                                              |
| `CharacterTemplate.md` | character sheet template                                        |

## Scripts

The scripts need Python 3 and use only the standard library. The campaign
name (`--campaign`) is required, and every roll goes to
`Campaigns/<campaign>/Rolls.log`.

A 3d6 roll against an outcome table (optionally with DP spent):

```
python Scripts/roll.py --campaign Randuvil --desc "Climbing the wall" --dp 1 "3-4:falls, light wound" "5-8:falls, scratch" "9-18:success"
```

A coin toss in a dispute between the player and the GM:

```
python Scripts/coin.py --campaign Randuvil --desc "Did the character manage to close the gate" --gm "the gate was open" --player "the character closed the gate"
```

The player map with fog of war, on which the GM reveals the places the
character has discovered. The browser preview refreshes itself:

```
python Scripts/fogmap.py --campaign Randuvil --map Scenarios/Crypt/Maps/MapCrypt.svg --reveal 1 2 --open
```

The GM's hidden state (world clock, hidden events and rolls) is kept by
`Scripts/gm.py`, so that secrets never appear in the console the player sees.

## Scenarios and settings

A scenario can be written by a human, by an agent or by both together. The
file `Scenario.md` always states the setting: the name of a folder in
`Settings/` or a short description of the world, e.g. "a low fantasy world,
the adventure takes place in a village cut off from the world and in
a nearby crypt".

For now the repository contains one test scenario, **Crypt**
(`Scenarios/Crypt/`), written in Polish. It is a short mini adventure in a low
fantasy world described in the scenario itself: the character goes down into
a crypt under a hill to find a missing shepherd. The scenario has a crypt map
with fog of war for the player and a treasure script.

The only setting is **Generia** (`Settings/Generia/`): a thoroughly generic
fantasy world with elves, dwarves, magic and monsters, described tersely to
take up as little context as possible. Whatever it does not describe, the GM
fills in with the most typical fantasy convention.

## Licence

The project is released under the MIT licence, see [LICENSE](LICENSE).
