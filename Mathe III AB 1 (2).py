import math

def f(x):                   # Funktion
    return math.sin(x)

def F(x):                   # Stammfunktion
    return -math.cos(x)

def trapezRegel(o, u, n):   # Trapezregel mit Parametern: u = untere Intervallgrenze, o = obere Grenze, n = Anzahl Teilintervalle
    h = (o-u)/n             # Schrittweite berechnen (zwischen Stützstellen)
    erg = (f(u)+f(o))/2     # erste Stützstelle
    for i in range(1,n):                
        erg += f(h*i)       # alle weiteren Stützstellen berechnen und summieren (das jeweilige Teilintervall aus Schrittweite zur unteren Grenze)
    return erg * h          # Ergebnis zurückgeben

ergListe = [["a: "],["b: "],["c: "]]

# A --- --- --- 

# Stammfunktion bestimmen:
#     π/2                             π/2
# I = ∫ sin(x) dx   ->   [-cos(x) + C] 
#     0                               0

x = math.pi/2               # obere Grenze
Io = F(x) + 0       # C = 0

x = 0                       # untere Grenze
Iu = F(x) + 0       

I = Io - Iu                 # exaktes Ergebnis des Integrals, I = 0.999.. ~ 1, Rundungsfehler durch float)

ergListe[0].append(I)       # Ergebnis speichern

# B --- --- --- 

# Taylorpolynom 3. Ordnung mit x0 = 0:
# f(x) = sin(x), f'(x) = cos(x), f''(x) = -sin(x), f'''(x) = -cos(x)
# f(0) = 0, f'(0) = 1, f''(0) = 0, f'''(0) = -1
# T(x) = 1/1!*(x-0)^1 + -1/3!*(x-0)^3
# T(x) = x - 1/6*x^3

x = math.pi/2
I = x - 1/6*x**3            # Taylorpolynom überprüfen (T(x) = 0.9248)

ergListe[1].append(I)       # Ergebnis speichern

# C --- --- --- 
# Erklärungen in der Ausgabe des Programms

i = trapezRegel(math.pi/2,0,1)                                          
ii = trapezRegel(math.pi/4,0,1) + trapezRegel(math.pi/2,math.pi/4,1)
iii = trapezRegel(math.pi/2,0,4)
iv = trapezRegel(math.pi/2,0,8)

ergListe[2].append(i)       # Ergebnisse speichern
ergListe[2].append(ii)
ergListe[2].append(iii)
ergListe[2].append(iv)

print("\nA) Exaktes Ergebnis f(x):\t\t " + str(ergListe[0][1]))
print("B) Näherungswert durch Taylorpolynom:\t " + str(ergListe[1][1]))
print("C) Trapezregel:")
print("\ti) gesamtes Intervall (n=1):\t " + str(ergListe[2][1]))
print("\tii) zwei Teilintervalle (n=2):\t " + str(ergListe[2][2]))
print("\tiii) vier Teilintervalle (n=4):\t " + str(ergListe[2][3]))
print("\tiv) acht Teilintervalle (n=8):\t " + str(ergListe[2][4]))