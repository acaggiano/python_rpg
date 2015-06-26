import math
import random

class Character:
	"""Create Character Class"""
	stats = {}
	def __init__(self, new_name):
		self.name = new_name
		
	def basic_attack(self, defender):
		damage = self.atk - defender.dfs
		hit_chance = self.spd/defender.spd
		percent = random.random()
		if(hit_chance < percent):
			print("{} missed!".format(self.name))
			return
		crit = random.randrange(self.luck, 100, 5)
		if damage <= 0:
			print("The attack has no effect.")
			damage = 0
		else:
			if(crit > 85):
				damage = int(damage * 1.5)
				print("Critical Hit!")
			defender.hp = defender.hp - damage
			print("{} did {} damage!".format(self.name, damage))

	def magic_attack(self, defender):
		damage = self.magic_atk - defender.dfs
		crit = random.randrange(self.luck, 100, 5)
		if damage <= 0:
			print("The attack has no effect.")
			damage = 0
		else:
			if(crit > 85):
				damage = damage * 1.5
				print("Critical Hit!")
			defender.hp = defender.hp - damage
			print("{} did {} damage!".format(self.name, damage))

	def defend(self):
		pass


class Player(Character):
	"""Create Player Class"""
	def __init__(self, *args, **kwargs):
		self.base_hp = 10
		self.lvl = 1
		self.exp = 0
		super().__init__(*args, **kwargs)

	def stats_init(self):
		self.hp = self.stats['BASE_HP']
		self.mp = self.stats['BASE_MP']
		self.atk = self.stats['BASE_ATK']
		self.dfs = self.stats['BASE_DFS']
		self.magic_atk = self.stats['BASE_MAGIC_ATK']
		self.spd = self.stats['BASE_SPD']
		self.luck = self.stats['BASE_LUCK']

	def level_up(self, modifiers):
		print()
		print("*--- {} LEVELED UP! ---*".format(self.name))
		print("Level {} stats:".format(self.lvl))
		print("\tHP: ", self.stats['BASE_HP'])
		print("\tMP: ", self.stats['BASE_MP'])
		print("\tAttack: ", self.stats['BASE_ATK'])
		print("\tDefense: ", self.stats['BASE_DFS'])
		print("\tMagic Attack: ", self.stats['BASE_MAGIC_ATK'])
		for stat, value in self.stats.items():
			self.stats[stat] = value + modifiers[stat]
		self.lvl += 1
		print("Level {} stats:".format(self.lvl))
		print("\tHP: ", self.stats['BASE_HP'])
		print("\tMP: ", self.stats['BASE_MP'])
		print("\tAttack: ", self.stats['BASE_ATK'])
		print("\tDefense: ", self.stats['BASE_DFS'])
		print("\tMagic Attack: ", self.stats['BASE_MAGIC_ATK'])
		print("*----------------------------------*")
		print()

	def check_level_up(self):
		levels = [100, 250, 500, 1200]
		for value in levels:
			if self.exp >= value:
				self.level_up(self.modifiers)
				levels.remove(value)
				break

	def calculate_experience(self, enemies):
		for enemy in enemies:
			self.exp = self.exp + enemy.exp

class Fighter(Player):
	"""Defines Fighter Class"""
	def __init__(self, *args, **kwargs):
		self.class_type = "Fighter"
		self.weapon = "sword"
		self.stats['BASE_HP'] = 12
		self.stats['BASE_MP'] = 2
		self.stats['BASE_ATK'] = 10
		self.stats['BASE_DFS'] = 5
		self.stats['BASE_MAGIC_ATK'] = 2
		self.stats['BASE_SPD'] = 4
		self.stats['BASE_LUCK'] = 6
		self.modifiers = {'BASE_HP': 4, 'BASE_MP': 1, 'BASE_ATK': 2, 'BASE_DFS': 3, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 1, 'BASE_LUCK': 1}
		self.stats_init()
		super().__init__(*args, **kwargs)
		
