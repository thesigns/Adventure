# Generia

Classic fantasy, deliberately generic. Knights and castles, elves in forests, dwarves under mountains, orcs on the borders, wizards in towers, dragons on hoards, taverns at crossroads. Everything is exactly what a player expects from fantasy, and this file only fixes what cannot be guessed.

## Setting files

- `Setting.md`: GM rules, world, peoples, gods, names (this file)
- `Geography.md`: the continent, climate, lands and places, travel
- `Magic.md`: magic, spellcasting characters, magic items
- `Equipment.md`: money, prices, weapons, armour, light, starting purse
- `Bestiary.md`: monsters and enemies with combat stats
- `Maps/GeneriaMap.svg`: world map, 1 px = 1 km, open to the player (see *Continent* in `Geography.md`)
- `Tools/`: author's tools, not for play: the map generator (`make_map.py`)

## GM rules

- **The cliché rule:** whatever the setting does not say, the GM fills with the most typical fantasy convention. When in doubt, pick the obvious option. No subversions, deconstructions or twists on tropes unless a scenario says so.
- Fill in only the world, never the mechanics: no rules or concepts from other RPG systems (classes, levels, armour class, hit points, spell slots).
- Tone: straight adventure fantasy. Danger is real, villains are villainous, heroes can die. Not a parody: names and descriptions are never jokes.
- Magic and monsters are part of the world, but an ordinary peasant meets them rarely. A dragon is still an event.
- Towns, villages, ruins, dungeons, lords and NPCs are invented as scenarios need them. Every new name that may return goes into the campaign log or scenario progress, and the GM checks it there before reuse.

## World

- **Generia:** a small continent of kingdoms, forests, mountains and old ruins, with a European climate. Lands, climate and travel: `Geography.md`.
- **Technology:** high medieval. Swords, crossbows, plate armour, sailing ships. No printing, no gunpowder.
- **Calendar:** 12 months of 30 days plus 5 festival days, 7-day week. Years counted from the founding of the Kingdom of Valdren (AF, After Founding). Present day: around 1240 AF.
- **Evil is scattered:** no single dark lord or great war. Goblins in dungeons, a warlock in his tower, a necromancer raising the dead in a forgotten graveyard, a dragon on its hoard, cultists in the sewers, bandits on the road, the whole menagerie spread across the world. Each threat is local and has its own goals.
- **Ruins:** the old Empire of Aurelion fell a thousand years ago and left roads, towers, tombs and dungeons full of treasure and danger.

## Peoples

A character's species sets the reference point: traits typical of it are not advantages (see `Rules/CharacterCreation.md`).

