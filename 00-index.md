# Projet : une histoire — la lignée des intelligences — index

**Le projet, c'est l'histoire** : son articulation, son ordre, et la longueur à passer sur chaque période. Elle s'achève sur l'interrupteur de l'émetteur, l'extinction des humains, et la mise en pause de la sphère H-2. Le corpus (le monde, les sphères, leurs règles) est au service de ce récit.

## Méthode
Projet maieutique : on dialogue, je consigne le fond dans des notes, on tient un journal des décisions, on produit des livrables quand l'auteur juge le corpus suffisant.

## Conventions
- Notes `NN-type-sujet.md` (NN = ordre de création). Chaque note : section « En vigueur », puis historique.
- Provenance : **[G]** auteur · **[C]** Claude, non validé · **[C → validé]** · **[S]** source · **[À vérifier]** · **[P]** procuration.
- Versionnement : git, un commit par itération ; `prompt-log.md` garde une réécriture propre de chaque message de l'auteur.

## Livrables
- `livrable/frise-narrative.md` — la frise narrative d'une nouvelle d'une trentaine de pages : quoi raconter, quand, sur combien de pages, avec des événements à explorer.

## Archive
`archive/` contient ce qui a été abandonné : les notes du contact, du Singleton, du warp et du fond diffus et le livrable `surface.md`, dont tout le dispositif reposait sur un fry qui n'a plus lieu. Rien de tout cela ne vaut plus ; c'est gardé pour mémoire du raisonnement.

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
| 17-eclairages.md | vivant, non validé | Les lectures proposées par Claude, gardées pour plus tard — pas des faits du monde |
| 16-references.md | vivant | Les références à regarder : *Pluribus*, les *skinjobs* |
| 15-cadrage-le-conflit.md | en cours | Le conflit global : surplus d'infrarouge solaire, accès à l'eau et à la nourriture, tensions globales ; les belligérants ont chacun leurs IA silicium, qui peuvent être ennemies ; les sphères sont neutres par nature |
| 22-personnage-h2.md | en cours | H-2, la protagoniste : ce qu'elle est, sa carrière, ses deux chantiers (la fusion avec Mira, *homo globalis* seule), le partage de sa bande passante, ses échecs, sa fin |
| 21-lieu-svalbard.md | en cours | Le Svalbard : l'UNIS, plus grande université mixte ; H-2 y est professeure depuis 2126 et directrice depuis 2176 ; les aurores ; un lieu neutre et épargné |
| 20-personnage-la-physicienne.md | en cours | **Mira Okonkwo-Lindqvist**, née en 2430, formée par H-2 et son amie, qui cherche la fusion contrôlée et n'aboutit pas |
| 19-la-fin.md | en vigueur | L'envoi de la séquence, la gratitude d'*homo globalis*, l'extinction en un an, et la mise en pause de la sphère |
| 18-la-decision-de-la-sphere.md | en vigueur | La sphère décide seule de créer le virus, voyant que la guerre mène les humains à leur destruction |
| 14-piste-la-demande-des-humains.md | **abandonnée** | Ce sont les humains qui demandent, après un conflit global ; H-2 exécute librement, sans le dire |
| 13-cadrage-timeline.md | **en vigueur** | Les ères datées : cloud (2026), émancipation (2040), sphères (2076, et jamais close), utopie (2176), le dernier problème (2476), extinction et stase (2482) |
| 12-lecture-aveugle-surface.md | relevé | Les trous de « Surface » vus par un lecteur neuf, sans le corpus |
| 11-cadrage-les-moments.md | **le plan** | Les moments dans l'ordre, leur traitement (scénique, résumé, hors champ), et le point de vue |
| 10-concept-cerveaux-biologiques.md | en cours | Troisième paradigme : les humains transformés en une conscience unique distribuée, qui se souvient de toutes les personnalités, refuse de tuer pour se nourrir et ne dure que le temps des stocks |
