from sympy import symbols, Eq, solve

def balance_combustion(formula):
    # Elementos químicos involucrados en la combustión
    C, H, O = symbols('C H O')
    a, b, c, d = symbols('a b c d')
    
    # Extraer el número de átomos de C, H y O
    carbon = int(''.join(filter(str.isdigit, formula.split('H')[0][1:]))) if 'H' in formula else 1
    hydrogen = int(''.join(filter(str.isdigit, formula.split('O')[0].split('H')[1]))) if 'O' in formula else 2
    oxygen = int(''.join(filter(str.isdigit, formula.split('O')[1]))) if 'O' in formula and len(formula.split('O')) > 1 else 0
    
    # Definir ecuaciones de conservación de masa
    eq1 = Eq(carbon * a, c)  # Carbono
    eq2 = Eq(hydrogen * a, 2 * d)  # Hidrógeno
    eq3 = Eq(2 * b, 2 * c + d)  # Oxígeno
    
    # Resolver ecuaciones
    solution = solve((eq1, eq2, eq3), (a, b, c, d))
    
    if solution:
        return f"{solution[a]} {formula} + {solution[b]} O2 -> {solution[c]} CO2 + {solution[d]} H2O"
    else:
        return "No se pudo balancear la ecuación."

# Ejemplo de uso
if __name__ == "__main__":
    hydrocarbon = input("Ingresa la fórmula del hidrocarburo (ej. C2H6): ")
    print(balance_combustion(hydrocarbon))
