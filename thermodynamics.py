import sympy as smp
from sympy import *
# solve and assign method


def s_a(function, variable):
    sol = smp.solve(function, variable)
    return(sol[0])

# Convert to Kelvin Method



# Define frequently used symbols

cp, m, T_f, T_i, l_heat = smp.symbols('cp m T_f T_i,l')

# Change in Entropy

DS = smp.symbols('\u0394S')

# DS at constant pressure and volume

ds_cp = smp.Eq(m * cp * smp.log(T_f / T_i), DS)

# ds at constant temp and P

ds_h = smp.Eq((m * l) / T, DS)
