import math

wavelength = float(input("Enter the wavelength in cm: "))*1e-2
thickness_cm = float(input("Enter the thickness of the material in 0.1mm: "))*1e-4
epsilon_r = float(input("Enter the relative permittivity of the reflector material: "))

thickness = (wavelength/4) * math.sqrt(epsilon_r)

print("Optimum thickness of the reflector material: {:.6f} meters".format(thickness))