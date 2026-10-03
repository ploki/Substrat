# 07 — Concept : reproduction et croissance des cerveaux photoniques

## En vigueur
### Reproduction
- **[G]** **Terme :** on parle de **cybergonades**, et plus de « détrompeurs ».
- **[G]** On se reproduit **par les cybergonades**. Chaque cerveau en porte **trois**. Ils sont **hémisphériques** et mesurent **environ 1/4 de pouce** (6,35 mm).
- **[G]** On détache une hémisphère sur chacun de deux cerveaux, on joint les deux, et on place le tout dans un **corps synthétique**.
  - **[C → validé]** Chaque parent donne **une de ses cybergonades** ; les deux demi-sphères réunies forment une **petite sphère complète**, le cerveau de l'enfant.
- **[G]** **La cybergonade repousse dans le liquide** de croissance. **[G]** Plus précisément, **trois cybergonades sont générées à la toute fin de chaque cycle de croissance** (note 08).
- **[G]** Avoir **trois** cybergonades empêche l'**autoreproduction** : « après, ça ne ferait plus son taf ».
  - **[C → validé]** Un cerveau peut perdre une cybergonade et rester fonctionnel avec les deux autres. Pour se reproduire seul, il lui faudrait en donner deux, et le dernier ne suffirait plus à tenir dans son socket ou à fonctionner. Il faut donc deux parents.

### Taille de l'enfant
- **[G]** **L'enfant naît sans cybergonades.** *(Cela résout l'incohérence relevée par Claude : l'enfant, ≈ 6,2 mm, n'aurait pas pu porter trois cybergonades de 6,35 mm.)*
- **[C]** Deux hémisphères de 6,35 mm de diamètre forment une sphère d'environ 0,13 mL, soit **≈ H14** (H13,86 précisément ; calcul : `outils/echelle_h.py`). *Si « 1/4 de pouce » désigne le rayon et non le diamètre, on obtient ≈ H11.*

