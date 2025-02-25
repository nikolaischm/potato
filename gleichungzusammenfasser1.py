import sympy as sp

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
    
    except Exception as e:
        print(f"Fehler: Ungültige Eingabe! ({e})")

# Gleichung lösen und Rechenweg anzeigen
loese_gleichung()