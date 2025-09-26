import datetime
class CricketPlayer:
    def __init__(self,fname,lname,birth_year,team):
        self.first_name=fname
        self.last_name=lname
        self.birth_year=birth_year
        self.team=team
        self.scores=[]
    def get_age(self):
        now=datetime.datetime.now()
        return now.year - self.birth_year
    def add_score(self,score):
        self.scores.append(score)
    def get_avg(self):
        return sum(self.scores)/len(self.scores)

virat=CricketPlayer('virat','kohli',1988,'india')
virat.add_score(90)
virat.add_score(10)
virat.add_score(80)
print(virat.get_age(),virat.get_avg())

david=CricketPlayer('david','warner',1986,'Australia')
david.add_score(20)
david.add_score(60)
david.add_score(50)
print(david.get_age(),david.get_avg())

#Task
# Avengers is a Marvel’s American Superheroes team, and if you are a fan of avengers, 
# recently you have learned about classes and objects in your python course. 
# Now you want to showcase your programming skills by representing the Avengers team using classes. 
# Create a class called Avenger and create these six superheroes using this class.

# super_heroes = ["Captain America", "Iron Man", "Black Widow", "Hulk", "Thor", "Hawkeye"]
# Your Avenger class should have these properties:

# Name
# Age
# Gender
# Super Power
# Weapon
# Captain America has Super strength, Iron Man has Technology, Black Widow is superhuman, 
# Hulk has Unlimited Strength, Thor has super Energy and Hawkeye has fighting skills as superpowers.

# Weapons: Shield, Armor, Batons, No Weapon for hulk, Mjölnir, Bow, and Arrows

# Create methods to get the information about each superhero

# Create a method is_leader() which will tell if the superhero is a leader or not.


class Avengers:
    names = ["Captain America", "Iron Man", "Black Widow", "Hulk", "Thor", "Hawkeye"]
    superpowers = ["Super strength", "Technology", "Superhuman", "Unlimited Strength", "Super Energy", "Fighting skills"]
    weapons = ["Shield", "Armor", "Batons", "No weapon", "Mjölnir", "Bow and Arrows"]
    ages = [110, 40, 35, 34, 10000, 30]
    genders = ['M', 'M', 'F', 'M', 'M', 'M']

    avengers = []
    for name, age, gender, superpower, weapon in zip(names, ages, genders, superpowers, weapons):
        avengers.append([name, age, gender, superpower, weapon])

    def __init__(self, name, age, gender, superpower, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.superpower = superpower
        self.weapon = weapon
        self.is_leader_flag = False

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_superpower(self):
        return self.superpower

    def get_weapon(self):
        return self.weapon

    def get_info(self):
        return f"""
        Avenger Profile:

        Name: {self.name}
        Age: {self.age}
        Gender: {self.gender}

        Has {self.weapon} weapon and {self.superpower} superpower.
        """

    def is_leader(self):
        return self.is_leader_flag

    def make_leader(self):
        self.is_leader_flag = True
        return f"{self.name} is the new leader of the Avengers"

    def remove_leader(self):
        self.is_leader_flag = False
        return f"{self.name} is removed from the leader role"

    def __str__(self):
        return f"Avenger({self.name}, {self.age}, {self.gender}, {self.superpower}, {self.weapon})"


# Example usage:
ironman = Avengers("Iron Man", 40, "M", "Technology", "Armor")
print(ironman.get_info())
print(ironman.make_leader())
