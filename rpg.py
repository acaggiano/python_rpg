import math
import random

class Character:
	"""Create Character Class"""
	def __init__(self):
		self.name = ""
		self.stats = {}

	def basic_attack(self, defender):
		damage = self.atk - defender.dfs
		type(damage)
		if damage <= 0:
			print("The attack has no effect.")
			damage = 0
		else:
			defender.hp = defender.hp - damage
			print(self.name + " did " + str(damage) + " damage!")

	def magic_attack(self, defender):
		damage = self.magic_atk - defender.dfs
		if damage <= 0:
			print("The attack has no effect.")
			damage = 0
		else:
			defender.hp = defender.hp - damage
			print(self.name + " did " + str(damage) + " damage!")

	def defend(self):
		pass


class Player(Character):
	"""Create Player Class"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.base_hp = 10
		self.lvl = 1
		self.exp = 0

	def stats_reset(self):
		self.hp = self.stats['BASE_HP']
		self.mp = self.stats['BASE_MP']
		self.atk = self.stats['BASE_ATK']
		self.dfs = self.stats['BASE_DFS']
		self.magic_atk = self.stats['BASE_MAGIC_ATK']
		self.spd = self.stats['BASE_SPD']
		self.luck = self.stats['BASE_LUCK']

	def level_up(self, modifiers):
		self.lvl += 1
		print()
		print("*------------ LEVEL UP ------------*")
		print("Level " + str(self.lvl)+ " stats:")
		print("\tHP: ", self.stats['BASE_HP'])
		print("\tMP: ", self.stats['BASE_MP'])
		print("\tAttack: ", self.stats['BASE_ATK'])
		print("\tDefense: ", self.stats['BASE_DFS'])
		print("\tMagic Attack: ", self.stats['BASE_MAGIC_ATK'])
		for stat, value in self.stats.items():
			self.stats[stat] = value + modifiers[stat]

		print("Level " + str(self.lvl)+ " stats: ")
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

class Fighter(Player):
	"""Defines Fighter Class"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.class_type = "fighter"
		self.weapon = "sword"
		self.stats['BASE_HP'] = self.base_hp + 2
		self.stats['BASE_MP'] = 2
		self.stats['BASE_ATK'] = 10
		self.stats['BASE_DFS'] = 5
		self.stats['BASE_MAGIC_ATK'] = 2
		self.stats['BASE_SPD'] = 4
		self.stats['BASE_LUCK'] = 6
		self.modifiers = {'BASE_HP': 4, 'BASE_MP': 1, 'BASE_ATK': 2, 'BASE_DFS': 3, 'BASE_MAGIC_ATK': 2, 'BASE_SPD': 1, 'BASE_LUCK': 1}
		
