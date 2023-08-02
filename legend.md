Legend for files

Default names: recipe|crafter.path.name

Duration format: (0<?)d(0<?<24)h(0<?<60)m(float<60)s (0 are NOT needed)

Speed format: x?

-------------------------------------------

Recipe format (name.recipe) :

Name: \<name to show when printing (if missing it will be the path to the file)\>

Description: \<description to show when using help on the recipe (if missing a default will appear describing the craft)\>

Ressources: \<ressources needed to do the craft (if missing it is considered free)\>

Result: \<ressources given when the craft is finished (if missing it is considered as a void recipe)\>

Crafter: \<machine needed to make\\accelerate the craft (if missing only the ressources are needed)\>

Crafter needed: <True/False (false if missing)>

Duration: \<duration of the craft (if missing it is instant)\>

-------------------------------------------

Crafting system format (name.crafter) :

Name: \<name to show when printing (if missing it will be the path to the file)\>

Description: \<description to show when using help on the crafter (if missing a default will appear describing the craft)\>

Ressources: \<ressources needed to add to each of the craft using it (if missing it is ignored)\>

Result: \<ressources given for each finished craft (if missing it is ignored)\>

Crafter: \<other machines needed to accelerate the craft (if missing it is ignored)\>

Speed: \<speed multiplier of the crafts (if missing it is x1)\>