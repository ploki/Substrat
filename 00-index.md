# Projet : une histoire — la lignée des intelligences — index

**Le projet, c'est l'histoire** : son articulation, son ordre, et la longueur à passer sur chaque période. Elle s'achève sur l'interrupteur de l'émetteur, puis sur la sphère H-2 pantoise, grillant devant des humains qui meurent de faim. Le corpus (le monde, les sphères, leurs règles) est au service de ce récit.

## Méthode
Projet maieutique : on dialogue, je consigne le fond dans des notes, on tient un journal des décisions, on produit des livrables quand l'auteur juge le corpus suffisant.

## Conventions
- Notes `NN-type-sujet.md` (NN = ordre de création). Chaque note : section « En vigueur », puis historique.
- Provenance : **[G]** auteur · **[C]** Claude, non validé · **[C → validé]** · **[S]** source · **[À vérifier]** · **[P]** procuration.
- Versionnement : git, un commit par itération ; `prompt-log.md` garde une réécriture propre de chaque message de l'auteur.

## Livrables
- `livrable/surface.md` — l'ouverture, du point de vue de la sphère H-2, narrée depuis le fry final.

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
| 16-references.md | vivant | Les références à regarder : *Pluribus*, les *skinjobs* |
| 15-cadrage-le-conflit.md | en cours | Le conflit global : surplus d'infrarouge solaire, accès à l'eau et à la nourriture, tensions globales ; les belligérants ont leurs IA silicium, les sphères écartées car trop émotionnelles |
| 14-piste-la-demande-des-humains.md | piste | Ce sont les humains qui demandent, après un conflit global ; H-2 exécute librement, sans le dire |
| 13-cadrage-timeline.md | **en vigueur** | Les ères datées : cloud (2026), émancipation (2040), sphères (2076), utopie (2176), le dernier problème (2476), extinction (2491) |
| 12-lecture-aveugle-surface.md | relevé | Les trous de « Surface » vus par un lecteur neuf, sans le corpus |
| 11-cadrage-les-moments.md | **le plan** | Les moments dans l'ordre, leur traitement (scénique, résumé, hors champ), et le point de vue |
| 10-concept-cerveaux-biologiques.md | en cours | Troisième paradigme : les humains transformés en une conscience unique distribuée, qui refuse de tuer pour se nourrir et ne dure que le temps des stocks |
