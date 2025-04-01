def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def balance_combustion(formula):
    # Extraer el número de átomos de C, H y O
    carbon = int(''.join(filter(str.isdigit, formula.split('H')[0][1:]))) if 'H' in formula else 1
    hydrogen = int(''.join(filter(str.isdigit, formula.split('O')[0].split('H')[1]))) if 'O' in formula and len(formula.split('O')) > 1 else 2
    
    # Definir coeficientes
    a = 1  # Hidrocarburo
    c = carbon  # CO2
    d = hydrogen // 2  # H2O
    b = (2 * c + d) // 2  # O2
    
    # Encontrar el mínimo común denominador
    factor = gcd(gcd(a, b), gcd(c, d))
    
    return f"{a//factor} {formula} + {b//factor} O2 -> {c//factor} CO2 + {d//factor} H2O"

# Ejemplo de uso
if __name__ == "__main__":
    hydrocarbon = input("Ingresa la fórmula del hidrocarburo (ej. C2H6): ")
    print(balance_combustion(hydrocarbon))
