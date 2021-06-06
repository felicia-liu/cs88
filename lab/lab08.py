## Inheritance ##

# Quidditch

class QuidditchPlayer:
    def __init__(self, name, base_energy):
        """
        QuidditchPlayers have a name, and begin with base_energy.
        """
        self.name = name
        self.base_energy = base_energy

    def energy(self):
        return self.base_energy

class Beater(QuidditchPlayer):
    role = "bludgers"

    def energy(self, time):
        """
        Returns the amount of energy left after playing for time minutes.
        After playing for time minutes, Beaters lose their base energy level
        divided by the number of minutes. If time is 0, catch the ZeroDivisionError
        and print "You can't divide by zero!" instead.
        >>> fred = Beater("Fred Weasley", 640)
        >>> fred.energy(40)
        624.0
        >>> fred.energy(0)
        You can't divide by zero!
        """
        if time == 0:
            print("You can't divide by zero!")
        else:
            energy_left = self.base_energy - self.base_energy/time
            return energy_left

class Chaser(QuidditchPlayer):
    role = "score"
    energy_expended = 20

    def __init__(self, name, base_energy, goals):
        """
        Chasers have a name, score goals, and begin with base_energy.
        """
        self.name = name
        self.base_energy = base_energy
        self.goals = goals


    def energy(self, time):
        """
        Returns the amount of energy left after playing for time minutes. For every goal
        they score, they use energy_expended units of energy. In addition, they also use
        10% of energy_expended if the number of minutes they have played is a multiple of 9.
        >>> katie = Chaser("Katie Bell", 230, 2)
        >>> katie.energy(20)
        190
        >>> ginny = Chaser("Ginny Weasley", 400, 3)
        >>> ginny.energy(45)
        338.0
        """
        if time % 9 == 0:
            expended = Chaser.energy_expended * self.goals + 0.1 * Chaser.energy_expended
            return self.base_energy - expended
        else:
            return self.base_energy - Chaser.energy_expended * self.goals

class Seeker(QuidditchPlayer):
    role = "snitch"
    energy_expended = 5

    def energy(self, time):
        """
        Returns the amount of energy after time minutes. Seekers expend energy_expended
        units of their energy for every minute they have been playing.
        >>> harry = Seeker("Harry Potter", 700)
        >>> harry.energy(30)
        550
        """
        expended = Seeker.energy_expended * time
        return self.base_energy - expended


class Keeper(QuidditchPlayer):
    role = "guard"
    energy_expended = 50

    def energy(self, time):
        """
        Returns the amount of energy after time minutes. If less than 30 minutes have
        passed, then Keepers do not lose any energy. If 30 minutes or more have passed,
        then Keepers expend 80% of their energy_expended units for every full 15
        minutes that pass.
        >>> oliver = Keeper("Oliver Wood", 380)
        >>> oliver.energy(45)
        260.0
        """
        if time < 30:
            return self.base_energy
        else:
            expended = 0.8 * Keeper.energy_expended * time/15
            return self.base_energy - expended
