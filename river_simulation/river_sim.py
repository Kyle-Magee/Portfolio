from random import choice, random


class Animal:

    def __init__(self, ecosystem, prey, predators, species,
                 birth_position=None,
                 able_to_reproduce=True, reproduction_timer=0,
                 reproduction_timer_max=5, strength=random()):
        """
        ecosystem               environment which animal lives in (list)
        prey                    animals that are on the menu (list)
        predators               animals that try to eat thine (list)
        species                 the species the animal belongs to (str)
        gender                  gender of the particular animal (str)
        birth_position          index of the animal in the ecosystem (int)
        able_to_reproduce       animal's ability to produce new animals (bool)
        reproduction_timer      starting number for reproduction cooldown (int)
        reproduction_timer_max  reproduction cooldown time (int
        strength                animal's ability to fight (float)
        """
        self._eco = ecosystem
        self._prey = prey
        self._predators = predators
        self._species = species
        self._strength = strength
        self._gender = choice(['Male', 'Female'])
        self._able_to_reproduce = able_to_reproduce
        self._reproduction_timer = reproduction_timer
        self._reproduction_timer_max = reproduction_timer_max
        self._destination = None
        if birth_position:
            self._eco[birth_position] = self
        # Find empty locations in ecosystem
        else:
            empties = [position for position, animal in
                       enumerate(self._eco.get_eco()) if not(animal)]
            self._eco[choice(empties)] = self
        self._current_position = self._eco.get_eco().index(self)

    def get_direction(self):
        """ Decide in what direction, if any the animal will move in """

        direction = choice([-1, 1, 0, 0])
        current_pos = self._current_position
        if direction + current_pos >= len(self._eco.get_eco()):
            destination = 0
        elif direction + current_pos < 0:
            destination = -1
        elif direction == 0:
            destination = None
        else:
            destination = direction + current_pos

        return destination

    def compare_gender(self, animal):
        return self._gender == animal._gender

    def compare_species(self, animal):
        return self._species == animal._species

    def move_to_spot(self, destination):
        self._eco[self._current_position] = None
        self._eco[destination] = self
        self.update_current_position()

    def death(self):
        self._eco[self._current_position] = None

    def move(self, destination):
        """
            Animals move in accordance to the following behavior:
            Randomly move left, right or nowhere
            Animals of the same sex and species will fight for occupying a spot
            the loser dies.
            Predators will always kill prey
            Animals of the same species and opposite sex will spawn a
            new animal in a random available space
        """
        if not(destination):
            # If the animal isn't going anywhere
            return None
        animal = self._eco[destination]
        if isinstance(animal, Animal):
            mate = (self.compare_species(animal) and
                    not(self.compare_gender(animal)))
            fight = self.compare_species(animal) and self.compare_gender(animal)
            eat = isinstance(animal, self._prey)
            die = isinstance(animal, self._predators)
            nothing_found = False
        else:
            eat = False
            mate = False
            die = False
            fight = False
            nothing_found = True

        if eat or nothing_found:
            self.move_to_spot(destination)
        elif die:
            self.death()
        elif fight:
            if self.strength_check(animal):
                self.move_to_spot(destination)
            else:
                self.death()
        elif mate:
            self.reproduce()

    def strength_check(self, animal):
        return self._strength >= animal._strength

    def reproduce(self):
        """ Instantiante a new animal in a random, empty space; if any """
        # Check for empty space, loc = location
        empties = [loc for loc, animal in enumerate(self._eco) if not(animal)]
        if empties and self.reproduction_check():
            birthplace = choice(empties)
            animal = self._species
            self._eco[birthplace] = animal(self._eco, birth_position=birthplace)
            self.reproduction_off()

    def update_current_position(self):
        self._current_position = self._eco.get_eco().index(self)

    def reproduction_check(self):
        return self._able_to_reproduce

    def reproduction_off(self):
        self._able_to_reproduce = False

    def reproduction_update(self):
        if not(self._able_to_reproduce):
            if self._reproduction_timer < self._reproduction_timer_max:
                self._reproduction_timer += 1
            else:
                self.reproduction_on()

    def reproduction_on(self):
        self._able_to_reproduce = True


class Bear(Animal):

    def __init__(self, eco, birth_position=None):
        super().__init__(eco, Fish, type(None), Bear, birth_position=None)

    def __repr__(self):
        return str(self._gender)[0] + '.Bear'


class Fish(Animal):

    def __init__(self, eco, birth_position=None):
        super().__init__(eco, type(None), Bear, Fish, birth_position=None)

    def __repr__(self):
        return str(self._gender)[0] + '.Fish'


class Ecosystem:

    def __init__(self, size):
        self._eco = [None] * size
        self._size = size

    def time_step(self):
        for animal in self._eco:
            if animal:
                animal.reproduction_update()
                animal.move(animal.get_direction())

    def get_eco(self):
        return list(self._eco)

    def headcount(self):
        bears = 0
        fishes = 0
        for animal in self._eco:
            if animal and animal._species == 'bear':
                bears += 1
            elif animal and animal._species == 'fish':
                fishes += 1
        return('Bears: ', bears, 'Fishes: ', fishes)

    def __setitem__(self, j, animal):
        """
        Allow assingment of animals to ecosystem
        j   index
        """
        self._eco[j] = animal

    def __getitem__(self, j):
        """
        Allow indexing of the ecosystem
        j   index
        """
        return self._eco[j]


if __name__ == '__main__':
    from time import sleep
    e = Ecosystem(14)
    for i in range(6):
        Fish(e)
        Bear(e)
    while True:
        sleep(1)
        e.time_step()
        print(e.get_eco())