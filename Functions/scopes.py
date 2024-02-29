#Entender como funciona el local y global scope

F = 9.8 # Variable global

def force_newton(masa, aceleracion):
    F = masa * aceleracion
    print('newton', F, id(F), sep = ' -- >')

def force_pressure(presion, area):
    F = presion * area
    print('pressure',F, id(F), sep = ' -- >') 

force_newton(10, 9.8)
force_pressure(4, 2)
print('global', F, id(F), sep = ' -- >')
