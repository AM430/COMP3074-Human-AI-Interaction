"""4. Define a string raw containing a sentence of your own choosing.  Now, split raw on some
character other than space."""

raw = "Nottingham-London-Manchester-Birmingham"  ## , - / : ; |
cities = raw.split("-")
print(cities)
