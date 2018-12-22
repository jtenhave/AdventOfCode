# Find the ten digits after a given number of generations.

desired_recipe_count = 74501
final_recipe_count = desired_recipe_count + 10

recipes = [3, 7]

current_recipe_a = 0
current_recipe_b = 1

recipe_count = 2
while recipe_count < final_recipe_count:
	recipe_a = recipes[current_recipe_a]
	recipe_b = recipes[current_recipe_b]

	total = recipe_a + recipe_b
	for d in str(total):
		recipes.append(int(d))

	recipe_count = len(recipes)
	current_recipe_a = current_recipe_a + recipe_a + 1
	current_recipe_b = current_recipe_b + recipe_b + 1

	current_recipe_a = current_recipe_a % recipe_count
	current_recipe_b = current_recipe_b % recipe_count

recipes = recipes[desired_recipe_count:]
print(recipes)
