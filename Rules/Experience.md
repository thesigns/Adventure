# Experience

The player character gains experience by playing through scenarios. It is measured by two values on the character sheet: **experience level** and **experience points**. Only player characters have them.

## Experience level

A character starts play at experience level zero. The exception is a character who already has rich experience behind them at the start, e.g. an old, seasoned mage. Such a character can start at a higher level, e.g. seventh. The GM sets the starting level together with the player at character creation, and it must follow from the character's background. A scenario or setting can specify a starting level, e.g. a scenario intended for experienced characters.

Each experience level gives the character 1 base Determination Point and raises the cap on base DP by 1. A character without advantages and disadvantages therefore has 10 + level base DP, and their base DP must be in the range from 5 to 15 + level. The lower limit does not change.

## Advancement

Reaching level *n* costs *n* × 500 experience points: advancing to level 1 costs 500 points, and each next level 500 more, e.g. advancing from level 7 to 8 costs 4000 points.

| Level | Advancement cost | Total from level 0 | Base DP without traits | Base DP range |
|-------|------------------|--------------------|------------------------|---------------|
| 0     | —                | —                  | 10                     | 5–15          |
| 1     | 500              | 500                | 11                     | 5–16          |
| 2     | 1000             | 1500               | 12                     | 5–17          |
| 3     | 1500             | 3000               | 13                     | 5–18          |
| 4     | 2000             | 5000               | 14                     | 5–19          |
| 5     | 2500             | 7500               | 15                     | 5–20          |
| 6     | 3000             | 10500              | 16                     | 5–21          |
| 7     | 3500             | 14000              | 17                     | 5–22          |
| 8     | 4000             | 18000              | 18                     | 5–23          |
| 9     | 4500             | 22500              | 19                     | 5–24          |
| 10    | 5000             | 27500              | 20                     | 5–25          |

Experience points are spent like currency. When the character has enough points, the player can advance them to the next level: subtract the advancement cost from the points collected, and the rest remains for further advancement. Advancement is always by one level, but a character with enough points can advance several times in a row, paying for each level separately.

A character can advance at any moment if they have enough experience points. The GM, however, awards them only after the scenario has been played, not during it (see *Awarding experience points*), so in practice a character usually advances at the end of a scenario or at the start of the next one.

On advancement base DP, current DP and the cap on base DP rise by 1. The GM writes the new level, the remaining experience points and the new DP on the character sheet.

Gerald is at experience level 3 and has 2300 experience points. Reaching level 4 costs 4 × 500 = 2000 points, so Gerald can advance. He spends 2000 points and is now at level 4 with 2300 − 2000 = 300 experience points. He is 2200 short of level 5, which costs 5 × 500 = 2500 points.

Gerald is at experience level zero and has 12 base DP, and his base DP range is 5–15. He advances to level 1. He now has 13 base DP, and his base DP range is 5–16.

## Awarding experience points

The GM awards experience points at the end of a scenario. The scenario sets what for and how many. A reward can concern a specific achievement, e.g. defeating a particular enemy, saving someone, solving a puzzle, avoiding a trap or breaking out of a siege, or repeatable achievements, e.g. every zombie killed.

For an achievement the scenario does not foresee, the GM judges whether to award experience points and how many, guided by the rewards the scenario gives for similar achievements. If the scenario sets no rewards at all, the GM sets them.

A scenario usually describes its rewards in a separate file `ExperienceRewards.md` in its folder, because they are needed only at the end of the scenario.

When awarding points, the GM tells the player their total and lists the achievements they were awarded for. The GM does not, however, reveal secrets the character has not discovered, e.g. a trap they avoided without knowing about it. Points for such achievements are given as a lump sum, without explanation. The GM records the points awarded and the achievements the player has learned of in the scenario progress in the campaign folder, and the new point total on the character sheet (see *Kampanie* in `AGENTS.md`).

### Scenario size

The size of rewards depends on the size of the scenario. The table gives rough values for full success, i.e. for a character who did everything the scenario's plot foresees and gets the most points the scenario gives. Rewards for repeatable achievements count up to a limit set by the scenario, e.g. for at most 10 zombies killed.

| Size    | Play time     | Example                                                                              | Full success |
|---------|---------------|--------------------------------------------------------------------------------------|--------------|
| micro   | up to 1 hour  | a short story, one place with 3–4 rooms, 2–3 GM characters                           | about 250    |
| mini    | about 2 hours | a short story, one place with 6–8 rooms, 4–8 GM characters                           | about 500    |
| medium  | about 4 hours | an elaborate story, several places, including one multi-level with at least 10 rooms | about 1000   |
| large   | up to 6 hours | no limits                                                                            | about 2000   |

Size is set mainly by play time, and the numbers of rooms and GM characters are only examples. A place can be e.g. a dungeon, a building or a spaceship. Longer campaigns are split into scenarios of these sizes.

Rewards do not depend on the scenario's difficulty or on the character's experience level. A scenario is balanced for the level of the characters it is intended for, so there are no exceptionally deadly scenarios that would deserve a bonus. A scenario states its size and the experience level or range of levels of the characters it is intended for. A character who plays a scenario intended for a lower level gets the same number of points, but earns them more easily.

The advancement cost grows with each level, so the character advances more and more slowly. With full successes a character earns about 250 points per hour of play, i.e. reaches level *n* after roughly *n* × (*n* + 1) hours of play.

## Example

> A mercenary escapes from an orbital station taken over by rebel robots. She leads a wounded technician out, destroys four combat robots on the way, and strikes a deal without a fight with the smugglers who have taken the hangar.

The scenario foresees 150 experience points for escaping the station, 100 for saving the technician, 20 for each combat robot destroyed and 100 for shutting down the reactor. The mercenary did not shut down the reactor. The scenario foresees no reward for the deal with the smugglers, but the GM counts it as an achievement and awards 50 points for it. The mercenary gets 150 + 100 + 4 × 20 + 50 = 380 experience points.

The mercenary is at experience level zero and already had 300 points, so she now has 680. She advances to level 1 for 500 points and has 180 left. Her base DP rises from 11 to 12, and her base DP range is now 5–16.
