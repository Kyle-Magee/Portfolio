from random import choice, random


class Animal:

    def __init__(self, ecosystem, prey, predators, species, birth_position=None):
        """
        ecosystem   environment which animal lives in (list)
        prey        animals that are on the menu (list)
        predators   animals that try to eat thine (list)
        species     the species the animal belongs to (str)
        """
        self._eco = ecosystem
        self._prey = prey
        self._predators = predators
        self._species = species
        available_spaces = [position for position, animal in enumerate(self._eco) if animal == None]
        if birth_position:
            self._eco[birth_position] = self
        else:
            self._eco[choice(available_spaces)] = self
        self._current_position = ecosystem.index(self)
        self._strength = random()
        self._gender = choice(['Male', 'Female'])
        self._able_to_reproduce = True
        self._reproduction_timer = 0
        self._reproduction_timer_max = 250

    def get_direction(self):
        """ Decide in what direction, if any the animal will move in """

        direction = choice([-1, 1, 0, 0])
        current_pos = self._current_position
        if direction + current_pos >= len(self._eco):
            destination = 0
        elif direction + current_pos < 0:
            destination = -1
        elif direction == 0:
            destination = None
        else:
            destination = direction + current_pos
        
        return destination

    def move(self, destination):
        """ Animal moves to adjacent place in list, if moving past limit, allow reset"""

        ecosystem = self._eco
        if destination == None:
            return None
        if ecosystem[destination]:
            same_species_different_sex = (ecosystem[destination]._species == self._species and 
                                          ecosystem[destination]._gender != self._gender)
            same_species_same_sex = (ecosystem[destination]._species == self._species and
                                     ecosystem[destination]._gender == self._gender)
            prey_found = ecosystem[destination]._species in self._prey
            oh_fuck_its_a_predator = ecosystem[destination]._species in self._predators
            theres_nothing_there = False
        else:
            prey_found = None
            same_species_different_sex = None
            oh_fuck_its_a_predator = None
            same_species_same_sex = None
            theres_nothing_there = True

        current_pos = self._current_position
        if prey_found or theres_nothing_there:
            ecosystem[current_pos] = None
            ecosystem[destination] = self
            self.update_current_position()
        elif oh_fuck_its_a_predator:
            ecosystem[current_pos] = None
        elif same_species_same_sex:
            if self.strength_check(ecosystem[destination]): 
                ecosystem[current_pos] = None
                ecosystem[destination] = self
                self.update_current_position()
            else:
                ecosystem[current_pos] = None
        elif same_species_different_sex:
            self.reproduce()

    def strength_check(self, other):
        return self._strength >= other._strength

    def reproduce(self):
        """ Instantiante a new animal in a random, empty space; if any """

        # Check for empty space
        available_spaces = [position for position, animal in enumerate(self._eco) if animal == None]
        if available_spaces and self.reproduction_check(): 
            baby_destination = choice(available_spaces)
            if self._species == 'bear': 
                constructor = Bear
            else: 
                constructor = Fish
            self._eco[baby_destination] = constructor(self._eco, birth_position=baby_destination)
            self.reproduction_off()

    def update_current_position(self):
        self._current_position = self._eco.index(self)

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
        super().__init__(eco, ['fish'], ['Nothing'], 'bear', birth_position=None)

    def __repr__(self):
        return str(self._gender)[0] + '.Bear'


class Fish(Animal):

    def __init__(self, eco, birth_position=None):
        super().__init__(eco, [0], ['bear'], 'fish', birth_position=None)

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
        return self._eco

    def headcount(self):
        bears = 0
        fishes = 0
        for animal in self._eco:
            if animal and animal._species == 'bear':
                bears += 1
            elif animal and animal._species == 'fish': 
                fishes += 1
        return('Bears: ', bears, 'Fishes: ', fishes)
