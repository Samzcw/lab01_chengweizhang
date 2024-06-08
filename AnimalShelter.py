from Animal import Animal
class AnimalShelter:
    def __init__(self):
        self.animalshelter = {}

    def addAnimal(self, animal):
        if self.doesAnimalExist(animal) == False:
            if self.animalshelter.get(animal.species) == None:
                self.animalshelter[animal.species] = [animal]
            else:
                self.animalshelter[animal.species].append(animal)

    def removeAnimal(self, animal):
        if self.doesAnimalExist(animal) == True:
            self.animalshelter[animal.species].remove(animal)

    def removeSpecies(self, species):
        if species == None:
            if species in self.animalshelter:
                return self.animalshelter.pop(species)
        else:
            if species.upper() in self.animalshelter:
                return self.animalshelter.pop(species.upper())

    def getAnimalsBySpecies(self, species):
        if species == None:
            if self.animalshelter.get(species) == None:
                return ""
            else:
                a = []
                for animal in self.animalshelter.get(species):
                    a.append(animal.toString())
                return '\n'.join(a)
        else:
            if self.animalshelter.get(species.upper()) == None:
                return ""
            else:
                a = []
                for animal in self.animalshelter.get(species.upper()):
                    a.append(animal.toString())
                return '\n'.join(a)

    def doesAnimalExist(self, animal):
        if self.animalshelter.get(animal.species) == None:
            return False
        else:
            if animal in self.animalshelter.get(animal.species):
                return True
            else:
                return False