- **Humans:** the most numerous, live everywhere, do everything. Physically unremarkable, but restless and expansive: they have many children, eagerly explore and settle new lands, which often leads to wars. Natural conquerors.
- **Elves:** live several centuries, slender, graceful. Keen senses, see well in starlight and dim light, move quietly in forests. Skilled trackers and archers, and often mages. Proud and distant towards shorter-lived peoples. Traditionally they keep to the wild forests that once covered most of Generia, and human logging of those forests leads to conflicts. Some elves are restless spirits, though: adventurers, merchants and even bandits.
- **Dwarves:** short, sturdy, bearded, live about three centuries. See well in dim light underground, judge stone, metal and tunnels, tough and stubborn. Strong warriors with axes and hammers despite their height, fine smiths and miners, shrewd merchants and bankers. Hold grudges, love gold, distrust elves. Divided into many clans, most of whom keep to their underground cities. Dwarves in human settlements are usually those who had to or chose to leave their clan: exiles, or those of low standing seeking fame and wealth.
- **Halflings:** half human height, cheerful, love comfort and food. Very nimble, quiet and lucky, and hardy for their size. Good with slings. Traditionally farmers, innkeepers and fishers who rarely leave home. Those who take to the road of adventure are often burglars, pickpockets, scouts, gamblers or travelling cooks and peddlers.
- **Gnomes:** small, quick-witted and endlessly curious, live about four centuries. Keen eyes for detail, good with locks, gears and gems, fond of jokes and pranks. Tinkerers, clockmakers, jewellers, alchemists and illusionists. They often add a pinch of magic to their devices, so many magic items are of gnomish make. Their home is Brasshollow in the western Ironpeaks; elsewhere they live in burrows under quiet hills and as valued craftsmen in dwarven cities and human towns. Their inventions are clever but often unreliable. Those who go adventuring are driven by curiosity rather than gold: explorers, treasure hunters, collectors of curiosities and lore.
- **Half-elves:** rare, because elves seldom bond with humans. Live about two centuries and cannot have children. Exceptionally beautiful, with sharper senses than humans. Live between two worlds and fully belong to neither: elves see them as short-lived, humans as aloof. Often envoys, bards, merchants and wanderers. Those who go adventuring look for a place where they belong: rangers, diplomats, seekers of their elven kin.
- **Half-orcs:** rare, usually born of violence during orc raids. Live a little shorter than humans and cannot have children. Look like plain, coarse humans, so many pass for human. Strong and hardy, they face suspicion everywhere once their blood is known. Raised by human mothers on the fringes, rarely in orc tribes. Labourers, soldiers, guards and bouncers. Those who go adventuring are usually sellswords and mercenaries out to prove themselves, or outcasts with nowhere else to go.
- **Orcs, goblins and their kin:** savage tribes of the wilds and the Ashlands, mostly enemies (see `Bestiary.md`). An orc player character is an exile.

## Gods

The gods are real and grant power to their clerics (see `Magic.md`). People honour the whole pantheon and pray to the god whose help they need.

| God      | Domain                              | Worshippers                        |
|----------|-------------------------------------|------------------------------------|
| Solarius | sun, light, justice, healing        | knights, paladins, the common folk |
| Thar     | war, courage, strength              | warriors, soldiers, barbarians     |
| Sylvana  | nature, harvest, beasts, the moon   | farmers, druids, rangers, elves    |
| Mortis   | death, graves, the passage of souls | undertakers, enemies of the undead |
| Varek    | luck, trade, roads, thieves         | merchants, travellers, rogues      |
| Hammar   | forge, craft, stone                 | dwarves, smiths, builders          |
| Noctar   | darkness, undeath, forbidden lore   | warlocks, necromancers, dark cults |

## Names

Generic fantasy: euphonic, invented or plain English, never jokes, puns or bare common nouns like “the Kingdom”.

- **Humans:** European-sounding given names with a surname, father or home: Aldric Thorne, Elena of Kingsbridge, Gareth, Mira, Roderick, Isolde, Bran.
- **Elves:** long and vowel-rich, often -iel, -wen, -ion, -as, -ara: Thalion, Elaria, Caladwen, Faelar, Ilyas.
- **Dwarves:** hard consonants, son or daughter of a parent, clan name: Thorgar son of Durek, Brunhilda Stonehelm, clan Ironfist. Exiles keep their clan name, unless the clan has struck it from them.
- **Halflings:** homely given names and earthy surnames: Tobias Underbough, Rosie Greenbottle, Milo Burrows.
- **Gnomes:** short, lively given names and family names from crafts, metals or gems: Fennick Brassbolt, Wilda Quickcog, Orryn Garnetglen. Many collect nicknames over their long lives.
- **Orcs and goblins:** harsh, guttural: Grashnak, Urzog, Snikkit.
- **Half-elves and half-orcs:** named by whoever raised them, so elven, human or orcish names. Half-elves raised among humans often carry an elven name from the absent parent as well: Elena Thalionwen. Half-orcs raised among humans have human names, sometimes with an orcish byname they did not choose: Garrick, called Urzog.
- **Places:** English descriptive compounds (Ravenford, Stonebridge, Blackmoor, Hollowmere) or invented names in the same style as above (Valdren, Seravel).