class Mage(Player):
	"""Defines Mage Class"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.class_type = "mage"
		self.weapon = "wand"
		self.lvl = 1
		self.stats['BASE_HP'] = self.base_hp + 2
		self.stats['BASE_MP'] = 8
		self.stats['BASE_ATK']  = 5
		self.stats['BASE_DFS'] = 4
		self.stats['BASE_MAGIC_ATK'] = 12
		self.stats['BASE_SPD'] = 7
		self.stats['BASE_LUCK'] = 5
		self.modifiers = {'BASE_HP': 2, 'BASE_MP': 4, 'BASE_ATK': 1, 'BASE_DFS': 3, 'BASE_MAGIC_ATK': 3, 'BASE_SPD': 2, 'BASE_LUCK': 1}

class Beast(Character):
	"""Create Beast Enemy"""
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.name = "The Beast"
		self.hp = 10
		self.mp = 0
		self.atk = 7
		self.dfs = 4
		self.spd = 3
		self.luck = 1
		self.exp = 50

def character_create():
	name = input("Hello brave adventurer, what is your name? : ")
	print()
	print("1. Fighter\n2. Mage")
	print()
	
	chosen = False
	while not chosen:
		class_choice = input("Please choose a class: ")
		print()
		if class_choice == "1":
			return Fighter(), name
			chosen = True
		elif class_choice == "2":
			return Mage(), name
			chosen = True
		else:
			print("Invalid input. Please pick 1 or 2")
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

	for enemy in enemies:
		print(enemies.index(enemy), "\b.", enemy.name, "HP:", enemy.hp)

	valid_target = False

	while not valid_target:
		target = int(input("Pick Target: "))
		valid_target = target >= 0 and target <= len(enemies)-1
		continue
	else:
		return target
	
def battle(all_combatants, party, enemies):
	all_combatants = turn_order(all_combatants)

	party_alive = True
	enemies_alive = True

	while party_alive and enemies_alive:

		print("*-------------------*")
		for person in party:
			print(person.name + "\'s HP: " + str(person.hp))
			print(person.name + "\'s MP: " + str(person.mp))
			print("|-------------------|")
		for enemy in enemies:
			print(enemy.name + "\'s HP: " + str(enemy.hp))
			print(enemy.name + "\'s MP: " + str(enemy.mp))
			print("|-------------------|")
		print("*-------------------*")
		print()


		for person in all_combatants:
			print(person.name, "\b's Turn")
			if person in party and person.hp > 0:
				print("1. Attack\n2. Magic Attack *MP Cost: 2*\n3. Defend\n4. Stand there and do nothing")
				choice = input("Enter command number: ")
				print()
				if choice == "1":
					player_target = pick_target(enemies)
					print("You attack with your " + person.weapon + "!")
					person.basic_attack(enemies[player_target])
					if enemies[player_target].hp <= 0:
						enemies[player_target].hp = 0
						print(person.name, "defeated", enemies[player_target].name)
				elif choice == "2":
					if(person.mp >= 2):
						player_target = pick_target(enemies)
						print("You cast a ball of magic energy at the beast!")
						person.magic_attack(enemies[player_target])
						person.mp = person.mp - 2
						if enemies[player_target].hp <= 0:
							enemies[player_target].hp = 0
							print(person.name, "defeated", enemies[player_target].name)
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
			elif person in enemies and person.hp > 0:
				target = random.randrange(0, len(party))
				print(person.name, "attacks", party[target].name)
				person.basic_attack(party[target])

		party_alive = check_health(party)
		enemies_alive = check_health(enemies)

	else:
		if not party_alive and enemies_alive:
			print("You're party has died...")
		elif not enemies_alive and party_alive:
			print(enemies_alive)
			print("All enemies have been defeated!")
		else:
			print("Double KO?")
		
	# while enemy.hp > 0 and player.hp > 0:
	# 	print("*--------------------*")
	# 	print("|----Your HP: ", end = "")
	# 	if player.hp < 10:
	# 		print(" ", end = "")
	# 	print(str(player.hp) + "-----|")
	# 	print("|----Your MP: ", end = "")
	# 	if player.mp < 10:
	# 		print(" ", end = "")
	# 	print(str(player.mp) + "-----|")
	# 	print("|----Enemy HP: ", end = "")
	# 	if enemy.hp < 10:
	# 		print(" ", end = "")
	# 	print(str(enemy.hp) + "----|")
	# 	print("|----Enemy MP: ", end = "")
	# 	if enemy.mp < 10:
	# 		print(" ", end = "")
	# 	print(str(enemy.mp) + "----|")
	# 	print("*--------------------*")
	# 	print()
	# 	print("1. Attack\n2. Magic Attack *MP Cost: 2*\n3. Defend\n4. Stand there and do nothing")
	# 	print()
	# 	choice = input("Enter command number: ")
	# 	print()
	# 	if choice == '1':
	# 		print("You attack the beast with your " + player.weapon + "!")
	# 		player.basic_attack(enemy)
	# 		if enemy.hp <= 0:
	# 			break
	# 	elif choice == "2":
	# 		if(player.mp >= 2):
	# 			print("You cast a ball of magic energy at the beast!")
	# 			player.magic_attack(enemy)
	# 			player.mp = player.mp - 2
	# 			if enemy.hp <= 0:
	# 				break
	# 		else:
	# 			print("You don't have enough mp for that!")
	# 			continue
	# 	elif choice == "3":
	# 		print("You ready yourself for an attack.")
	# 		player.dfs = player.dfs * 1.5
	# 	elif choice == "4":
	# 		print("You stand there and do nothing.")
	# 	else:
	# 		print("Input not recoginized! Please enter y or n.\n")
	# 		continue

	# 	print(enemy.name + " claws at your face!")
	# 	enemy.basic_attack(player)
	# 	player.dfs = player.stats['BASE_DFS']

	# if enemy.hp < 0:
	# 		enemy.hp = 0
	# if player.hp < 0:
	# 	player.hp = 0

	# if enemy.hp == 0:
	# 	print("You've defeated the enemy!")
	# 	player.exp += enemy.exp
	# 	print("You've gained " + str(enemy.exp) + " exp!\nTotal Exp: " + str(player.exp))
	# 	player.check_level_up()
	# elif player.hp == 0:
	# 	print("You've been killed.")

def main():

	player, player.name = character_create()
	player.stats_reset()

	friend = Mage()
	friend.name = "Dude"
	friend.stats_reset()

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
			enemy = Beast()
			enemy2 = Beast()
			print("A wild beast appears!")
			battle([player, friend, enemy, enemy2], [player, friend], [enemy, enemy2])
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
	



	