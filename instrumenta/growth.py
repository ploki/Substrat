"""Durée de croissance des sphères, de H20 à H0.

Unité de volume : le volume ajouté pour passer de H20 à H19 (= volume de H20).
Unité de temps : la durée de ce passage.

Modèle A (hypothèse de l'auteur) : débit constant en volume, 1 unité de temps par unité de volume.
Modèle B (comparaison) : croissance à vitesse radiale constante, comme un cristal en solution
dont la croissance est limitée par la surface ; la durée est proportionnelle à l'augmentation du rayon.
"""
import math

def volume_ml(n):
    return 1000 / 2 ** (n - 1)

def diametre_mm(n):
    return 2 * (3 * volume_ml(n) / (4 * math.pi)) ** (1 / 3) * 10

v20, d20 = volume_ml(20), diametre_mm(20)
pas_b = diametre_mm(19) - d20

print("| Niveau | Volume | Diamètre | Volume (unités H20) | A : durée du cran vers le niveau | A : cumul depuis H20 | B : cumul depuis H20 |")
print("|---|---|---|---|---|---|---|")
for n in range(20, -1, -1):
    v, d = volume_ml(n), diametre_mm(n)
    u = v / v20
    cran = "—" if n == 20 else f"{volume_ml(n + 1) / v20:,.0f}".replace(",", " ")
    cumul_a = f"{u - 1:,.0f}".replace(",", " ")
    cumul_b = f"{(d - d20) / pas_b:,.1f}".replace(",", " ").replace(".", ",")
    vol = f"{v:,.4f} mL".replace(",", " ").replace(".", ",") if v < 10 else f"{v:,.0f} mL".replace(",", " ")
    print(f"| H{n} | {vol} | {d:.1f} mm".replace(".", ",") + f" | {u:,.0f}".replace(",", " ") + f" | {cran} | {cumul_a} | {cumul_b} |")
