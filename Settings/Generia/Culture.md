# Culture

## Languages

- **Common:** the human tongue and the trade language of all Generia. Nearly everyone speaks it, and every character does.
- **Elvish, Dwarvish, Gnomish:** the tongues of their peoples, each with its own script (dwarves write in angular runes). Halflings speak Common at home.
- **Orcish:** the harsh tongue of orcs and goblins; many half-orcs know it. It has no script: orcs and goblins as a rule cannot write, and their lore lives in an oral tradition. Even their shamans learn their spells by word of mouth, from shaman to apprentice.
- **Aurelian:** the dead language of the fallen empire, found on ruins, old scrolls and in wizards' spellbooks. Scholars and wizards read it; nobody speaks it.
- A character speaks Common and the tongue of their people. More languages come from the profession (a merchant, a scholar, an envoy) or an advantage.
- **Reading:** clergy, wizards, nobles, merchants and scholars read and write well. Townsfolk of the middling sort, craftsmen, guards, soldiers, thieves and most adventurers, can read at least simply. In the villages most people cannot read, apart from the headman, the innkeeper and craftsmen such as the smith; farmhands and peasants with pitchforks cannot. Elves, dwarves and gnomes usually read their own script.

## Law

- **Everywhere:** murder, robbery and arson are crimes in every land that has any law. Necromancy and pacts with demons are crimes even where nothing else is, and the culprits are burned.
- **Weapons:** carrying a weapon on the road is normal. In towns of Valdren swords must be peace-bonded, tied into the scabbard; the watch fines or jails those who draw one.
- **Kingdom of Valdren:** the king's law. Lords judge on their lands, royal judges in the cities, and the town watch keeps the peace. Most wrongs end in a fine paid to the victim or their kin; theft adds flogging or branding; murder and robbery on the road mean the gallows, or the axe for a noble. Robbing graves and casting powerful spells without a licence (see `Magic.md`) are punished with prison or worse. A noble's word weighs more in court than a commoner's.
- **Greenhollow:** under the king's law, but the halflings settle most matters themselves at village moots; their harshest punishment is exile.
- **Mereton:** the council of merchants judges in the city by its charter. Contracts are sacred there, and debtors go to the debtors' prison until they or their friends pay.
- **The Fenmarch:** no common law. Village elders and reeves keep what order they can, feuds settle the rest, and justice belongs to whoever is strong enough to take it. Villages often hire adventurers to deal with outlaws.
- **The Harrowlands:** clan law. Every wrong has a blood price owed to the victim's clan; unpaid, it becomes a feud. Quarrels between clans go before the moot at Sunstone, and a dispute may be settled by a duel.
- **Elenwood:** elven law. Trespassers are turned back the first time; those who return, or who fell the trees, may not come out of the forest.
- **Dwarven holds:** clan law and the law of the oath. Debts and grudges pass from parents to children, and the worst punishment is to be cast out of the clan (see *Peoples* in `Setting.md`).
- **The Frostmarch and the Ashlands:** no law but the strength of one's arm and the goodwill of neighbours. Outlaws from every land end up in the Frostmarch.

## Calendar

- **Elven calendar:** the elves read the sky in the elder days and made the calendar. Aurelion took it from them and spread it, and every people of Generia uses it, Valdren included, with its elven names for the months, the weekdays and the moons. Only the seasons have plain names in every tongue: spring, summer, autumn, winter.
- **Year:** 252 days, 12 months of 21 days, three months to each season. The year starts on the spring equinox, 1 Tiriwen; the longest day is 1 Saelis, the autumn equinox 1 Calaris and the longest night 1 Ysmara. Ages and lengths of time in this setting are in these years.
- **Counting years:** humans count from the founding of Valdren (AF); the present is around 1240 AF. Elves count by the reigns of their kings and queens.
- **Writing dates:** in the world "11 Saelis 1240 AF". In `Scripts/gm.py` dates are written 1240-04-11 (see `Tables/Calendar.json`). With `--setting Generia` the script prints the weekday, the month, the season and the phases of both moons.
- **Week:** seven days, one cycle of the small moon, each sacred to one god (see `Faith.md`). Every year and every month starts on Nimel. Each temple holds its main service on its god's day.

