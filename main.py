import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def loese_gleichung():
    # Benutzerdefinierte Eingabe der Gleichung
    eingabe = input("Gib eine Gleichung ein (z.B. 2*x + 5 = 2 + 5): ")
    
    # Umwandlung der Eingabe in Kleinbuchstaben, um die Variable korrekt zu erkennen
    eingabe = eingabe.replace('X', 'x')  # X wird zu x ersetzt
    
    # Erstelle ein Symbol für x
    x = sp.symbols('x')
    
    try:
        # Zerlege die Eingabe in linke und rechte Seite der Gleichung
        if '=' not in eingabe:
            raise ValueError("Die Eingabe muss ein '=' enthalten.")
        
        linke_seite, rechte_seite = eingabe.split('=')
        # Erstelle eine echte Gleichung mit sympy.Eq
        gleichung = sp.Eq(sp.sympify(linke_seite), sp.sympify(rechte_seite))

        # Schritt-für-Schritt Lösung der Gleichung
        print("\nRechenweg:")
        
        # 1. Ursprüngliche Gleichung anzeigen
        print(f"1. Ursprüngliche Gleichung: {gleichung}")

        # 2. Umstellen der Gleichung (alles auf eine Seite bringen)
        umgestellt = sp.simplify(gleichung.lhs - gleichung.rhs)
        print(f"2. Umgestellt (alles auf eine Seite): {umgestellt} = 0")

        # 3. Lösung der Gleichung nach x
        loesung = sp.solve(gleichung, x)
        
        # Ausgabe der Lösung
        if loesung:
            print(f"\nDie Lösung der Gleichung ist: x = {loesung[0]}")
        else:
            print("\nEs gibt keine Lösung oder unendlich viele Lösungen.")

        # 4. Zeichne den Graphen
        zeichne_graph(linke_seite, rechte_seite, loesung)

    except Exception as e:
        print(f"Fehler: Ungültige Eingabe! ({e})")


def zeichne_graph(linke_seite, rechte_seite, loesung):
    # Umwandlung der linken und rechten Seite in lambdified Funktionen
    x = sp.symbols('x')
    f_links = sp.lambdify(x, sp.sympify(linke_seite), "numpy")

    # Prüfen, ob die rechte Seite eine Konstante ist
    rechte_expr = sp.sympify(rechte_seite)
    if rechte_expr.free_symbols:
        f_rechts = sp.lambdify(x, rechte_expr, "numpy")
    else:
        # Wenn die rechte Seite eine Konstante ist, erstelle eine Funktion, die die Konstante zurückgibt
        konstante = float(rechte_expr)
        f_rechts = lambda x: np.full_like(x, konstante)

    # Erstelle x-Werte für den Plot
    x_werte = np.linspace(-10, 10, 400)
    y_links = f_links(x_werte)
    y_rechts = f_rechts(x_werte)

    # Plot erstellen
    plt.figure(figsize=(10, 6))
    plt.plot(x_werte, y_links, label=f"Linke Seite: {linke_seite}")
    plt.plot(x_werte, y_rechts, label=f"Rechte Seite: {rechte_seite}")

    # Schnittpunkte (Lösungen) markieren
    if loesung:
        for l in loesung:
            y_wert = f_links(float(l))
            plt.plot(float(l), y_wert, 'ro')  # Markiere die Lösung als roten Punkt
            plt.text(float(l), y_wert, f'  x={float(l):.2f}', color='red')

    plt.axhline(0, color='black', linewidth=0.5)  # x-Achse
    plt.axvline(0, color='black', linewidth=0.5)  # y-Achse
    plt.title("Graph der Gleichung")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)

    # Speichere den Graphen als Bild
    dateipfad = "graph.png"
    plt.savefig(dateipfad)
    print(f"Graph gespeichert als '{dateipfad}'")

# Gleichung lösen und Rechenweg anzeigen
loese_gleichung()