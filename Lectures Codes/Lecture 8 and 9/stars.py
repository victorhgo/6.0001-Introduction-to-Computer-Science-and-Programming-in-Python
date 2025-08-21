# A small star catalog to test OOP concepts
# We can put all stars into a JSON file to make it easier to work with

# We will use the pyplot to plot a graph (just to demonstrate the stars luminosity)
import matplotlib.pyplot as plot

# Create a parent class Star with attributes: 
# name, age, size, mass, temperature, luminosity, colour and chemical composition
class Star(object):
    def __init__(self, name):
        self.name = name

    def setAge(self, newAge):
        self.age = newAge

    def setSize(self, newSize):
        self.size = newSize
    
    def setMass(self, newMass):
        self.mass = newMass
    
    def setTemp(self, newTemp):
        self.temp = newTemp
    
    def __str__(self):
        return "Star name: "+str(self.name)+" Age: " +str(self.age)
    
class Star(object):
    def __init__(self, name):
        self.name = name
        self.age = None
        self.size = None
        self.mass = None
        self.temp = None
        self.luminosity = None
        self.colour = None
        self.chemComp = None

    # Setters
    def setAge(self, newAge):
        self.age = newAge

    def setSize(self, newSize):
        self.size = newSize
    
    def setMass(self, newMass):
        self.mass = newMass
    
    def setTemp(self, newTemp):
        self.temp = newTemp
    
    def setLum(self, newLuminosity):
        self.luminosity = newLuminosity

    def setColour(self, newColour):
        self.colour = newColour

    def setChemComp(self, newComposition):
        self.chemComp = newComposition

    # Getters
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getSize(self):
        return self.size

    def getMass(self):
        return self.mass

    def getTemp(self):
        return self.temp

    def getLum(self):
        return self.luminosity

    def getColour(self):
        return self.colour

    def getChemComp(self):
        return self.chemComp

    def __str__(self):
        return (
            f"Star name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Size: {self.size}\n"
            f"Mass: {self.mass}\n"
            f"Temperature: {self.temp}\n"
            f"Luminosity: {self.luminosity}\n"
            f"Colour: {self.colour}\n"
            f"Chemical Composition: {self.chemComp}"
        ) # Better way of printing a lot of data

# Plot data, test 1 - Following matplotlib.pyplot manual

def plotSizeLuminosity(starsCatalog):
    names = []
    sizes = []
    luminosities = []

    for name, star in starsCatalog.items():
        try:
            # Parse size and luminosity to float assuming they are in "X * Sun ..." format
            sizeStr = str(star.getSize())
            lumStr = str(star.getLum())

            # Extract numeric values if formatted like "X * Sun luminosity"
            size = float(sizeStr.split("*")[0].strip()) if "*" in sizeStr else float(sizeStr)
            lum = float(lumStr.split("*")[0].strip()) if "*" in lumStr else float(lumStr)

            names.append(name)
            sizes.append(size)
            luminosities.append(lum)

        except (ValueError, AttributeError, TypeError):
            # Skip stars with missing or invalid data
            continue

    # Plotting the graph
    plot.figure(figsize=(10, 6))
    plot.scatter(sizes, luminosities, color='gold', edgecolor='black', s=100)

    for i, name in enumerate(names):
        plot.text(sizes[i], luminosities[i], name, fontsize=9, ha='right', va='bottom')

    plot.xscale("log")
    plot.yscale("log")
    plot.xlabel("Size (relative to Sun, log scale)")
    plot.ylabel("Luminosity (relative to Sun, log scale)")
    plot.title("Star Size vs Luminosity")
    plot.grid(True, which="both", ls="--", linewidth=0.25)
    plot.tight_layout()
    plot.show()

# We can create a dictionary and save all stars: key: "name" value: obj instance
stars = {}

#  Instances of the Star class:

# Sun
sun = Star("Sun")
sun.setAge(4.6e9) # Billion years
sun.setSize("1.392 million km in diameter")
sun.setMass("1.989 * 10^30 kg")
sun.setTemp("5778 K")
sun.setLum("3.828 * 10^26 W")
sun.setColour("Yellow")
sun.setChemComp("74% Hydrogen, 24% Helium, 2% other elements")
stars["Sun"] = sun

# Betelgeuse
betelgeuse = Star("Betelgeuse")
betelgeuse.setAge(8.0e6)
betelgeuse.setSize("1.2 billion km diameter")
betelgeuse.setMass("11.6 * Sun mass")
betelgeuse.setTemp("3500 K")
betelgeuse.setLum("126,000 * Sun luminosity")
betelgeuse.setColour("Red")
betelgeuse.setChemComp("Hydrogen, Helium, heavy elements")
stars["Betelgeuse"] = betelgeuse

# Sirius
sirius = Star("Sirius")
sirius.setAge(2.4e8)
sirius.setSize("1.71 * Sun radius")
sirius.setMass("2.06 * Sun mass")
sirius.setTemp("9940 K")
sirius.setLum("25.4 * Sun luminosity")
sirius.setColour("White")
sirius.setChemComp("Hydrogen, Helium")
stars["Sirius"] = sirius

