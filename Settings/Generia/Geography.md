# Geography

The map `Maps/ElandriaMap.svg` is the source of truth; this file describes what is on it.

## World and continent

- **Generia:** the world, a planet like ours with two moons (see *Calendar* in `Culture.md`). Scholars know it is round. Sailors tell of other lands beyond the seas, but nobody has charted them; Elandria is the only continent anyone knows.
- **Elandria:** the continent where the setting takes place. The name is elven, spread across the land by Aurelion like the calendar, and every people uses it. A small continent in the northern hemisphere, about the size of Australia: roughly 3,500 km west to east and 2,500 km north to south. An irregular shape: a long north-western coast running north-east, a large peninsula in the north-east, a broad western lobe, seven islands offshore, and about seventy small islands scattered in groups in the southern sea between Silverhaven and Port Seravel, like the Aegean, with a handful more off the coast between Brenwick and Silverhaven.
- **Climate** as in Europe, by latitude. The southern coast is warm like southern Italy and Spain: hot dry summers, mild wet winters. The centre is temperate like France or Germany. The north beyond the Ironpeaks is cool like the lands around Oslo: long snowy winters, short summers, long summer days and short winter ones. Seasons and daylight follow the same latitudes, but the year is shorter: 252 days, 63 to a season (see *Calendar* in `Culture.md`).
- **Map:** 1 px = 1 km, north up, x grows east and y south. The `<desc>` at the top of the file lists every place with its coordinates and every road and river with its length, so the GM can read distances there without parsing the drawing. Rivers, lakes, forests, mountain ranges and lands carry their names in `data-name`, rivers their length in km in `data-km`, ranges their ridge line in `data-ridge`. Lands without a drawn border have an invisible outline `region-<name>`. The map shows only what everyone knows, so the player may see it in full.
- **Travel:** pace, costs, seasons and dangers on the way: `Travel.md`.
- **What the map leaves out:** it shows only the main places. Elandria has dozens of towns and hundreds of villages, ruins, crypts, towers and dungeons that are not on it; the GM places them as scenarios need, fitting the land, and records them in the campaign log. How densely the lands are settled:
  - Valdren and Greenhollow: a village every few to a dozen kilometres, a market town every day or two of travel,
  - the Fenmarch and the Harrowlands: scattered villages and farmsteads, several days between towns,
  - the Frostmarch: lone settlements, often a week apart,
  - Elenwood: hidden elven halls, found only with the elves' leave,
  - the Ashlands: orc camps and nothing else.

## Mountains

- **Ironpeaks:** the great range of young, high and jagged mountains. It runs from the west across the middle of the continent and bends north-east, with many spurs on both sides. Home of the dwarven clans. Their great hold is Khaz Dorun, high in the middle of the range where it bends north-east; Durnhold is a smaller hold on the northern slopes, above the Frostmarch. The gnomes' home is Brasshollow, a warren of workshops in the western Ironpeaks, north of Elenwood. Goblin tribes, smaller than orcs, swarm in caves throughout the range and raid dwarves, gnomes, mountain villages and travellers.
- **Crookback Mountains:** the second range, in the east, running from north-west to south-east down to the eastern coast. Far older than the Ironpeaks, lower and worn into bare ridges. A valley separates it from the Ironpeaks; it is the main way between the Harrowlands and the Ashlands, guarded by the clan fort of Ashgate. Over the range itself leads Crow's Pass, the only pass worth the name.

## Waters

- **Silvermere:** the largest lake, at the southern foot of the Ironpeaks, so wide that on a grey day the far shore cannot be seen. Fed by the Highrun and the Aldwater, drained by the Silverrun to the southern sea. Storms come quickly, and the deep water is said to hide things older than Aurelion.
- **Mistmere and Reedmere:** two smaller lakes west of Silvermere. The Mistbrook and the Reedbrook flow into them from the mountains; the Brenna drains Mistmere and the Wend drains Reedmere to the southern sea.
- **Vael:** the longest river, from the Ironpeaks south-east to the eastern coast. It is the border between Valdren and the Harrowlands.
- **Kingswater:** a tributary of the Vael, from the foot of the Ironpeaks through Kingsbridge.
- **Aelwen:** from the Ironpeaks through Elenwood to the south-western coast.
- **Coldwater and Frostrun:** short rivers flowing north from the Ironpeaks through the Frostmarch to the northern coast.

## Ruins of Aurelion

The Empire of Aurelion fell a thousand years ago. Its ruins are scattered across Elandria, full of treasure and danger; the best known are on the map:

- **Aurelion:** the ruined imperial capital, deep in the Ashlands. Orcs camp in its shadow but avoid its halls.
- **Drowned Spires:** towers sinking into the Fenmarch marshes, between Mistmere, Reedmere and the sea.
- **Hollow Crown:** a ring of broken halls on a hill in the western Frostmarch.
- **Lonely Tower:** a tower on an island off the north-western coast.
- **Sunstone:** a fallen temple of the sun in the Harrowlands, where the clans hold their moots.

## Lands

