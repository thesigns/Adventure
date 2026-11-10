# Combat

## Tactics

Before combat the player describes the character's **tactics**, i.e. how the character fights, e.g. "I hack at him with my sword", "I shoot from behind the wagon" or "I try to disarm him and take him alive". If the player does not set them, the GM asks.

Tactics determine which outcomes can appear in the round table. A character who wants to take an enemy alive does not kill them by accident, and a character shooting from cover is harder to hit.

After every round the GM describes the course of the fight, and based on that the player can change tactics, flee, surrender or do something else (see *Between rounds*). The character does not flee or surrender on their own during a round: the player decides that between rounds.

## Rounds

Combat is fought in **rounds**. A round is a short exchange of blows resolved with one roll with its own outcome table. It lasts about 10 seconds, so six rounds are about a minute. The GM takes this into account when tracking the passage of time, e.g. how long a torch burns or when help arrives. The fight goes on until it is decided: one side dies, falls dying, flees or surrenders, or something else ends the fight (help arrives, the enemy is driven off).

Before every round the GM shows the player the table, and the player decides how many Determination Points to spend on that round (see *Player's decision* in `Rules/StandardThrow.md`). Before the first round, if the character can still back out, the player can also change tactics or decline the fight.

The round table describes the consequences for both sides: on low results the enemy wounds the character, on high results the character wounds the enemy, and in between there is an exchange with no result. The no-result band is narrow, so that the fight does not drag on forever. Wounds dealt in a round change the wound level of both sides at once, and so the difficulty of the next round.

The GM knows the enemy's wound level before the roll, so they write outcomes into the table directly: "the bandit falls", "the bandit flees wounded".

A fight with clear stages (e.g. a skirmish with guards, after which their captain arrives) can be split by the GM into several separate fights.

## Between rounds

After a round that did not end the fight, the GM describes the situation, including the enemy's state, and the player decides what next. They can:

- keep fighting the same way,
- change tactics, e.g. drive an animal off with a torch instead of hacking at it with a sword, or fall back behind cover,
- do something other than fighting: flee, surrender, drink a potion, pray, call for help.

The GM sets up the table for the next round according to the player's decision. An action other than fighting takes a round: its table describes whether it worked and whether the enemy wounded the character meanwhile. Surrender ends the fight without a roll, unless the enemy's reaction is uncertain.

A dying character fights no more. What happens to them next depends on the enemy (see *End of combat*).

## Series of rounds

When consecutive rounds have the same table, because the player keeps fighting the same way, spends the same number of Determination Points on each round and no side's wounds change the difficulty, the player can order a series of rounds. The GM shows the table once and rolls the whole series with a single script command with the options `--rounds` and `--stop` (see *Scripted rolls* in `Rules/StandardThrow.md`).

In `--stop` the GM lists the results after which the situation changes: usually wounds to the player character and wounds after which the enemy falls, flees or changes behaviour. If the enemy can fall only after several wounds, the GM sets `--rounds` so that the series ends at the latest in the round in which the enemy could fall. A series also ends when a circumstance outside the table changes, e.g. a torch goes out or help arrives.

After the series the GM describes the fight round by round, and the player again decides what next (see *Between rounds*).

## Fatigue in combat

When both sides tire equally, fatigue does not matter. It counts only when one side tires clearly more slowly or not at all, e.g. a human fighting a golem, an undead or a robot.

The side that tires gets the circumstance "fatigue" after every 6 rounds of continuous fighting, i.e. after about a minute: the fight becomes half a level harder for them (both values move by 1, see *Combat difficulty*). Fatigue accumulates: after 12 rounds it is a level, after 18 one and a half. It passes after a few minutes of rest.

An advantage such as good stamina extends this time to 12 rounds, and a disadvantage such as asthma shortens it to 3. The rule works both ways: if it is the player character who does not tire, the enemy's fatigue makes the fight easier for them.

A series of rounds ends at the latest in the round in which fatigue increases, because the difficulty of the fight changes (see *Series of rounds*).

## Ranged combat

When the player character shoots at an enemy, the GM decides what the enemy does meanwhile, according to their nature, weapons and situation: returns fire (if they can), closes the distance, takes cover or flees (if they have somewhere to go). The GM sets up the round table on that basis. An enemy who returns fire can wound the character in that very round. An enemy running at the character usually does not wound them yet, but on low results reaches them and the fight turns into melee.

When an enemy shoots at the player character and the character sees them, the GM asks the player what the character does before setting up the table, e.g. returns fire, takes cover, charges or flees. The table depends on the answer: a character taking cover reaches cover unharmed on high results, but does not wound the enemy. If the character does not see the shooter, e.g. an archer in ambush, the GM rolls at once, without asking (see *Player's decision* in `Rules/StandardThrow.md`).

The greater the distance, the harder the hit: each clearly greater distance makes the shot one level harder. A target out of the weapon's range cannot be reached, and the shot simply fails, without a roll (see *When to roll* in `Rules/StandardThrow.md`). For example, a knife thrown at an ogre 200 metres away will not get there.

Range is also a circumstance of the fight. Attacking from a distance an enemy who cannot answer in kind makes the fight easier, and a ranged weapon in melee makes it harder. Cover makes hitting harder (see *Shields and cover* in `Rules/Equipment.md`).

## Combat difficulty

The enemy's category (see *Enemies*) gives two values:

- **hit threshold:** a result equal to or above the threshold means the character wounds the enemy,
- **wound range:** results in this range mean the enemy wounds the character.

Circumstances change combat difficulty as with any other action (see *Circumstances* in `Rules/StandardThrow.md`): by 2 points per level and by 1 point per half level (see *Levels in points* in `Rules/StandardThrow.md`). Which value a circumstance moves depends on what it concerns:

- **the character's attack** moves only the hit threshold, e.g. aiming at the head or another weak spot, a weapon better or worse than typical, shooting distance, the enemy's cover and armour,
- **the character's defence** moves only the wound range, e.g. the character's armour, shield and cover, the enemy's weapon better or worse than typical, a weapon that forces the character to let the enemy close,
- **the whole fight** moves both values, e.g. wounds and fatigue of both sides, surprise, terrain, darkness, combat advantages and disadvantages, every additional enemy, which makes the fight one level harder, and companions fighting at the character's side, who make it easier (see *Combat* in `Rules/Companions.md`).

Armour, shields and cover move these values by the amounts given in *Armour* and *Shields and cover* in `Rules/Equipment.md`, not by whole levels.

If a circumstance's description simply says it makes the fight harder or easier, it concerns the whole fight. Making it harder raises the hit threshold or widens the wound range, and making it easier works the other way.

If the wound range disappears after shifting, the enemy cannot wound the character. If the hit threshold exceeds 18, the character cannot wound the enemy with that way of fighting. If the wound range reaches the hit threshold or beyond, the shared results mean both sides wound each other.

Lightly wounded Randuvil hurls a stone from his sling at the head of an average enemy (hit threshold 9, wound range 3–6). Aiming is a circumstance of the attack (+2 to the threshold), and the wound concerns the whole fight (+1 to both values): hit threshold 12, wound range 3–7.

A circumstance that concerns only part of the fight counts only in those rounds, e.g. surprise usually only in the first.

## Wounds in combat

A wound depends on both sides: on what attacks and on who is the target.

- **The attacker's weapon or nature:** every weapon and every attack has a **wound spread**, from the lightest wound on a weak hit to the heaviest on the best. For example, a sling deals from a scratch to a medium wound, a sword from a scratch to a serious wound, and a fireball spell from a scratch to mangling. The typical wound, i.e. the wound from a full hit on an unarmoured human, is given by the *Wound scale* (see `Rules/Health.md`): a dog's bite deals a light wound, and a bear's a serious wound.
- **The target:** the kind of creature and its toughness (see *Toughness* in `Rules/Health.md`), and armour (see *Armour* in `Rules/Equipment.md`) shift the wound by a step or more. A shield and cover do not make wounds lighter, only less frequent. The same sword blow kills a rat, wounds a human and barely scratches a knight in plate armour. This applies to both sides: the player character and the enemy.

The GM sets the wound spread after taking both sides into account and spreads it over the table: the more extreme the result, the heavier the wound.

## Typical round table layout

From the lowest results:

| Result | Outcome |
|---|---|
| 3 | the enemy deals a wound one step heavier than typical, the fight goes on |
| rest of the wound range | the enemy deals the typical wound, the fight goes on |
| from the end of the wound range to the hit threshold | an exchange with no result, the fight goes on |
| from the hit threshold to 16 | the character deals the enemy the typical wound |
| 17–18 | the character deals a wound one step heavier than typical |

With a weapon of a wide wound spread, the GM writes more steps into the table. When an enemy hurls a fireball at the character, a 3 may mean mangling, and the highest results of the wound range only a scratch.

Within this layout the GM can set apart other outcomes, e.g. losing a weapon, damaged armour, the enemy fleeing or an injury.

## Enemies

| Enemy | Examples | Combat difficulty | Hit threshold | Wound range |
|---|---|---|---|---|
| weak | a youth with a knife, a peasant with a pitchfork, a dog | easy | 6 | 3–4 |
| average | bandit, guard, wolf | average | 9 | 3–6 |
| strong | veteran, bear | hard | 11 | 3–9 |
| powerful | great beast, master swordsman | very hard | 13 | 3–11 |
| legendary | creature of legend | nearly impossible | 16 | 3–14 |

The category tells how dangerous the enemy is in a fight, and toughness how hard they are to wound. These are two different things: a master swordsman is a powerful enemy of human toughness.

The world gives its own examples of enemies in each category.

## End of combat

Victory does not have to mean the enemy's death. Enemies behave according to their nature. Humans and animals usually flee or surrender when wounded or when the fight goes badly. Creatures without an instinct for self-preservation fight to the end. The GM takes this into account in the tables.

A player character who falls dying is helpless. The enemy treats them according to their nature: they may finish them off, rob them, capture them or leave them. If their reaction is uncertain, the GM resolves it with a roll.

Fighting to the end against a stronger enemy is very dangerous, because wounds add up and each one makes the fight harder. Against a legendary creature it ends in almost certain death: a sensible character flees or looks for another way. The GM describes the rounds so that the player can see when the fight is going badly.

## Examples

> Randuvil goes down into a cellar and runs into a giant rat.

The player's tactics: "I hit it with my staff". The rat is a weak enemy (hit threshold 6, wound range 3–4) with a very frail build: a staff blow (light wound) is two steps heavier for it (serious wound), enough to break its back. A rat's bite is a scratch. Randuvil's limp makes melee one level harder for the whole fight: hit threshold 8, wound range 3–6. The table for the first round:

| Result | Outcome                                                          |
|--------|------------------------------------------------------------------|
| 3      | the rat bites the leg painfully (light wound), the fight goes on |
| 4–6    | the rat bites the leg (scratch), the fight goes on               |
| 7      | both miss, the fight goes on                                     |
| 8–18   | Randuvil breaks the rat's back with his staff                    |

The roll is 7. The player does not want to risk a bite and decides to drive the rat off with a torch. The GM sets up the next round's table for the new way of fighting:

| Result | Outcome                                                 |
|--------|---------------------------------------------------------|
| 3      | the rat bites the hand (scratch), the fight goes on     |
| 4–6    | the rat hisses but does not back off, the fight goes on |
| 7–18   | the rat flees into the dark                             |

The rat cannot seriously threaten Randuvil: even a series of bites is at most a few light wounds.

> At night Randuvil sleeps by a campfire. A snapping twig wakes him, and a bandit with a club stands over him.

The GM asks about tactics. The player answers: "I grab the staff lying next to me and get to my feet". The bandit is an average enemy (hit threshold 9, wound range 3–6) of human toughness. The club deals a light wound, and so does Randuvil's staff. Randuvil wears no armour. His limp makes melee one level harder for the whole fight, and being caught asleep makes the first round one level harder too: both values move by 4. Randuvil can no longer back out but sees the enemy, so the GM shows the table and asks only about Determination Points:

| Result | Outcome                                                                    |
|--------|----------------------------------------------------------------------------|
| 3      | the bandit hits the head with the club (medium wound), the fight goes on   |
| 4–10   | the bandit hits the arm (light wound), the fight goes on                   |
| 11–12  | Randuvil gets up and parries, the fight goes on                            |
| 13–16  | Randuvil strikes the bandit with the staff (light wound), the bandit flees |
| 17–18  | Randuvil cracks the bandit's head (medium wound), the bandit collapses     |

The player decides this is an important moment and spends 1 DP. The GM rolls 4d6 instead of 3d6 and gets 6: Randuvil is at 10% and lightly wounded. Surprise no longer applies, but the light wound makes the fight half a level harder, so both values move by 1 more: hit threshold 12, wound range 3–9. The player keeps fighting the same way and spends no points:

| Result | Outcome                                                                    |
|--------|----------------------------------------------------------------------------|
| 3      | the bandit hits the head with the club (medium wound), the fight goes on   |
| 4–9    | the bandit hits (light wound), the fight goes on                           |
| 10–11  | an exchange of blows with no result, the fight goes on                     |
| 12–16  | Randuvil strikes the bandit with the staff (light wound), the bandit flees |
| 17–18  | Randuvil cracks the bandit's head (medium wound), the bandit collapses     |

The roll is 12: the bandit flees wounded. Randuvil stays by the fire at 10%.