# Antares
antares = Star("Antares")
antares.setAge(1.2e7)
antares.setSize("850 * Sun radius")
antares.setMass("12 * Sun mass")
antares.setTemp("3400 K")
antares.setLum("75,900 * Sun luminosity")
antares.setColour("Red")
antares.setChemComp("Hydrogen, Helium, heavy elements")
stars["Antares"] = antares

# Polaris
polaris = Star("Polaris")
polaris.setAge(7.0e7)
polaris.setSize("50 * Sun radius")
polaris.setMass("5.4 * Sun mass")
polaris.setTemp("6015 K")
polaris.setLum("2500 * Sun luminosity")
polaris.setColour("Yellow-white")
polaris.setChemComp("Hydrogen, Helium")
stars["Polaris"] = polaris

# Proxima Centauri A
proxima_a = Star("Proxima Centauri A")
proxima_a.setAge(4.85e9)
proxima_a.setSize("0.1542 * Sun radius")
proxima_a.setMass("0.1221 * Sun mass")
proxima_a.setTemp("3042 K")
proxima_a.setLum("0.0017 * Sun luminosity")
proxima_a.setColour("Red")
proxima_a.setChemComp("Hydrogen, Helium")
stars["Proxima Centauri A"] = proxima_a

# Proxima Centauri B (technically a planet, but included)
proxima_b = Star("Proxima Centauri B")
proxima_b.setAge(4.85e9)
proxima_b.setSize("1.17 * Earth radius")
proxima_b.setMass("1.27 * Earth mass")
proxima_b.setTemp("234 K")
proxima_b.setLum("N/A")
proxima_b.setColour("N/A")
proxima_b.setChemComp("Iron, silicates, possible water")
stars["Proxima Centauri B"] = proxima_b

# Vega
vega = Star("Vega")
vega.setAge(4.5e8)
vega.setSize("2.362 * Sun radius")
vega.setMass("2.1 * Sun mass")
vega.setTemp("9602 K")
vega.setLum("40 * Sun luminosity")
vega.setColour("Blue-white")
vega.setChemComp("Hydrogen, Helium")
stars["Vega"] = vega

# Arcturus
arcturus = Star("Arcturus")
arcturus.setAge(7.1e9)
arcturus.setSize("25 * Sun radius")
arcturus.setMass("1.1 * Sun mass")
arcturus.setTemp("4286 K")
arcturus.setLum("170 * Sun luminosity")
arcturus.setColour("Orange")
arcturus.setChemComp("Hydrogen, Helium")
stars["Arcturus"] = arcturus

# Altair
altair = Star("Altair")
altair.setAge(1.2e9)
altair.setSize("1.8 * Sun radius")
altair.setMass("1.79 * Sun mass")
altair.setTemp("7550 K")
altair.setLum("10.6 * Sun luminosity")
altair.setColour("White")
altair.setChemComp("Hydrogen, Helium")
stars["Altair"] = altair

# Aldebaran
aldebaran = Star("Aldebaran")
aldebaran.setAge(6.4e9)
aldebaran.setSize("44.2 * Sun radius")
aldebaran.setMass("1.16 * Sun mass")
aldebaran.setTemp("3910 K")
aldebaran.setLum("518 * Sun luminosity")
aldebaran.setColour("Orange")
aldebaran.setChemComp("Hydrogen, Helium, metals")
stars["Aldebaran"] = aldebaran

# Bellatrix
bellatrix = Star("Bellatrix")
bellatrix.setAge(2.5e7)
bellatrix.setSize("5.8 * Sun radius")
bellatrix.setMass("8.6 * Sun mass")
bellatrix.setTemp("21,800 K")
bellatrix.setLum("6400 * Sun luminosity")
bellatrix.setColour("Blue-white")
bellatrix.setChemComp("Hydrogen, Helium")
stars["Bellatrix"] = bellatrix

# R136a1 - Biggest and most luminous star
r136a1 = Star("R136a1")
r136a1.setAge(1.5e6)
r136a1.setSize("40 * Sun radius")
r136a1.setMass("215 * Sun mass")
r136a1.setTemp("46,000 K")
r136a1.setLum("6170000 * Sun luminosity")
r136a1.setColour("Blue-white")
r136a1.setChemComp("Hydrogen, Helium and Nitrogen")
stars["R136a1"] = r136a1

# Now we can print all star names and some information by accessing the dictionary:

print("Star Catalog:")

for name in stars:
    print("-", name)

print("\nSome details:")
print(stars["R136a1"])

print("\n---\n")
print(stars["Sirius"])

print("\n---\n")
print(stars["Vega"])

print("\n---\n")
print(stars["Sun"])

print("\n---\n")
print(stars["Betelgeuse"])

# Plot the size vs Luminosity
plotSizeLuminosity(stars)