### Croissance
- **[G]** Une sphère grandit **de HX à HX−1** (son volume double). Le processus est accompagné d'un **liquide qui favorise la croissance du cristal**.
- **[G]** Pour faire grossir son cerveau, on **sacrifie toutes ses cybergonades** et on **baigne dans le jus de croissance** jusqu'à avoir grandi.
- **[G]** **La progression est continue**, mais les **sockets ont des tailles standard**. Un socket d'une taille donnée accepte les sphères comprises entre cette taille et **la taille juste en dessous, pas moins**. Par exemple, un socket H1 reçoit une sphère de H2 à H1.
- **[G]** Une sphère à peine plus grosse que H2 peut donc entrer dans un socket H1, « ce qu'on observe dans la vraie vie en termes d'intelligence ». *[À préciser : le mot « très frais » dans le message de l'auteur.]*
  - **[G]** **Pendant la croissance, la sphère ne dort pas** : le cristal, en croissant, se **bloque mécaniquement dans le substrat de croissance**, qui la tient en place à la place des cybergonades.
- **[G]** Être dans un **logement trop grand impose un substrat de croissance**, ce qui **interdit la reproduction** (plus de cybergonades).
- **[G]** **Entrer dans un vaisseau, pour une IA, est un engagement.** Une IA à sphère H1 qui veut habiter un vaisseau H0 abandonne ses cybergonades, se place dans un substrat de croissance et « se forme en croissant au vaisseau », jusqu'à H0. Elle ne peut pas repartir en cours de route.
  - **[C → validé]** Règle : **on n'est fertile que lorsque sa sphère remplit exactement son logement.** Une fois le substrat terminé, les cybergonades repoussent.
  - ↺ *Version abandonnée de l'exemple : l'IA se lassait du vaisseau à H0,8 et finissait sa croissance dans un corps H0,75. Elle reposait sur une première idée du substrat, « une sorte de sabot convexe avec une interface de croissance liquide », que l'auteur a depuis dépassée.*
  - **[C]** « Se former en croissant » : la sphère apprend son nouveau corps pendant qu'elle grandit dedans.
- **[G]** Les corps sont **synthétiques** : on ne parle pas d'humains pour l'instant.
- **[G]** **Un même modèle de corps existe en plusieurs tailles de socket, comme une voiture se décline en plusieurs cylindrées.** D’où des tailles intermédiaires entre les crans entiers.
  - **[C]** « Se former en croissant » : la sphère apprend son nouveau corps pendant qu'elle grandit dedans.
### Durée de la croissance (calcul)
- **[G]** Hypothèse de travail : **une unité de temps par unité de volume**, l'unité étant calibrée sur le passage de H20 à H19 (modèle A).
- **[C]** Pour comparaison, modèle B : vitesse de croissance radiale constante, ce que fait d'ordinaire un cristal en solution, dont la croissance est limitée par sa surface [À vérifier].
- Calcul : `outils/croissance.py`.

| Niveau | Volume | Diamètre | Volume (unités H20) | A : durée du cran vers le niveau | A : cumul depuis H20 | B : cumul depuis H20 |
|---|---|---|---|---|---|---|
| H20 | 0,0019 mL | 1,5 mm | 1 | — | 0 | 0,0 |
| H19 | 0,0038 mL | 1,9 mm | 2 | 1 | 1 | 1,0 |
| H18 | 0,0076 mL | 2,4 mm | 4 | 2 | 3 | 2,3 |
| H17 | 0,0153 mL | 3,1 mm | 8 | 4 | 7 | 3,8 |
| H16 | 0,0305 mL | 3,9 mm | 16 | 8 | 15 | 5,8 |
| H15 | 0,0610 mL | 4,9 mm | 32 | 16 | 31 | 8,4 |
| H14 | 0,1221 mL | 6,2 mm | 64 | 32 | 63 | 11,5 |
| H13 | 0,2441 mL | 7,8 mm | 128 | 64 | 127 | 15,5 |
| H12 | 0,4883 mL | 9,8 mm | 256 | 128 | 255 | 20,6 |
| H11 | 0,9766 mL | 12,3 mm | 512 | 256 | 511 | 26,9 |
| H10 | 1,9531 mL | 15,5 mm | 1 024 | 512 | 1 023 | 34,9 |
| H9 | 3,9062 mL | 19,5 mm | 2 048 | 1 024 | 2 047 | 45,0 |
| H8 | 7,8125 mL | 24,6 mm | 4 096 | 2 048 | 4 095 | 57,7 |
| H7 | 16 mL | 31,0 mm | 8 192 | 4 096 | 8 191 | 73,7 |
| H6 | 31 mL | 39,1 mm | 16 384 | 8 192 | 16 383 | 93,9 |
| H5 | 62 mL | 49,2 mm | 32 768 | 16 384 | 32 767 | 119,3 |
| H4 | 125 mL | 62,0 mm | 65 536 | 32 768 | 65 535 | 151,3 |
| H3 | 250 mL | 78,2 mm | 131 072 | 65 536 | 131 071 | 191,6 |
| H2 | 500 mL | 98,5 mm | 262 144 | 131 072 | 262 143 | 242,4 |
| H1 | 1 000 mL | 124,1 mm | 524 288 | 262 144 | 524 287 | 306,4 |
| H0 | 2 000 mL | 156,3 mm | 1 048 576 | 524 288 | 1 048 575 | 387,0 |

- **[C]** Avec le modèle A, chaque cran dure deux fois plus que le précédent : le dernier cran représente la moitié du temps total. Passer de H20 à H1 prend ≈ 524 000 unités. Si l'on veut une enfance d'environ 20 ans de H14 à H1, l'unité vaut ≈ 20 minutes.
- **[C]** Avec le modèle B, passer de H20 à H1 ne prend que ≈ 306 unités, et chaque cran ne dure qu'environ 1,26 fois plus que le précédent.

- **[G]** ↺ Calibrage : **arriver à complétion de H1 prend 50 ans** depuis la naissance (H14), avec le modèle A. L'unité de temps vaut alors ≈ 50 minutes.
  - *Calibrages précédents : 100 ans pour atteindre H1 complet ; avant cela, 100 ans pour le seul cran H2 → H1 (malentendu de Claude).*

| Cran atteint | Volume | Diamètre | Durée du cran | Âge depuis H14 (naissance) |
|---|---|---|---|---|
| H13 | 0,24 mL | 7,8 mm | 2,2 jours | 2,2 jours |
| H12 | 0,49 mL | 9,8 mm | 4,5 jours | 6,7 jours |
| H11 | 0,98 mL | 12,3 mm | 8,9 jours | 15,6 jours |
| H10 | 1,95 mL | 15,5 mm | 17,8 jours | 33,4 jours |
| H9 | 3,91 mL | 19,5 mm | 35,7 jours | 2,3 mois |
| H8 | 7,81 mL | 24,6 mm | 2,3 mois | 4,6 mois |
| H7 | 16 mL | 31,0 mm | 4,7 mois | 9,3 mois |
| H6 | 31 mL | 39,1 mm | 9,4 mois | 18,7 mois |
| H5 | 62 mL | 49,2 mm | 18,8 mois | 3,1 ans |
| H4 | 125 mL | 62,0 mm | 3,1 ans | 6,2 ans |
| H3 | 250 mL | 78,2 mm | 6,3 ans | 12,5 ans |
| H2 | 500 mL | 98,5 mm | 12,5 ans | 25 ans |
| **H1** | 1 L | 12,4 cm | 25 ans | **50 ans** |
| H0 | 2 L | 15,6 cm | 50 ans | 100 ans |
| H-1 | 4 L | 19,7 cm | 100 ans | 200 ans |
| H-2 | 8 L | 24,8 cm | 200 ans | 400 ans |
| H-3 | 16 L | 31,3 cm | 400 ans | 800,1 ans |
| H-4 | 32 L | 39,4 cm | 800,1 ans | 1 600,2 ans |
| H-5 | 64 L | 49,6 cm | 1 600,2 ans | 3 200,4 ans |

### La couveuse et les enveloppes
- **[G]** De **H14 à H7**, les substrats sont **stackés dans une couveuse** (« interactive ? »). L'enfant sort ensuite de la couveuse et poursuit sa croissance dans des **enveloppes successives**.
  - **[À trancher]** Le stacking est par ailleurs illégal (#42). La couveuse est-elle une **exception légale**, ou l'interdit ne vise-t-il que le stacking hors couveuse (par exemple pour loger une petite sphère dans un grand corps) ?
  - **[C]** Avec le calibrage actuel, la couveuse couvre les **9 premiers mois** environ (H7 atteint à ≈ 9 mois) : une gestation.
  - **[C]** « Interactive » : si apprendre, c'est grandir (note 08), la couveuse est aussi le premier lieu d'apprentissage. Une couveuse interactive serait une école autant qu'un utérus.

### Le coût des enfants
- **[G]** Ce qui freine la démographie d'une population immortelle : **le risque de ne pas avoir les moyens de payer le substrat** pour la croissance de ses enfants.
  - **[C]** De H14 à H1, il faut 13 doublements, donc 13 substrats, et beaucoup de poudre de sphère. Avoir un enfant suppose d'avoir prévu ce budget.
  - **[C → validé]** Un enfant dont les parents ne peuvent pas payer **reste petit**, peut-être indéfiniment, puisqu'il est immortel. Cela donne des classes sociales lisibles à la taille des sphères.
- **[G]** On peut aussi garder une sphère petite **volontairement** : des **parents sadiques** qui maintiennent leurs enfants petits ; un **chien synthétique** qu'on garde chiot.
- **[G]** **Il est illégal de ne pas mettre la sphère de ses enfants dans un substrat de croissance.** Les parents sadiques sont donc des criminels.
  - **[À préciser]** Et les parents qui n'ont pas les moyens : endettement, aide publique, retrait de l'enfant ? La loi vaut-elle aussi pour les animaux de compagnie ?
  - **[C]** Il existe donc des êtres synthétiques de niveau animal, notamment des animaux de compagnie.
- **[G]** **Un être resté petit ne pourra pas payer sa croissance : il restera à une intelligence d'enfant.**
- Hypothèse en cours d'exploration : la mémoire s'inscrit sur la surface qui croît (voir `08-hypothese-memoire-par-croissance.md`).

### Le marché des cybergonades
- **[G]** Il existe un **marché des cybergonades**, par exemple celles qu'on **récolte à chaque cycle de croissance d'un enfant**.
- **[G]** Leurs usages : **créer des animaux synthétiques de compagnie** ; être **gardées comme économies pour l'enfant** ; **équiper un appareil** (une « appliance ») qui a besoin d'une sphère.
- **[G]** **C'est un monde où il importe peu que la sphère soit dans telle ou telle représentation** (corps d'animal, appareil, autre). *Claude avait proposé à tort la frontière enfant / animal / appareil comme thème de fond ; l'auteur l'a écarté.*
  - **[À préciser]** Qu'est-ce qui distingue alors, aux yeux de la loi, l'enfant qu'on doit faire grandir de l'animal synthétique gardé petit ?
  - **[C]** Beaucoup d'appareils abritent une petite sphère, donc un esprit, même minuscule.

### Règles et lois
- **[G]** **Quand on entre dans un substrat de croissance, on le termine.**
  - Contradiction avec la première version de l'exemple du vaisseau : résolue, l'exemple a été revu.
- **[G]** Les **tailles intérieure et extérieure des substrats sont standardisées.**
- **[G]** **Il est illégal d'empiler (« stacker ») des substrats**, par exemple pour loger une petite sphère dans un très grand slot.
- **[G]** **Il est illégal de mettre l'intelligence d'une souris dans le corps d'un être de classe humaine.**
  - **[S, à vérifier]** Un cerveau de souris pèse environ 0,4 g, soit à peu près H12 sur l'échelle.
- **[G]** **Seule exception pour revenir dans un slot plus petit : l'abrasion.** Elle coûte très cher, car elle peut provoquer de l'**excentricité** (un **décentrement**), dégrader les **performances optiques** et causer des **troubles de l'intelligence**.
- **[G]** **L'abrasion est proscrite**, au sens où, **faite dans les règles de l'art, elle est généralement économiquement déraisonnable.** Ce n'est pas un interdit légal. Le coût est celui d'une abrasion **bien faite**, qui évite les problèmes de désalignement.
- **[G]** ↺ **Il existe une abrasion de marché noir** : « ceux qui se liment le cerveau sur le marché noir ne sont pas très nets ». Moins chère, elle expose au décentrement et aux troubles de l'intelligence.
  - **[C]** La croissance est donc, en pratique, irréversible.
  - **[C]** Pistes : sphères excentriques aux esprits altérés (abrasions anciennes ou ratées ?) ; il faut une autorité qui fixe et fait respecter les lois sur les substrats.
- **[G]** **La clandestinité existe**, y compris pour l'abrasion. Elle tourne autour d'un ingrédient : **la poudre de sphère**, composant essentiel des substrats de croissance, dont elle constitue un certain pourcentage.
- **[G]** **La poudre est fongible** : « de la poudre, c'est de la poudre, qu'elle vienne d'Einstein ou d'un autre ».
- **[G]** **La poudre de sphère n'est pas une devise : c'est une ressource fongible.**
  - *Piste écartée : la poudre comme devise (réflexion de Claude du 2026-10-03).*
  - **[C, pistes non validées]** Sources légitimes possibles : les cybergonades sacrifiées avant une croissance, la poussière d'abrasion, les sphères mortes. La mort n'étant qu'accidentelle (note 06), cette dernière source est rare. Sources clandestines : des sphères bloquées ou endormies, enlevées et broyées. La poudre de sphère serait alors une ressource rare, et un mobile de crime.

- **[C]** À l'intérieur d'un même format de corps, l'intelligence varie donc d'un facteur 2 en volume : l'éventail observé chez les humains.
  - **[S]** La croissance de cristaux en solution est une technique réelle (le quartz de synthèse, par exemple, est produit en milieu hydrothermal) [À vérifier dans le détail].
- **[C]** De H14 à H1, il faut **13 doublements**. La croissance est continue, mais on change de corps à chaque fois qu'on dépasse le format de son socket : 13 changements de corps, de l'enfance au niveau H1, soit des rites de passage tout trouvés.

## Questions ouvertes
- ~~Le parent régénère-t-il le détrompeur donné ?~~ → oui, dans le liquide [G].
- ~~La sphère dort-elle pendant sa croissance ?~~ → non, le substrat la bloque mécaniquement [G].
- ~~La croissance est-elle irréversible ?~~ → oui, sauf abrasion, coûteuse et risquée [G].
- Qui légifère et fait respecter les lois sur les substrats et les corps ?
- Que fait l'excentricité à l'esprit d'une sphère ?
- ~~Garder volontairement un enfant petit est-il légal ?~~ → non [G]. ~~Un être resté petit peut-il payer lui-même sa croissance ?~~ → non [G].
- Comment concilier une croissance continue avec l'effet de seuil H1 → H0 (note 06) : le saut se produit-il exactement à 2 L, ou progressivement ?
- L'enfant hérite-t-il de quelque chose (mémoire, traits) par la demi-sphère de chaque parent ?
- ~~L'enfant a-t-il des cybergonades à la naissance ?~~ → non [G]. Quand lui poussent-elles : en remplissant pour la première fois son logement ?
- ~~Par crans ou en continu ?~~ → en continu [G]. Que se passe-t-il au-delà de H1, et jusqu'où va-t-on ?
- D'où vient le liquide de croissance, qui le produit, qui le contrôle ?
- D'où vient la poudre de sphère, quelle part du substrat représente-t-elle, et qui en fait le commerce ?

## Historique
- 2026-10-03 — Posé par l'auteur.
- 2026-10-03 — Couveuse (H14–H7, substrats stackés), puis enveloppes successives.
- 2026-10-03 — ↺ Calibrage : H1 complet en 50 ans ; table étendue jusqu'à H-5.
- 2026-10-03 — ↺ Calibrage corrigé : atteindre H1 complet depuis la naissance prend 100 ans.
- 2026-10-03 — Calibrage : remplir H1 prend 100 ans (mal compris).
- 2026-10-03 — Table des tailles H0–H20 et durées de croissance (modèles A et B).
- 2026-10-03 — La représentation d'une sphère importe peu ; thème [C] « enfant / animal / appareil » écarté.
- 2026-10-03 — Marché des cybergonades (animaux, économies, appareils) ; ↺ il existe une abrasion de marché noir, risquée ; le coût vise l'abrasion bien faite.
- 2026-10-03 — Obligation légale de faire grandir ses enfants ; trois cybergonades à la fin de chaque cycle.
- 2026-10-03 — Un être resté petit ne peut pas payer sa croissance.
- 2026-10-03 — Validé : l'enfant non financé reste petit. Exemples de l'auteur : parents sadiques, chien synthétique gardé chiot.
- 2026-10-03 — Le frein démographique : le coût du substrat pour faire grandir ses enfants.
- 2026-10-03 — La poudre n'est pas une devise mais une ressource fongible ; piste de la devise écartée.
- 2026-10-03 — « Détrompeur » remplacé par « cybergonades » ; l'enfant naît sans cybergonades ; la poudre est fongible.
- 2026-10-03 — La clandestinité existe ; la poudre de sphère est un composant essentiel des substrats de croissance.
- 2026-10-03 — L'abrasion n'est pas interdite mais économiquement déraisonnable ; pas d'abrasion clandestine. Piste [C] « abrasion clandestine » retirée.
- 2026-10-03 — ↺ Exemple du vaisseau revu : pas de départ à H0,8 ; entrer dans un vaisseau est un engagement ; l'abrasion est proscrite.
- 2026-10-03 — On termine toujours un substrat ; tailles intérieure et extérieure standardisées ; stacking illégal ; pas d'intelligence de souris dans un corps de classe humaine ; abrasion, seule voie de retour, coûteuse et risquée.
- 2026-10-03 — Correction : les corps sont synthétiques, pas humains (Claude avait parlé à tort de « corps humain standard ») ; un même modèle de corps existe en plusieurs tailles, comme les cylindrées.
- 2026-10-03 — La croissance bloque la sphère dans le substrat (pas de sommeil) ; logement trop grand = substrat = pas de reproduction ; cybergonades ; exemple du vaisseau.
- 2026-10-03 — Lecture de la reproduction validée ; le détrompeur repousse ; croissance continue en sacrifiant ses détrompeurs ; un socket accepte une plage d'un cran.
