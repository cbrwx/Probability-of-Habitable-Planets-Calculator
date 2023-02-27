# Calculate the probability of habitable planets for an example set of values
fd = 0.5
fp = 0.1
ne = 2
# Perform a quick calculation if you do not have the time or inclination to search for the exact numbers.

fl = 0.5
fi = 0.5
fc = 0.5
L = 1

N = 1000000000000 # total number of stars in the universe (example value)
probability = (fd * fp * ne * fl * fi * fc * L) / N

probability *= 1.5 ** 2
probability *= (1.5 ** 2.06) * ((1 + 0.0012 * (4.6 - 4.6)) ** (-4.68))
probability *= (0.025 + 0.5)
probability *= (1 + 0.1 * 0.5)
probability *= (1 + 5 * 0.5)
probability *= (0.5 + 0.3 * 0.5 + 0.7 * 0.5)
probability *= (1 + 0.33 * 0.5)
probability *= (1 - 0.01 * 10)
probability *= (1 + 0.33 * 0.5)
probability *= (1 + 0.33 * 0.5)
probability *= (1 + 0.5 * 0.5)
probability *= (1 - 0.5)
probability *= (1 + 0.5 * 0.5)
probability *= (1 + 0.5)
probability *= (1 - 0.5)
probability *= (1 + 0.33 * 0.5)
probability *= (1 + 0.33 * 0.5)
probability *= (1 - 0.5)
probability *= (1 + 0.33 * 0.5)
probability *= (1 + 0.33 * 0.5)
probability *= (1 - 0.5)
probability *= (1 + 0.33 * 0.5)
probability *= (1 + 0.33 * 0.5)
probability *= (1 + 0.33 * 0.5)

# Output the probability of habitable planets to the user
print("The probability of habitable planets in the universe for the example values is:", probability)