- **Kingdom of Valdren:** the human heartland, between Silvermere, the Silverrun and the Aldwater in the west and the Vael in the east, from the Ironpeaks down to the southern coast. King, nobles, knights, peasants. Capital: Kingsbridge, in the north of the kingdom on the Kingswater, just south of Fernwood, near the Vael and the mountains. Ports: Silverhaven at the mouth of the Silverrun and Port Seravel at the mouth of the Vael, the kingdom's gate to the sea and to the Harrowlands; roads lead to both. Second city: Mereton, on the north-eastern shore of Silvermere at the mouth of the Aldwater, the last bastion of civilisation before the Fenmarch. Goods from the mountains come down the Aldwater and spread by boat across the lake and into the Fenmarch. A merchant city with a royal charter, governed by a council of merchants, where traders, adventurers and Fenmarch folk mix with royal officials. Forests: Blackwood, Fernwood, Hartwood and smaller woods.
- **Alderwick:** a lake port of Valdren on the eastern shore of Silvermere, west of the northern tip of Alderwood, a short way above the source of the Silverrun. Every boat between Mereton and Silverhaven stops here: barges cross the lake from Mereton, and here goods are moved onto river boats for the Silverrun, or onto carts for the road east to Hartwell. Boatmen, fishers, rope-walks and boatyards; lake pilots who read Silvermere's sudden storms; a shrine of Varek on the quay. Fishers tell of nets torn by something in the deep water, and nobody laughs at them.
- **Crossholt:** a town of Valdren where the road from Mereton meets the road south from Kingsbridge, at the western edge of Hartwood, about 115 km from the capital. Every main road from the south and the west runs through it, so it is the last stop before Kingsbridge: big coaching inns, warehouses, carters and caravan masters hiring guards for the way back. A royal customs post checks goods bound for the capital, and the town watch peace-bonds swords from here on. Highwaymen caught on the roads hang on the gallows at the crossroads.
- **Hartwell:** a small market town of Valdren at the crossroads where the road from Port Seravel meets the road from Kingsbridge to Hollowbury, at the southern end of Hartwood, about 230 km from Kingsbridge. Named for the deep well in its square, older than the town, with a shrine of Varek beside it where travellers drop a copper for luck on the road. It lives off the crossroads: coaching inns, stables and wheelwrights, a royal toll, and a cattle market on Duriel, where Harrowland drovers sell herds bound for Kingsbridge and halfling carters from Greenhollow bring wine and cheese. Hartwood is the king's hunting forest, and the royal foresters who guard its deer live in the town; poachers are branded.
- **Greenhollow:** halfling land in the south of Valdren, under the king. Low, grassy glacial hills, fertile and tilled: fields, orchards, vineyards and small woods between them. The main town is Hollowbury, at the end of the road from Kingsbridge, west of Hazelwood.
- **Applecombe:** the second halfling town of Greenhollow, in its western hills, halfway along the road from Hollowbury to Silverhaven. A town of orchards and cider: apple trees on every slope, cider presses and cellars dug into the hillsides, and a cider fair after the harvest feast in Calaris, when carts loaded with barrels set off for the port. Halfling families have run its inns and orchards for generations; its moot settles disputes, and the human carters and Silverhaven merchants who come for the cider are welcome as long as they mind halfling manners.
- **The Fenmarch:** the frontier west of Valdren, the river lands of Mistmere and Reedmere and the rivers flowing into and out of the lakes, from the Ironpeaks to the southern coast. Forests (Silverwood, Southwood), marshes and rivers. Independent villages and small towns, not part of Valdren, where humanity pushes west. Brenwick, a small port at the mouth of the Brenna, is the frontier's door to the sea. The marshes hide will-o'-wisps, bog hags, lizardfolk and the drowned dead.
- **Elenwood:** the great primeval forest in the west, the largest remnant of the forests that once covered Elandria, the realm of the wood elves. Outsiders enter only with permission. The elves' chief seat is Aelindor, on the eastern bank of the Aelwen in the heart of the forest. Highwood, under the Ironpeaks north of Silvermere, is a smaller forest east of it.
- **The Harrowlands:** between the Vael and the Crookback Mountains. Not a kingdom but a loose bond of clans, each led by a chieftain; in war the clans elect a war-chief at a moot. Herders, hunters and sellswords, hard and plain people used to hardship, among them many half-orcs, who are equals here as nowhere else. They guard the way through Ashgate and Crow's Pass against the orcs of the Ashlands. Valdren sees them as savages but gladly hires their warriors.
- **Ashlands:** blasted wastes beyond the Crookback Mountains, up to the north-eastern coast and its peninsula, roamed by orc tribes. Orc raids come through the valley by Ashgate and over Crow's Pass.
- **Frostmarch:** the cold north beyond the Ironpeaks, between the mountains and the northern coast, with coniferous forests (Coldpines, Frostwood). Few people and scattered settlements of humans and elves, dwarven holds on the northern slopes of the Ironpeaks, no halflings. A refuge for outlaws and exiles from every land.
