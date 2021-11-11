def kapustinskii(number_of_ions, cation_charge_number, anion_charge_number, cation_radius, anion_radius):
    lattice_energy = 1.079*10**5*cation_charge_number*anion_charge_number*number_of_ions/(cation_radius+anion_radius)
    return lattice_energy

number_of_ions = int(input('Please enter the number of ions in one formula unit:'))
cation_charge_number = int(input('Please enter the charge number of the cation:'))
anion_charge_number = int(input('Please enter the charge number of the anion:'))
cation_radius = float(input('Please enter the radius in picometres of the cation:'))
anion_radius = float(input('Please enter the radius in picometres of the anion:'))

result = kapustinskii(number_of_ions, cation_charge_number, anion_charge_number, cation_radius, anion_radius)
print(f'The lattice energy is {result} kJ/mol.')