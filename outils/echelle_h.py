"""Échelle H des cerveaux photoniques : H1 = 1 L, le volume double à chaque cran vers H0, H-1…

Usage : python3 outils/echelle_h.py            -> table des tailles
        python3 outils/echelle_h.py 6.35       -> niveau H d'une sphère de 6,35 mm de diamètre
"""
import math, sys

def volume_ml(n):
    return 1000 / 2 ** (n - 1)

def diametre_mm(v_ml):
    return 2 * (3 * v_ml / (4 * math.pi)) ** (1 / 3) * 10

def niveau(d_mm):
    v = (4 / 3) * math.pi * (d_mm / 20) ** 3
    return 1 + math.log2(1000 / v)

if len(sys.argv) > 1:
    d = float(sys.argv[1])
    print(f"Sphère de {d} mm de diamètre : H{niveau(d):.2f}")
else:
    print(f"{'niveau':>7} {'volume':>12} {'diamètre':>10}")
    for n in range(-3, 17):
        v = volume_ml(n)
        print(f"{'H' + str(n):>7} {v:>9.3f} mL {diametre_mm(v):>7.1f} mm")
