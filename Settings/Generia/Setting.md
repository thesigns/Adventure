# Generia

Classic fantasy, deliberately generic. Knights and castles, elves in forests, dwarves under mountains, orcs on the borders, wizards in towers, dragons on hoards, taverns at crossroads. Everything is exactly what a player expects from fantasy, and this file only fixes what cannot be guessed.

## Setting files

- `Setting.md`: GM rules, world, peoples, adventurers, organisations and factions, names (this file)
- `Culture.md`: languages, law, calendar and customs
- `History.md`: the Empire of Aurelion, the history of Generia and its present rulers
- `Geography.md`: the continent, climate, mountains, waters, ruins and lands
- `Travel.md`: pace, costs, seasons and dangers of travel
- `Magic.md`: arcane spells, learning them, scrolls and magic items
- `Faith.md`: gods, divine gifts, displeasure and conversion
- `Equipment.md`: money, prices, weapons, armour, light, starting purse
- `Bestiary.md`: monsters and enemies with combat stats
- `Maps/GeneriaMap.svg`: world map, 1 px = 1 km, open to the player (see *Continent* in `Geography.md`)
- `Tables/Calendar.json`: the calendar for `Scripts/gm.py` (see *Calendar* in `Culture.md`)
- `Tables/Daylight.json`: sunrise, sunset and darkness for `Scripts/gm.py`, in the heart of Valdren
- `Tools/`: author's tools, not for play: the map generator (`make_map.py`) and the daylight table generator (`make_daylight.py`)

## GM rules

- **The cliché rule:** whatever the setting does not say, the GM fills with the most typical fantasy convention. When in doubt, pick the obvious option. No subversions, deconstructions or twists on tropes unless a scenario says so.
- Fill in only the world, never the mechanics: no rules or concepts from other RPG systems (classes, levels, armour class, hit points, spell slots).
- Tone: straight adventure fantasy. Danger is real, villains are villainous, heroes can die. Not a parody: names and descriptions are never jokes.
- Magic and monsters are part of the world, but an ordinary peasant meets them rarely. A dragon is still an event.
- Towns, villages, ruins, dungeons, lords and NPCs are invented as scenarios need them. Every new name that may return goes into the campaign log or scenario progress, and the GM checks it there before reuse.

## World

- **Generia:** a small continent of kingdoms, forests, mountains and old ruins, with a European climate. Lands, climate and travel: `Geography.md`.
- **Technology:** high medieval. Swords, crossbows, plate armour, sailing ships. No printing, no gunpowder.
- **Calendar:** 12 months of 30 days plus the 5 festival days of Yearturn, a 7-day week named after the gods. Years counted from the founding of the Kingdom of Valdren (AF, After Founding). Present day: around 1240 AF. Month names, weekdays and festivals: *Calendar* in `Culture.md`. In play the GM sets the clock with `time --setting Generia` (see *GM secrets* in `AGENTS.md`).
- **Evil is scattered:** no single dark lord or great war. Goblins in dungeons, a warlock in his tower, a necromancer raising the dead in a forgotten graveyard, a dragon on its hoard, cultists in the sewers, bandits on the road, the whole menagerie spread across the world. Each threat is local and has its own goals.
- **Culture:** languages, law and customs of the lands: `Culture.md`.
- **Gods:** seven jealous gods, each followed on their own; their clerics and paladins receive divine gifts. Gods, gifts, displeasure and conversion: `Faith.md`.
- **Ruins:** the old Empire of Aurelion fell a thousand years ago and left roads, towers, tombs and dungeons full of treasure and danger. History and present rulers: `History.md`.

## Peoples

A character's species sets the reference point: traits typical of it are not advantages (see `Rules/CharacterCreation.md`). All peoples heal at the same rate as humans (see *Healing* in `Rules/Health.md`).

- **Humans:** the most numerous, live everywhere, do everything. Physically unremarkable, but restless and expansive: they have many children, eagerly explore and settle new lands, which often leads to wars. Natural conquerors.
- **Elves:** live several centuries, slender, graceful. Keen senses, see well in starlight and dim light, move quietly in forests. Skilled trackers and archers, and often mages. Proud and distant towards shorter-lived peoples. Traditionally they keep to the wild forests that once covered most of Generia, and human logging of those forests leads to conflicts. Some elves are restless spirits, though: adventurers, merchants and even bandits.
- **Dwarves:** short, sturdy, bearded, live about three centuries. See well in dim light underground, judge stone, metal and tunnels, tough and stubborn. Strong warriors with axes and hammers despite their height, fine smiths and miners, shrewd merchants and bankers. Hold grudges, love gold, distrust elves. Divided into many clans, most of whom keep to their underground cities. Dwarves in human settlements are usually those who had to or chose to leave their clan: exiles, or those of low standing seeking fame and wealth.
- **Halflings:** half human height, cheerful, love comfort and food. Very nimble, quiet and lucky, and hardy for their size. Good with slings. Traditionally farmers, innkeepers and fishers who rarely leave home. Those who take to the road of adventure are often burglars, pickpockets, scouts, gamblers or travelling cooks and peddlers.
- **Gnomes:** small, quick-witted and endlessly curious, live about four centuries. Keen eyes for detail, good with locks, gears and gems, fond of jokes and pranks. Tinkerers, clockmakers, jewellers, alchemists and illusionists. They often add a pinch of magic to their devices, so many magic items are of gnomish make. Their home is Brasshollow in the western Ironpeaks; elsewhere they live in burrows under quiet hills and as valued craftsmen in dwarven cities and human towns. Their inventions are clever but often unreliable. Those who go adventuring are driven by curiosity rather than gold: explorers, treasure hunters, collectors of curiosities and lore.
- **Half-elves:** rare, because elves seldom bond with humans. Live about two centuries and cannot have children. Exceptionally beautiful, with sharper senses than humans. Live between two worlds and fully belong to neither: elves see them as short-lived, humans as aloof. Often envoys, bards, merchants and wanderers. Those who go adventuring look for a place where they belong: rangers, diplomats, seekers of their elven kin.
- **Half-orcs:** rare, usually born of violence during orc raids. Live a little shorter than humans and cannot have children. Look like plain, coarse humans, so many pass for human. Strong and hardy, they face suspicion everywhere once their blood is known. Raised by human mothers on the fringes, rarely in orc tribes. Labourers, soldiers, guards and bouncers. Those who go adventuring are usually sellswords and mercenaries out to prove themselves, or outcasts with nowhere else to go.
- **Orcs, goblins and their kin:** savage tribes of the wilds: orcs in the Ashlands, goblins (smaller than orcs) in the caves of the Ironpeaks; mostly enemies (see `Bestiary.md`). An orc player character is an exile.

