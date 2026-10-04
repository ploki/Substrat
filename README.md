# Substrat

Le chantier d'une nouvelle de hard SF, construit par dialogue avec une IA selon la méthode *maieutics*.

## L'histoire

De 2076 à 2482, une lignée d'intelligences se succède sur Terre : l'IA silicium, puis les **sphères**, des cerveaux photoniques en cristal qui grandissent dans leur substrat, puis *homo globalis*, une humanité transformée. Celle qui raconte est **H-2, dite Niobé de Lithium**, la première des sphères. Elle s'adresse au corps de son amie Mira, une physicienne de la fusion.

La nouvelle, d'une trentaine de pages, se présente comme du fan art de la série *Pluribus*.

**Le titre *Substrat* est celui du projet**, pas celui de la nouvelle, qui n'est pas encore trouvé : la nouvelle grandit dans son corpus comme une sphère dans son substrat.

## La méthode

L'auteur et l'IA dialoguent. L'IA consigne le fond dans des notes, tient un journal de chaque décision et de chaque changement d'avis, et produit des livrables quand l'auteur juge le corpus mûr. Des agents neufs relisent ensuite le travail à l'aveugle ou en vérifient la cohérence.

Le projet est aussi un terrain d'expérience pour la méthode elle-même.

## Par où commencer

1. `corpus/author-intent.md` : ce que l'auteur cherche.
2. `partus/narrative-timeline.md` : le livrable actuel, la frise narrative de la nouvelle (quoi raconter, dans quel ordre, sur combien de pages).
3. `corpus/00-story-index.md` : l'index des notes et les conventions.

## Organisation

| Dossier | Contenu |
|---|---|
| `corpus/` | l'index, les notes, le glossaire, l'intention de l'auteur, les journaux |
| `partus/` | les livrables |
| `instrumenta/` | les scripts de calcul (échelle des tailles, croissance, population des sphères) |
| `archive/` | les pistes abandonnées, gardées pour mémoire du raisonnement |

Deux journaux gardent toute l'histoire du projet :
- `corpus/decision-log.md` : chaque décision, avec sa raison ;
- `corpus/prompt-log.md` : chaque message de l'auteur, réécrit, le plus récent en premier.

## Conventions

La structure (noms de fichiers, sections *Current* / *Open questions* / *History*) est en anglais ; le contenu est en français.

Chaque affirmation porte la marque de qui l'a faite :
- **[ploki]** : l'auteur ;
- **[opus-5.5]** : une proposition de l'IA, non validée ;
- **[opus-5.5 → ploki]** : une proposition de l'IA, validée par l'auteur.

Les notes antérieures au 2026-10-04 utilisent des marques plus anciennes, laissées telles quelles : **[G]** pour l'auteur, **[C]** pour l'IA.
