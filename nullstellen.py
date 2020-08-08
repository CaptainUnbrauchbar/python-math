# Mathematik 3 | AB 8 | Aufgabe 3 - Sekantenverfahren / Newtonverfahren

def f(x):                                       # Funktion f(x) = x^2 - 2
    return x**2 - 2

def Df(x):                                      # Ableitung f'(x) = 2x
    return 2*x

def sekantenverfahren(f, x0, x1):
    tol = 1e-12                                 # Toleranz 1*10^-12    
    x = x1                                      # Anfang mit oberer Intervallgrenze
    while abs(f(x)) > tol:                              # bis f(x) > toleranz
        x  = x1 - (x1 - x0) / (f(x1) - f(x0)) * f(x1)   # Sekantenverfahren
        x0 = x1
        x1 = x
    return x

def newton(f, Df, x0):
    tol = 1e-12
    xn = x0
    while True:                         # wiederholen bis toleranz erfüllt
        fxn = f(xn)
        if abs(fxn) < tol:              # Toleranz Kriterium
            return xn                   
        temp = Df(xn)                   # Ableitung von f(x)
        if temp == 0:                   # Keine Lösung gefunden
            return None
        xn = xn - fxn/temp              # Newton Verfahren
    print("Kein Ergebnis gefunden")     
    return None

print(sekantenverfahren(f,1,2))
# Erg: 1.4142135623730954
print(newton(f,Df,1))
# Erg: 1.4142135623730951

# sqrt(2) Taschenrechner : 1.4142135623730950488016887242097‬
# Sekantenverfahren      : 1.4142135623730954
# Newtonverfahren        : 1.4142135623730951
