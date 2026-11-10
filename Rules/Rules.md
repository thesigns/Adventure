# Game rules

## Character creation

Before playing a scenario, the player creates a character: their name, age, sex, species, profession and background, plus advantages, disadvantages and experience level (usually zero), which set the base number of Determination Points. The GM sets their starting equipment. The reference point is an average member of the character's species and profession, so traits typical of them are neither advantages nor disadvantages. Full character creation rules are in `Rules/CharacterCreation.md`.

## Character sheet

The player character's sheet is the file `Character.md` in their campaign folder, e.g. `Campaigns/Randuvil/Character.md` (see `Rules/CharacterCreation.md`). The GM keeps it up to date and updates it as soon as anything changes, including:

- current DP after every spending of points and every refresh of the pool,
- wound level and injuries after every wound and every day of healing,
- equipment: items gained, lost, used up and damaged, and the count of ammunition, light sources, rations and other supplies,
- money,
- traits and base DP when the character gains or loses an advantage or disadvantage,
- experience points when awarded, and experience level and base DP after advancement,
- plot threads.

The sheet is the source of truth about the character's state. When resuming play, the GM reads the character's state from the sheet.

## Standard roll

Every uncertain outcome is resolved with a **3d6** roll against an outcome table the GM sets up before the roll. Only the GM rolls, always with the script `Scripts/roll.py`, and the player can improve the odds by spending Determination Points. Full standard roll rules, including when to roll, how to build outcome tables and how to judge difficulty, are in `Rules/StandardThrow.md`.

## Determination Points

Determination Points (DP) are the effort, persistence and luck the player character can put into an action that matters to them. For every point spent before a roll, the GM rolls one extra die and drops the lowest, and the pool refreshes after proper rest. Full rules are in `Rules/Determination.md`.

## Health, wounds and death

Every creature has a wound level from 0% (unhurt) to 100% (death), raised by wounds ranging from a scratch to a mortal blow and mangling. The wound level sets penalties to actions, and wounds heal only in at least minimally comfortable conditions. Full rules, including the wound scale, creature toughness, dying, injuries, healing and death, are in `Rules/Health.md`.

## Equipment

Equipment has no separate mechanics: weapons, armour, tools and other items act as circumstances the GM takes into account in the outcome table. Armour narrows the enemy's wound range by 1–2 points and makes wounds up to two steps lighter, a shield and cover narrow the wound range further, and the GM tracks consumables such as ammunition and light sources on the character sheet. Full rules are in `Rules/Equipment.md`.

## Combat

Combat is fought in rounds of about 10 seconds, and each round is one standard roll with a table describing the consequences for both sides. Before combat the player sets the character's tactics, and the fight goes on until it is decided by death, dying, flight or surrender of one side. The player can order rounds with the same table as a series, which the GM rolls with a single command. Fatigue counts only against someone who tires more slowly or not at all, and makes the fight harder every 6 rounds. Full combat rules, including enemy categories and the typical layout of a round table, are in `Rules/Combat.md`.

## Companions

A companion is a GM character who joins the player character for a time: a hireling, a guide, a friend, a trained animal. The GM runs them according to their nature and loyalty (hired, allied, friendly or devoted), and a morale roll decides whether they stand firm when the risk exceeds it. Bound servants, e.g. undead, golems or drones, obey every command, know no fear and break free only under conditions set by the world or the scenario. Help from a companion makes an action easier, and a companion fighting at the character's side makes the fight easier by a level or more, depending on their category. Companions never advise the player. Full rules are in `Rules/Companions.md`.

## Traits (advantages and disadvantages)

An advantage sets the character apart from an average member of their species and profession: it makes actions in its field one level easier or makes possible actions that would otherwise be impossible. A disadvantage works the other way. Traits are chosen at character creation, affect the base number of Determination Points and very rarely change during play. An advantage can also grant a supernatural ability, whose effect, limits and number of uses the GM sets when pricing it. Full rules are in `Rules/Traits.md`.

## Experience

A character usually starts at experience level zero and at the end of each scenario receives experience points for achievements set by the scenario or judged by the GM. Points are spent like currency on advancement: reaching level *n* costs *n* × 500 points. Rewards depend on scenario size: full success gives from about 250 points in a micro scenario to about 2000 in a large one. Each level gives the character 1 base Determination Point and raises the cap on base DP by 1. Full rules are in `Rules/Experience.md`.

## Fatigue, hunger and light

- **No sleep:** every day without sleep makes all actions one level harder, until a night's sleep.
- **Hunger:** every day without food makes all actions one level harder, until a meal.
- **Darkness:** an action in the dark that needs sight is one level harder, and two levels in total darkness.
- **Light sources** last a limited time set by the world (see *Consumables* in `Rules/Equipment.md`).

The GM tracks the time of day and the passage of time.

## Coin toss

An unresolvable dispute between the player and the GM, e.g. about the course of events or the interpretation of a rule, is settled by a coin toss with the script `Scripts/coin.py`. The coin shows either "the GM is right" or "the player is right", and the decision is final. Full rules are in `Rules/CoinThrow.md`.

## World rules

The core rules are shared by all worlds. The world is described by a setting in `Settings/` or, if a scenario uses no setting, by the scenario itself. A setting can extend the core rules, and a scenario can extend both. In a conflict the scenario decides, then the setting, and the core rules last. In particular, the world defines:

- the convention and mood of the game,
- examples of enemies in each category and the toughness of creatures,
- examples of light, medium and heavy armour,
- the healing rate of species other than human and additional ways of healing,
- magic, prayer and other supernatural powers, if they exist,
- gear, prices, mounts, vehicles and unusual items, e.g. how long light sources last.