## Adventurers

- **A known trade:** adventurers are sellswords and treasure hunters who clear ruins and dungeons, hunt monsters, escort caravans and take the jobs nobody else wants. Commoners admire and distrust them in equal measure; lords hire them and look down on them.
- **Adventurers' Guild:** guild halls in the bigger cities (Kingsbridge, Mereton, Silverhaven, Port Seravel) register adventurers, post contracts and vouch for both sides for a tenth of the pay. Joining is cheap; many adventurers never bother.
- **Where work comes from:** notice boards in taverns and town halls, lords, merchants and temples, bounties on monsters and outlaws, and rumours of treasure heard over ale. The tavern is where adventures start.
- **Pay:** guard or escort work about 5 s a day; clearing a cellar of vermin 1 g; a goblin lair 10–30 g; a troll or a band of outlaws 50–100 g; anything worse is negotiated. Treasure is usually worth more than the pay.
- **Loot:** whatever is found in ancient ruins and monster lairs belongs to the finder. Robbing the graves of known families, temples or a lord's land is a crime.
- **Parties:** most adventurers work in small bands of three to six; a lone adventurer is unusual but not rare.
- **Hirelings:** porters, torchbearers, guides and men-at-arms are hired in any town or tavern; pay in `Equipment.md`, rules in `Rules/Companions.md`. They do not go into ruins and lairs for ordinary pay: double pay or a share is the custom there.

## Organisations and factions

Every faction is what it looks like (see *The cliché rule*). Each can be an employer, an ally or an enemy, depending on what the character does.

- **Temples:** every god has its own temple with a high priest in Kingsbridge, priests in the towns and shrines in the villages (see `Faith.md`). The temple of Solarius is the richest and the closest to the crown. Temples hire adventurers against undead, cults and desecrators of graves, and heal for a donation.
- **Order of the Dawn:** knights and paladins of Solarius, with their chapter house in Kingsbridge and commanderies across Valdren. They hunt undead, necromancers and the cults of Noctar, and they judge harshly.
- **Gravewardens:** the brotherhood of Mortis's priests and undertakers. They tend graveyards, bury the dead with the proper rites and put the restless dead to rest. They pay well for news of open graves and risen dead.
- **Shield of the East:** the knightly order of Thar at Port Seravel and along the Vael. Fights orc raiders beside the Harrowland clans and hires sellswords when raids grow bold.
- **Arcane College:** the school of wizards in Kingsbridge, ruled by the Archmagister and a council of masters. It trains and licenses wizards, buys old books and Aurelian relics, and its Seekers hunt unlicensed sorcerers and necromancers in Valdren (see `Magic.md`).
- **Adventurers' Guild:** halls in the big cities, contracts and the guild's word for a tenth of the pay (see *Adventurers*).
- **Merchant houses:** human families of Mereton and Kingsbridge, the merchant council of Mereton and the dwarven bankers, who lend gold under oath to anyone with a pledge. They hire guards for caravans and adventurers to recover stolen goods.
- **Tinkers' Guild of Brasshollow:** the gnomish craft guild that makes and sells clockwork and magic items; its masters always want rare gems, metals and old Aurelian devices.
- **Thieves' guilds:** each big city has one, under the quiet patronage of Varek: the Quiet Hands in Kingsbridge, the Lantern Men in Mereton, the Saltmen in the ports. They take a cut of every theft, smuggling and fence in their city, and punish thieves who work without leave.
- **Cults of Noctar:** secret cells in the cities and lonely manors, led by warlocks and necromancers, seeking the forbidden lore of Aurelion, eternal life and power over the dead. Hunted by every temple and every law.
- **Circles of Sylvana:** druids of the wild forests. Many side with the elves against the settlers of the Fenmarch.
- **The royal court:** the lords of Valdren split between Prince Aldric, the soldier, and Princess Isolde, the clever one, with the old king between them (see *The present* in `History.md`). Each side gathers friends and quietly hires those who can do what knights cannot.
- **Queen's Wardens:** elven rangers of Elenwood, who turn trespassers back and watch the Fenmarch's edge (see *Law* in `Culture.md`).
- **Outlaw bands:** in the forests of Valdren, the Fenmarch and the Frostmarch; bounties for them are posted in the towns.

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
