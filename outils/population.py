"""Population des sphères par bande de niveaux.

**Constat [C] :** la reproduction libre est impossible. Une sphère détache 3 cybergonades
à la fin de chaque cycle (1,5 enfant), et le premier cycle ne dure que 2,2 jours : la
population serait multipliée par 2,5 tous les 2,2 jours, soit ~10^65 en un an. La
démographie des sphères n'est donc pas biologique mais **industrielle** : elle vaut ce
que la civilisation produit de substrats (notes 07, 55).

Ce script suppose donc un **nombre constant de naissances par an** et donne la
répartition par bande, à une date donnée.

Usage : python3 outils/population.py [naissances_par_an]
"""
import sys

AN = 365.25
TOT = sum(2 ** (19 - n) for n in range(13, 0, -1))
U = 50 * AN / TOT

def age_a(n):
    """Âge, en années, auquel une sphère atteint le niveau Hn (naissance à H14)."""
    return sum(2 ** (19 - k) for k in range(13, n - 1, -1)) * U / AN if n < 14 else 0.0

BANDES = [("H14–H10", 14, 10), ("H9–H5", 9, 5), ("H4–H0", 4, 0)]

def occupation(hi, lo):
    """Durée pendant laquelle une sphère se trouve dans la bande [lo..hi]."""
    debut = age_a(hi)
    fin = age_a(lo - 1)  # quand elle quitte la bande
    return debut, fin

def table(n_par_an, dates):
    print(f"Hypothèse : {n_par_an:,} naissances par an, à partir de 2076.".replace(",", " "))
    print("\n| Année | " + " | ".join(b[0] for b in BANDES) + " | total |")
    print("|---|---|---|---|---|")
    for a in dates:
        A = a - 2076
        cols, tot = [], 0
        for _, hi, lo in BANDES:
            d, f = occupation(hi, lo)
            n = n_par_an * (min(f, A) - min(d, A))
            cols.append(f"{n:,.0f}".replace(",", " "))
            tot += n
        print(f"| {a} | " + " | ".join(cols) + f" | {tot:,.0f}".replace(",", " ") + " |")

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
    table(n, (2101, 2126, 2176, 2276, 2476))
    print("\nDurées d'occupation de chaque bande :")
    for nom, hi, lo in BANDES:
        d, f = occupation(hi, lo)
        print(f"  {nom:>8} : de {d:8.2f} an à {f:8.2f} ans  ({f-d:8.2f} ans)")
