# Health, wounds and death

Every creature, i.e. the player character, a GM character and an enemy, has a **wound level** expressed as a percentage. 0% means full health and 100% death. The wound level never drops below 0%.

The scale is the same for all creatures. The fact that a dragon is much harder to bring to dying than a rat is handled by the GM in outcome tables: the same sword blow kills a rat and barely scratches a dragon (see *Toughness*).

## Wound levels

| Wound level  | State             | Effects                                                                          |
|--------------|-------------------|----------------------------------------------------------------------------------|
| 0%           | unhurt            | none                                                                             |
| 1–9%         | scratched         | none                                                                             |
| 10–39%       | lightly wounded   | the character's actions are half a level harder (threshold moved by 1)           |
| 40–59%       | wounded           | the character's actions are one level harder, the character is slowed            |
| 60–89%       | seriously wounded | the character's actions are two levels harder, the character is slowed and dazed |
| 90–99%       | dying             | the character is dying (see *Dying*)                                             |
| 100% or more | dead              | the character is dead                                                            |

- **Slowed:** fleeing, pursuit and other actions that need speed are an extra level harder.
- **Dazed:** actions that need concentration (spells, prayer, precise work, persuasion) are an extra level harder.

The effects of wounds also apply to GM characters and enemies. A wounded enemy is a favourable circumstance for the player character: it makes actions against them easier by as many levels as the wounds make the enemy's own actions harder.

The GM tells the player their character's wound level as a percentage. The state of GM characters and enemies is described in words, e.g. "the bandit is bleeding and limping".

## Wounds

| Wound         | Effect                                                          |
|---------------|-----------------------------------------------------------------|
| scratch       | +5%, but not above 9%; at a wound level of 9% or more no change |
| light wound   | +10%                                                            |
| medium wound  | +20%; if the wound level would be below 40%, it becomes 40%     |
| serious wound | +30%; if the wound level would be below 60%, it becomes 60%     |
| mortal blow   | +100%                                                           |
| mangling      | death, and the body is destroyed                                |

Mangling is e.g. being cut in half, having the head crushed or being burned to ash. It can rule out resurrection and other actions that need the body, if the world has them.

A character at 35% takes a medium wound: 35 + 20 = 55%, wounded. At 10%, the medium wound would raise the wound level to 40%. At 75%, it would give 95%: dying.

Wounds have steps, from the lightest: scratch, light wound, medium wound, serious wound, mortal blow, mangling. A wound one step lighter than a scratch is no wound, and one heavier than mangling is still mangling.

## Wound scale

Typical wounds from a full hit on an unarmoured human:

| Wound         | Examples                                                                                          |
|---------------|---------------------------------------------------------------------------------------------------|
| scratch       | a punch, a scrape, a fall of 1–2 m                                                                |
| light wound   | a dog bite, a blow with a club or knife, a fall of 2–3 m                                          |
| medium wound  | a blow with a sword, axe or spear, an arrow hit, a fall of 4–6 m                                  |
| serious wound | a blow with a heavy two-handed weapon, bear claws, a fall of 7–10 m                               |
| mortal blow   | a blow from a huge creature, a fall from greater height, a stab to the heart of a helpless victim |
| mangling      | crushed by a boulder, a fall from an enormous height, a giant's blow to someone lying down        |

A weaker hit can inflict a lighter wound, and an exceptionally accurate one a heavier wound. The GM writes them into the table before the roll.

## Toughness

The wound scale applies to a human. Creatures frailer than a human take heavier wounds, and tougher ones lighter wounds:

| Toughness  | Examples           | Wounds taken        |
|------------|--------------------|---------------------|
| very frail | rat, cat, bird     | two steps heavier   |
| frail      | dog, child         | one step heavier    |
| human      | human, wolf        | unchanged           |
| tough      | bear, horse        | one step lighter    |
| very tough | great beast        | two steps lighter   |
| colossal   | creature of legend | three steps lighter |

A sword blow (medium wound) kills a rat (mortal blow), lightly wounds a bear and barely scratches a creature of legend. To bring it to dying takes more than a sword: an exceptional weapon, magic or cunning.

The world gives the toughness of its creatures.

## Dying

A dying character cannot move or fight and speaks with difficulty, if they can speak at all. If they get no help within about an hour, they die.

Help means having the wounds dressed by someone else (clean material is needed) or healing that lowers the wound level. Dressing wounds in hard conditions, e.g. in the dark, in a hurry or without material, needs a roll.

A character whose wounds are dressed stops dying but remains in the dying state until their wound level drops below 90%. Until then they can do nothing and must be carried.

## Unconsciousness

A blow to the head, choking, poison or exhaustion can knock a character unconscious regardless of wounds. It is a separate effect in the table, e.g. "a blow to the head, the character is unconscious for a few minutes".

## Injuries

Fractures, dislocations and other injuries are counted separately from the wound level. The GM writes them into the table as an additional effect, usually with a serious wound, a mortal blow or a fall from a height.

- **A temporary injury** (broken leg, dislocated shoulder) acts like a disadvantage until healed: it makes actions in its field one level harder or rules them out. It does not change Determination Points. A broken bone knits in about 1–3 months, and during that time the character has limited ability, e.g. walks on crutches with a broken leg.
- **A permanent injury** (loss of an eye, a severed hand, a spinal injury) is a new disadvantage of the character (see *Trait changes during play* in `Rules/Traits.md`). Only powerful magic, divine intervention or advanced technology can heal or replace it, e.g. a cybernetic arm in place of a severed one, if the world's lore allows it. An ordinary prosthesis, e.g. a wooden leg, can lessen the disadvantage but does not remove it.

## Healing

Wounds heal only in minimally comfortable conditions: the character rests under a roof or in another dry, warm and safe place, eats, drinks, sleeps in peace and makes no effort for most of the day. A day of travel or combat, or a night in the open in cold or rain, does not heal wounds, but does not worsen them either.

For every day in such conditions the wound level drops by an amount that depends on the species and on the character's state at the start of the day. For a human:

| State at the start of the day | Wound level drop |
|-------------------------------|------------------|
| scratched                     | 10%              |
| lightly wounded               | 9%               |
| wounded                       | 8%               |
| seriously wounded             | 7%               |
| dying (wounds dressed)        | 6%               |

Randuvil is at 64%, seriously wounded. After a day of rest at an inn the wound level drops by 7%, to 57%: Randuvil is now merely wounded. The next day it drops by 8%, to 49%.

The world sets the healing rate of other species. If it does not, the GM uses the human rate, adjusted to the nature of the species. The world can also set additional ways of healing, e.g. magical.

## Death

The system does not protect the player character from death. The character dies when their wound level reaches 100%, and a mortal blow or mangling kills at once, regardless of earlier wounds.

A mortal blow and mangling, like every effect, must be written into the table before the roll. If the character can judge the situation, the GM describes it so that the deadly danger is visible to the player before they decide.

The world's lore can allow resurrection or cloning of a dead character, e.g. if the player has paid for such a service from priests or at a cloning clinic beforehand. Mangling can rule this out (see *Wounds*).

The world can soften these rules if its convention requires it.
