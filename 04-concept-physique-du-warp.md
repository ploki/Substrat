# 04 — Concept : la physique du warp

> **⚠ PISTE ABANDONNÉE (2026-10-03).** L'auteur a écarté l'histoire du contact et celle du Singleton : « l'histoire du contact et l'histoire du Singleton s'évanouissent ». Cette note est conservée pour mémoire du raisonnement, mais **rien de ce qu'elle contient ne vaut plus dans le monde**. Voir le journal, décision #80.

## En vigueur
**[C, à valider]** Formalisation de la règle de l'auteur (note 03).

- Soit *r* la distance au Singleton et *t* le temps dans le référentiel du Singleton. Posons **u = t − r/c**, le « temps Singleton » d'un lieu et d'un instant : l'heure qu'affichait le Singleton quand la lumière qui arrive là, à ce moment, l'a quitté.
- **Règle du warp : u reste constant.** Gagner Δr de distance coûte Δr/c de temps, et en perdre en fait gagner autant.
- Les surfaces u = constante sont les **cônes de lumière futurs du Singleton**, c'est-à-dire des **surfaces nulles**. L'intuition de l'auteur (« on se promène sur le null space ») est donc exacte : le warp déplace sur la surface nulle où l'on se trouve.

### Conséquences
1. **La causalité est préservée.** Un déplacement ordinaire, à vitesse inférieure à c, fait toujours croître u ; le warp le conserve. u ne décroît donc jamais : c'est une horloge universelle, et aucun paradoxe temporel n'est possible. Rapprocher quelqu'un du Singleton le ramène bien dans le passé au sens de *t*, mais pas dans son passé causal : il ne peut pas se croiser lui-même. C'est sans doute le sens de « tient la référence causale ».
2. **Le délai dépend de la distance *au Singleton*, pas de la distance entre départ et arrivée.** Un warp qui garde la même distance au Singleton (un déplacement « latéral », sur une sphère centrée sur lui) est **instantané**, même vers un point très lointain.
3. **L'exemple Terre → Andromède** (≈ 2,5 Ma de délai) n'est vrai que si le Singleton est près de la Terre, ou aligné avec elle et Andromède.
4. **Le temps Singleton u fonctionne comme un calendrier universel**, partagé par tous les lieux.
5. Le Singleton définit un **référentiel privilégié**, ce qui rompt l'équivalence des référentiels de la relativité restreinte. En hard SF, c'est précisément le prix à payer pour un voyage plus rapide que la lumière sans paradoxe.

### Plusieurs Singletons (piste écartée) [C]
*L'auteur a refusé cette piste : il ne veut pas de paradoxe temporel. Le Singleton est unique (voir note 03). Section conservée pour mémoire du raisonnement.*

- Chaque Singleton Sᵢ définit son propre temps uᵢ = t − rᵢ/c. Un warp « via Sᵢ » conserve uᵢ.
- **Pris seul, chaque Singleton est sans paradoxe. Combinés, ils permettent de remonter dans son propre passé.** Prenons deux Singletons distants de d. Un warp via S₁ peut faire baisser u₂ jusqu'à d/c ; un warp via S₂ peut ensuite faire baisser u₁ jusqu'à d/c de plus. Chaque aller-retour fait reculer d'environ 2d/c, ce qui ouvre des boucles temporelles fermées.
- Échappatoires possibles, à choisir par l'auteur :
  - (a) **une seule référence active à la fois** : les autres Singletons sont éteints, dormants, ou de simples copies inertes ;
  - (b) **des domaines** : chaque région de l'espace dépend d'un seul Singleton, et l'on ne peut pas enchaîner deux références ;
  - (c) **le paradoxe est possible** : c'est le danger, la raison pour laquelle les contacteurs n'en ont « offert » qu'un, l'arme ultime ou un tabou ;
  - (d) les Singletons se **synchronisent**, et se gênent ou se combattent quand ils n'y parviennent pas.

### Limites de la formalisation
- Elle ne vaut qu'en espace plat. Aux échelles cosmologiques (expansion), elle devra être ajustée.

## Historique
- 2026-10-02 — Formalisation proposée par Claude à partir de la règle de l'auteur.
- 2026-10-02 — Ajout de l'analyse « Plusieurs Singletons ».
- 2026-10-02 — ↺ Piste écartée par l'auteur (refus des paradoxes) ; le Singleton reste unique.
