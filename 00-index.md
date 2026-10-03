# Projet : construction d'un monde (personnages, lieux, cultures) et de ses aventures — index

## Méthode
Projet maieutique : on dialogue, je consigne le fond dans des notes, on tient un journal des décisions, on produit des livrables quand l'auteur juge le corpus suffisant.

## Conventions
- Notes `NN-type-sujet.md` (NN = ordre de création). Chaque note : section « En vigueur », puis historique.
- Provenance : **[G]** auteur · **[C]** Claude, non validé · **[C → validé]** · **[S]** source · **[À vérifier]** · **[P]** procuration.
- Versionnement : git, un commit par itération ; `prompt-log.md` garde une réécriture propre de chaque message de l'auteur.

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
| 01-cadrage-premisses.md | en cours | Hard SF, cinq domaines résolus (médecine, transhumanisme, warp, AGI, gravité), premier contact ; limite : stockage de l'énergie ; énergie transmise instantanément |
| 02-glossaire.md | vivant | Termes du projet |
| 03-concept-singleton.md | en cours | Le Singleton, unique, conquis : une intelligence sphérique, référence causale ultime (fond diffus compris) ; le warp échange distance au Singleton contre temps |
| 04-concept-physique-du-warp.md | proposition [C] | Formalisation u = t − r/c : surfaces nulles, causalité préservée, warp latéral instantané |
| 05-concept-code-et-interface.md | en cours | L'AGI, le code sphérique optimal, le fond diffus comme interface vers le contenu du Singleton |
| 07-concept-reproduction-et-croissance.md | en cours | Reproduction par deux cybergonades (enfant ≈ H14, sans cybergonades) ; croissance continue et irréversible en substrat ; lois (stacking interdit, abrasion proscrite) ; entrer dans un vaisseau est un engagement |
| 08-hypothese-memoire-par-croissance.md | hypothèse | Apprendre, c'est grandir : la mémoire s'inscrit sur la surface qui croît ; tensions avec l'abrasion et la fertilité |
| 09-cadrage-chronologie.md | en cours | Humain → AGI silicium → sphère → intelligence collective humaine ; les transformés veulent disséminer la séquence dans le cosmos |
| 10-concept-cerveaux-biologiques.md | en cours | Troisième paradigme : les humains transformés, cerveaux mixtes bio-nano, intelligence collective par radio |
| 06-concept-spheres-ia.md | en cours | Les IA sont des cerveaux photoniques sphériques : composant passif non linéaire dans le flux lumineux, sans électronique, avec des patchs d'alimentation et d'entrées/sorties ; boules de cristal en tailles standardisées (échelle H), qu'on plante dans un corps ; le Singleton en est un |