class Mage(Player):
	"""Defines Mage Class"""
	def __init__(self, *args, **kwargs):
		self.class_type = "Mage"
		self.weapon = "wand"
		self.lvl = 1
		self.stats['BASE_HP'] = 10
		self.stats['BASE_MP'] = 8
		self.stats['BASE_ATK']  = 5
		self.stats['BASE_DFS'] = 4
		self.stats['BASE_MAGIC_ATK'] = 12
		self.stats['BASE_SPD'] = 7
		self.stats['BASE_LUCK'] = 5
		self.modifiers = {'BASE_HP': 2, 'BASE_MP': 4, 'BASE_ATK': 1, 'BASE_DFS': 3, 'BASE_MAGIC_ATK': 3, 'BASE_SPD': 2, 'BASE_LUCK': 1}
		self.stats_init()
		super().__init__(*args, **kwargs)


class Rogue(Player):
	"""Defines Rogue Class"""
	def __init__(self, *args, **kwargs):
		self.class_type = "Rogue"
		self.weapon = "dagger"
		self.lvl = 1
		self.stats['BASE_HP'] = 10
		self.stats['BASE_MP'] = 4
		self.stats['BASE_ATK']  = 7
		self.stats['BASE_DFS'] = 4
		self.stats['BASE_MAGIC_ATK'] = 7
		self.stats['BASE_SPD'] = 10
		self.stats['BASE_LUCK'] = 10
		self.modifiers = {'BASE_HP': 2, 'BASE_MP': 2, 'BASE_ATK': 2, 'BASE_DFS': 1, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 3, 'BASE_LUCK': 3}
		self.stats_init()
		super().__init__(*args, **kwargs)


class Enemy(Character):
	"""Create Enemy"""
	def __init__(self, new_name):
		super().__init__(new_name)
		
class Slime(Enemy):
	"""Create Beast Enemy"""
	def __init__(self):
		self.hp = 10
		self.mp = 0
		self.atk = 7
		self.dfs = 4
		self.spd = 15
		self.luck = 1
		self.exp = 50
		super().__init__("Slime")

class Item:
	"""Define item class"""
	def __init__(self):
		self.modifiers = {}
		self.name = ""
		self.type = ""

class Weapon(Item):
	"""Define Weapon Item"""
	def __init__(self):
		self.type = "weapon"
		super(Weapon, self).__init__()

def character_create():
	name = input("Hello brave adventurer, what is your name? : ")
	print()
	print("1. Fighter\n2. Mage\n3. Rogue")
	print()
	
	chosen = False
	while not chosen:
		class_choice = input("Please choose a class: ")
		print()
		if class_choice == "1":
			return Fighter(name)
			chosen = True
		elif class_choice == "2":
			return Mage(name)
			chosen = True
		elif class_choice == "3":
			return Rogue(name)
			chosen = True
		else:
			print("Invalid input. Please pick 1, 2, 3")
			continue

def turn_order(combatants):
	speed_order = sorted(combatants, key=lambda character: character.spd, reverse=True)

	return speed_order

def check_health(party):

	for person in party:
		if(person.hp > 0):
			return True

	return False

def pick_target(enemies):

	print("Which enemy do you target?")
	print()

	for idx, enemy in enumerate(enemies):
		print("{}. {} HP: {}".format(idx, enemy.name, enemy.hp))

	valid_target = False

	while not valid_target:
		target = input("Pick Target: ")
		try:
			target = int(target)
			valid_target = 0 <= target <= idx
		except ValueError:
			pass
		if not valid_target:
			print("Invalid Target")
		continue
	else:
		return target
	
