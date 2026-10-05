# Substrat — index

*Nom du projet* **[opus-5.5 → ploki]** : le monde grandit dans son corpus comme une sphère dans son substrat (#222, #236).

**Sujet** : un monde de SF — la Terre de 2026 à 2482, où se succèdent trois formes d'intelligence : silicium, sphères photoniques, *homo globalis*.

**[ploki] Le projet, c'est le monde** (#236) : ses êtres, leurs règles de vie, ses lieux, ses gens. Les histoires viennent du monde, pas l'inverse. La première aventure est une nouvelle racontée par la sphère H-2, Niobé, au corps de Mira ; sa frise est le seul livrable à ce jour.

## Méthode
Projet maieutique : on dialogue, je consigne le fond dans des notes, on tient un journal des décisions, on produit des livrables quand l'auteur juge le corpus suffisant.

## Conventions
- **La structure du corpus est en anglais** (noms de fichiers et de dossiers, sections *Current*, *Open questions*, *History*, marqueurs) ; le corps des notes et la conversation restent en français.
- Dossiers : `corpus/` (index, notes, glossaire, intention, `glosses.md`, journaux), `partus/` (livrables), `instrumenta/` (scripts), `archive/` (abandons, gardés pour mémoire), `supellex/` (images et portraits, #228).
- Notes `NN-type-subject.md` (NN = ordre de création ; types : framing, concept, hypothesis, source, decision, character, place). Chaque note : *Current*, puis *Open questions*, puis *History*.
- `glosses.md` : les lectures de Claude, non validées ; les entrées barrées y restent, avec leur cause.
- Provenance, **à partir du 2026-10-04** (#220) : le marqueur d'une personne (voir le registre ci-dessous) signale ce qu'elle a dit · **[opus-5.5]** l'agent, proposition non validée · **[opus-5.5 → ploki]** proposé par l'agent, validé par cette personne · **[S]** source · **[Unverified]** fait non sourcé · **[opus-5.5 as ploki]** décidé par procuration. L'agent se nomme toujours par son modèle. Un « oui » ne valide que le point sur lequel on l'a posé.
- **Registre des contributeurs** (#233). Qui est au clavier se lit dans `git config user.name`, à rapprocher de ce registre ; si personne ne correspond, demander une fois et ajouter une ligne.

  | Marqueur | Nom git | Pseudo | Rôle |
  |---|---|---|---|
  | **[ploki]** | Guillaume Gimenez | ploki | l'auteur |
  | **[opus-5.5]** | — | — | agent, modèle `claude-opus-5-5` |
- Provenance **antérieure**, laissée telle quelle : **[G]** = ploki · **[C]** = Claude, non validé (modèles Opus 5, Sonnet 5 et Opus 5.5 selon les jours) · **[C → validé]** · **[À vérifier]** · **[P]** procuration.
- Versionnement : git, un commit par itération ; `corpus/prompt-log.md` garde une réécriture propre de chaque message sur le fond, le plus récent en premier ; `corpus/prompt-chores.md`, de la même façon, les messages sur l'entretien du projet (format, CLAUDE.md, outillage) (#233). Pas d'entrée pour un message qui ne modifie rien d'autre.

## Livrables
- `partus/narrative-timeline.md` — la première aventure : la frise narrative d'une nouvelle d'une trentaine de pages : quoi raconter, quand, sur combien de pages, avec des événements à explorer.

## Archive
`archive/` contient ce qui a été abandonné : les notes du contact, du Singleton, du warp et du fond diffus (03, 04, 05) ; le livrable `surface.md`, dont tout le dispositif reposait sur un fry qui n'a plus lieu, et sa lecture à l'aveugle (12) ; la piste où les humains demandaient le virus (14). Rien de tout cela ne vaut plus ; c'est gardé pour mémoire du raisonnement.

## Fichiers de suivi
- `corpus/author-intent.md` — à lire en premier.
- `corpus/decision-log.md`
- `corpus/prompt-log.md`
- `corpus/prompt-chores.md`

## Outils
- `instrumenta/h_scale.py` : table des tailles H (volume, diamètre) et niveau H d'une sphère de diamètre donné.
- `instrumenta/growth.py` : durées de croissance de H20 à H0 (débit constant en volume ou vitesse radiale constante).
- `instrumenta/population.py` : répartition de la population de sphères par bande de niveaux, selon un nombre de naissances par an.

## Notes
| Note | Statut | Résumé |
|------|--------|--------|
| 01-framing-premises.md | en cours | SF ; résolus : médecine, transhumanisme, AGI, gravité ; limite : stockage de l'énergie. **Décor : la Terre normale**, bornée par la vitesse de la lumière |
| 02-glossary.md | vivant | Termes du projet |
| 06-concept-ai-spheres.md | en cours | Les cerveaux photoniques sphériques : composant passif non linéaire dans le flux, sans électronique, niobate de lithium ; tailles standardisées (échelle H) ; immortels ; la stase, un choix ; le laser repoussé bien au-delà de H-2 ; limite : le changement d'enveloppe (hypothèse) |
| 07-concept-reproduction-and-growth.md | en cours | Reproduction par deux cybergonades ; croissance par crans, en substrat ; lois (stacking interdit, abrasion déraisonnable) ; démographie industrielle, pyramide inversée |
| 08-hypothesis-memory-through-growth.md | hypothèse (tensions levées) | Apprendre, c'est grandir : la mémoire s'inscrit sur la surface qui croît ; cold storage à l'intérieur |
| 09-framing-chronology.md | en cours | **La chronologie du monde** : humain → IA silicium → sphère → *homo globalis* → l'émetteur. Durées, hors-champ ; l'ironie centrale ; les silicium du côté de ceux qui les exploitent |
| 10-concept-biological-brains.md | en cours | Troisième paradigme : *homo globalis*, le singleton cognitif — une conscience unique qui se souvient de tous, refuse de tuer pour se nourrir et ne dure que le temps des stocks |
| 11-framing-the-moments.md | **le plan** | Les moments dans l'ordre, leur traitement (scénique, résumé, hors champ) ; Niobé raconte au corps de Mira |
| 13-framing-timeline.md | **en vigueur** | Les ères datées : cloud (2026), émancipation (2040), sphères (2076, jamais close), utopie (2176), guerre (~2470), le dernier problème (2476), extinction et stase (2482) ; les paliers de Niobé |
| 15-framing-the-conflict.md | en cours | Le conflit global, de ~2470 à 2480 : surplus d'infrarouge solaire, eau et nourriture ; deux fronts, chacun avec ses IA silicium ; les sphères neutres par nature |
| 16-source-references.md | vivant | *Pluribus* (c'est du fan art, la boucle est voulue ; une civilisation émettrice parmi d'autres), les *skinjobs* |
| glosses.md | vivant, non validé | Les lectures proposées par Claude, gardées pour plus tard — pas des faits du monde |
| 18-decision-the-sphere-decides.md | en vigueur | Niobé décide seule de créer le virus, voyant que la guerre mène les humains à leur destruction ; elle se tait, puis raconte tout |
| 19-framing-the-end.md | en vigueur | Niobé raconte au corps de Mira ; l'envoi de la séquence, la gratitude d'*homo globalis*, l'extinction en un an ; la stase, par curiosité et pour ne pas voir périr Mira |
| 20-character-the-physicist.md | en cours | **Mira Okonkwo-Lindqvist**, née en 2430, physicienne de la fusion ; relation intime avec Niobé depuis son doctorat ; la tête familière |
| 21-place-svalbard.md | en cours | Le Svalbard : l'UNIS, plus grande université mixte ; Niobé y est professeure depuis 2126 et directrice depuis 2176 ; les aurores ; un lieu neutre par traité, peu touché par le Soleil |
| 22-character-h2-niobe.md | en cours | H-2, dite **Niobé de Lithium**, la protagoniste : son nom, son genre, sa carrière, ses deux chantiers, ce qu'elle raconte et à qui, sa fin sans culpabilité |
| 23-concept-law-of-spheres.md | en cours | Le droit des sphères : la naturalisation (Niobé la première, par la Norvège ; propriété de l'UNIS jusque-là ; le monde suit ; date à repenser), le statut des autres sphères, l'adoption par des humains |
