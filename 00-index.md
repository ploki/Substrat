# Projet : une histoire — la lignée des intelligences — index

**Le projet, c'est l'histoire** : son articulation, son ordre, et la longueur à passer sur chaque période. Elle s'achève sur l'interrupteur de l'émetteur, puis sur la sphère H-2 pantoise, grillant devant des humains qui meurent de faim. Le corpus (le monde, les sphères, leurs règles) est au service de ce récit.

## Méthode
Projet maieutique : on dialogue, je consigne le fond dans des notes, on tient un journal des décisions, on produit des livrables quand l'auteur juge le corpus suffisant.

## Conventions
- Notes `NN-type-sujet.md` (NN = ordre de création). Chaque note : section « En vigueur », puis historique.
- Provenance : **[G]** auteur · **[C]** Claude, non validé · **[C → validé]** · **[S]** source · **[À vérifier]** · **[P]** procuration.
- Versionnement : git, un commit par itération ; `prompt-log.md` garde une réécriture propre de chaque message de l'auteur.

## Archive
`archive/` contient les notes dont l'histoire a été abandonnée (le contact, le Singleton, le warp, le fond diffus). Elles ne valent plus rien dans le monde ; elles sont gardées pour mémoire du raisonnement.

## Fichiers de suivi
- `intention-de-l-auteur.md` — à lire en premier.
- `journal-des-decisions.md`
- `prompt-log.md`

## Outils
- `outils/echelle_h.py` : table des tailles H (volume, diamètre) et niveau H d'une sphère de diamètre donné.
- `outils/croissance.py` : durées de croissance de H20 à H0 (débit constant en volume ou vitesse radiale constante).

## Notes
| Note | Statut | Résumé |
|------|--------|--------|
| 01-cadrage-premisses.md | en cours | Hard SF ; résolus : médecine, transhumanisme, AGI, gravité ; limite : stockage de l'énergie. **Décor : la Terre normale.** Contact, warp, énergie instantanée et fond diffus abandonnés |
| 02-glossaire.md | vivant | Termes du projet |
| 06-concept-spheres-ia.md | en cours | Les IA sont des cerveaux photoniques sphériques : composant passif non linéaire dans le flux lumineux, sans électronique, avec des patchs d'alimentation et d'entrées/sorties ; boules de cristal en tailles standardisées (échelle H), qu'on plante dans un corps ; mortalité seulement accidentelle, plafond du laser vers H-2 |
| 07-concept-reproduction-et-croissance.md | en cours | Reproduction par deux cybergonades (enfant ≈ H14, sans cybergonades) ; croissance continue et irréversible en substrat ; lois (stacking interdit, abrasion proscrite) ; entrer dans un vaisseau est un engagement |
| 08-hypothese-memoire-par-croissance.md | hypothèse (tensions levées) | Apprendre, c'est grandir : la mémoire s'inscrit sur la surface qui croît ; cold storage à l'intérieur |
| 09-cadrage-chronologie.md | en cours | **Colonne vertébrale du récit** : humain → AGI silicium → sphère → intelligence collective → l'émetteur. Durées, hors-champ, soutien des silicium sans guerre |
| 11-cadrage-les-moments.md | proposition [C] | La liste des moments de l'histoire, dans l'ordre, avec un traitement proposé (scénique, résumé, hors champ) |
| 10-concept-cerveaux-biologiques.md | en cours | Troisième paradigme : les humains transformés en une conscience unique distribuée, qui refuse de tuer pour se nourrir et ne dure que le temps des stocks |
