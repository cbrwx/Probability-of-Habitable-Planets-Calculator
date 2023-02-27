# Print out the equation for calculating the probability of habitable planets
print("Probability of habitable planets = (f_d * f_p * n_e * f_l * f_i * f_c * L) / N")

# Get input from the user for the various factors
distance = float(input("Enter the distance from the star in AU: "))
size = float(input("Enter the size of the planet in Earth masses: "))
age = float(input("Enter the age of the planet in billions of years: "))
composition = float(input("Enter the composition of the planet (0-1): "))
magnetic_field = float(input("Enter the strength of the planet's magnetic field (0-1): "))
orbit_stability = float(input("Enter the stability of the planetary orbit (0-1): "))
water = float(input("Enter the presence of liquid water (0-1): "))
organic_molecules = float(input("Enter the presence of organic molecules (0-1): "))
climate_stability = float(input("Enter the stability of the planet's climate (0-1): "))
atmosphere = float(input("Enter the atmosphere conditions (0-1): "))
plate_tectonics = float(input("Enter the presence of plate tectonics (0-1): "))
other_systems_distance = float(input("Enter the distance from other stars or planetary systems in light years: "))
geological_activity = float(input("Enter the geological activity (0-1): "))
metallicity = float(input("Enter the parent star's metallicity (0-1): "))
energy_sources = float(input("Enter the availability of energy sources (0-1): "))
moon = float(input("Enter the presence of a moon (0-1): "))
stellar_activity = float(input("Enter the level of stellar activity (0-1): "))
planetary_magnetic_field = float(input("Enter the strength of the planetary magnetic field (0-1): "))
surface_features = float(input("Enter the presence of planetary surface features (0-1): "))
interstellar_medium = float(input("Enter the density and composition of the interstellar medium (0-1): "))
rotation = float(input("Enter the rate of planetary rotation (0-1): "))
obliquity = float(input("Enter the planetary obliquity (0-1): "))
crust_thickness = float(input("Enter the planetary crust thickness (0-1): "))
atmosphere_loss = float(input("Enter the rate of planetary atmosphere loss (0-1): "))
evolutionary_history = float(input("Enter the planetary evolutionary history (0-1): "))
global_magnetic_field = float(input("Enter the presence of a global magnetic field (0-1): "))
surface_radiation = float(input("Enter the type and intensity of the planet's surface radiation (0-1): "))
nutrients = float(input("Enter the availability of nutrients and resources for life (0-1): "))
impacts = float(input("Enter the role of impacts from asteroids or comets (0-1): "))
exoplanet_moons_rings = float(input("Enter the presence of exoplanet moons or rings (0-1): "))

# Calculate the probability of habitable planets
fd = 0.5
fp = 0.1
ne = 2
fl = water
fi = organic_molecules
fc = climate_stability
L = 1

N = 1000000000000 # total number of stars in the universe (example value)
probability = (fd * fp * ne * fl * fi * fc * L) / N

Apply user input to calculate probability of habitable planets
probability *= distance ** 2
probability *= (size ** 2.06) * ((1 + 0.0012 * (age - 4.6)) ** (-4.68))
probability *= (0.025 + composition)
probability *= (1 + 0.1 * magnetic_field)
probability *= (1 + 5 * orbit_stability)
probability *= (water + 0.3 * organic_molecules + 0.7 * climate_stability)
probability *= (1 + 0.33 * plate_tectonics)
probability *= (1 - 0.01 * other_systems_distance)
probability *= (1 + 0.33 * geological_activity)
probability *= (1 + 0.33 * metallicity)
probability *= (1 + energy_sources)
probability *= (1 + 0.5 * moon)
probability *= (1 - stellar_activity)
probability *= (1 + 0.5 * planetary_magnetic_field)
probability *= (1 + surface_features)
probability *= (1 - interstellar_medium)
probability *= (1 + 0.5 * rotation)
probability *= (1 + 0.33 * obliquity)
probability *= (1 + 0.33 * crust_thickness)
probability *= (1 - atmosphere_loss)
probability *= (1 + 0.33 * evolutionary_history)
probability *= (1 + 0.33 * global_magnetic_field)
probability *= (1 - surface_radiation)
probability *= (1 + 0.33 * nutrients)
probability *= (1 + 0.33 * impacts)
probability *= (1 + 0.33 * exoplanet_moons_rings)

Output the probability of habitable planets to the user
print("The probability of habitable planets in the universe is:", probability)