def battle(all_combatants, party, enemies):
	all_combatants = turn_order(all_combatants)

	party_alive = True
	enemies_alive = True

	enemies_defeated = []

	while party_alive and enemies_alive:

		print("*-------------------*")
		for person in party:
			print("{}'s HP: {}".format(person.name, person.hp))
			print("{}'s MP: {}".format(person.name, person.mp))
			print("-------------------")
		for enemy in enemies:
			print("{}s HP: {}".format(enemy.name, enemy.hp))
			print("{}s MP: {}".format(enemy.name, enemy.mp))
			print("-------------------")
		print("*-------------------*")
		print()


		for person in all_combatants:
			if person in party and person.hp > 0:
				print(person.name, "\b's Turn")
				print("1. Attack\n2. Magic Attack *MP Cost: 2*\n3. Defend\n4. Stand there and do nothing")

				valid_input = False

				while not valid_input:
					choice = input("Enter command number: ")
					valid_input = choice in ["1", "2", "3", "4"]
					print() 
					if choice == "1":
						player_target = pick_target(enemies)
						print("You attack with your {}!".format(person.weapon))
						person.basic_attack(enemies[player_target])
						if enemies[player_target].hp <= 0:
							enemies[player_target].hp = 0
							print("{} defeated {}".format(person.name, enemies[player_target].name))
							enemies_defeated.append(enemies[player_target])
							enemies.pop(player_target)
					elif choice == "2":
						if(person.mp >= 2):
							player_target = pick_target(enemies)
							print("You cast a ball of magic energy at the beast!")
							person.magic_attack(enemies[player_target])
							person.mp = person.mp - 2
							if enemies[player_target].hp <= 0:
								enemies[player_target].hp = 0
								print("{} defeated {}".format(person.name, enemies[player_target].name))
								enemies_defeated.append(enemies[player_target])
								enemies.pop(player_target)
						else:
							print("You don't have enough mp for that!")
							continue
					elif choice == "3":
						print("You ready yourself for an attack.")
						person.dfs = person.dfs * 1.5
					elif choice == "4":
						print("You stand there and do nothing.")
					else:
						print("Input not recoginized!")
						continue
				enemies_alive = check_health(enemies)
				if not enemies_alive:
					break

			elif person in enemies and person.hp > 0:
				print(person.name, "\b's Turn")
				target = random.randrange(0, len(party))
				valid_target = party[target].hp > 0

				while not valid_target:
					target = random.randrange(0, len(party))
					valid_target = party[target].hp > 0
				else:
					print(person.name, "attacks", party[target].name)
					person.basic_attack(party[target])
					target = random.randrange(0, len(party))

				party_alive = check_health(party)
				if not party_alive:
					break

	else:
		if not party_alive and enemies_alive:
			print("You're party has died...")
		elif not enemies_alive and party_alive:
			print("All enemies have been defeated!")
			for person in party:
				person.calculate_experience(enemies_defeated)
				person.check_level_up()
		else:
			print("Double KO?")
	
def main():

	player = character_create()
	player.stats_init()

	friend = Mage("Dude")

	print("You are " + player.name + ", the " + player.class_type)
	print()
	print("As you travel throught the forest you encounter a fork in the road.\nWhich way do you go?")
	print("1. Left\n2. Right")
	print()
	direction = input("Pick a path: ")
	print()
	if direction == "1":
		back = False
		while not back:
			slime = Slime()
			slime2 = Slime()

			print("Enemies Appear!")
			battle([player, friend, slime, slime2], [player, friend], [slime, slime2])
			if player.hp > 0:
				print("Behind the beast was a dead end. Do you want to turn back?")
				print("1. Yes\n2. No")
				print()
				go_back = input("Go back? : ")
				if go_back == "1":
					print("As you head back you see another adventurer walking away from the other path with boundless treasure, too bad you didn't go that way.")
					back = True
				elif go_back == "2":
					continue
			else:
				break
	elif direction == "2":
		print("You discover boundless treasure and will never have to work another day of you life!")

	print("Game over.")

if __name__ == '__main__':
	main()
	



	