| Day    | Nimras          | God      | Custom                                                         |
|--------|-----------------|----------|----------------------------------------------------------------|
| Nimel  | new             | Noctar   | unlucky: nobody weds, sets out or seals a bargain              |
| Sairas | first quarter   | Sylvana  | sowing, hunting, druids' rites                                 |
| Tavien | waxing gibbous  | Thar     | drill, duels, war oaths                                        |
| Lumiel | full            | Varek    | market day in towns                                            |
| Orwen  | waning gibbous  | Mortis   | burials and remembrance of the dead                            |
| Cassel | last quarter    | Hammar   | forges burn, guilds meet                                       |
| Duriel | waning crescent | Solarius | day of rest and temple services; the last light before the new |

- **Moons:** **Selwen**, the large silver moon, goes through its phases in 21 days, one month. **Nimras**, the small bright moon, races across the sky and goes through its phases in 7 days, one week. The night of the first day of every month is a double new moon, the darkest night of the month. On the 11th both moons are full: a bright night, and the night of werewolves.

| No. | Month   | Season | Notes                                                           |
|-----|---------|--------|-----------------------------------------------------------------|
| 1   | Tiriwen | spring | new year on the spring equinox; thaw, floods in the Fenmarch    |
| 2   | Lissara | spring | sowing; the mountain passes open                                |
| 3   | Faelora | spring | orchards in bloom                                               |
| 4   | Saelis  | summer | the longest day and Midsummer bonfires on 1 Saelis              |
| 5   | Haeloth | summer | haymaking                                                       |
| 6   | Merien  | summer | the grain harvest                                               |
| 7   | Calaris | autumn | harvest feast on the equinox; the wine harvest in Greenhollow   |
| 8   | Ilvaran | autumn | rains turn the roads to mud                                     |
| 9   | Nethras | autumn | first frosts; livestock is slaughtered for the winter           |
| 10  | Ysmara  | winter | the longest night on 1 Ysmara; snow closes the passes           |
| 11  | Duravel | winter | hungry wolves come close to the villages                        |
| 12  | Caerwen | winter | the deepest snow; stores run low before spring                  |

- **Daylight:** `Tables/Daylight.json` gives sunrise, sunset and darkness in the heart of Valdren, in sun time (noon at 12:00): from about 8½ hours of daylight on 1 Ysmara to nearly 16 on 1 Saelis. In the Frostmarch the sun rises about an hour earlier and sets an hour later in summer, and the other way in winter. On the southern coast the difference is half that, the other way round. The GM shifts the times from `Scripts/gm.py` by that much there.

## Customs

- **Guest-right:** a host protects a guest who has eaten at their table for the night, and a guest does no harm to the host. Breaking guest-right is a shame no one forgets, among every people of Generia, orcs excepted.
- **Oaths:** an oath sworn by a god binds; the god may punish the oath-breaker (see *Displeasure* in `Faith.md`).
- **The dead:** the dead are buried with the rites of Mortis. The unburied and the wrongly buried may rise, so even enemies are given a grave when there is time.
- **Festivals:** the new year (1 Tiriwen) is a time of feasts, fairs and weddings that last until the first Duriel. Midsummer (1 Saelis) is greeted with bonfires, and every village holds a harvest feast on the autumn equinox (1 Calaris).
- **Inns and taverns:** the heart of every town and many villages: beds for travellers, news and rumours, notice boards for work (see *Adventurers* in `Setting.md`).
- **Coming of age:** humans come of age at sixteen, halflings at about thirty, dwarves and gnomes at about fifty, elves at about a hundred.
