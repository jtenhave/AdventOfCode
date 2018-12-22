# Find the number of recipes before a given score sequence.

desired_recipe_seq= "074501"
desired_recipe_seq_len = len(desired_recipe_seq)

recipes = [3, 7, 1, 0, 1, 0]

current_recipe_a = 4
current_recipe_b = 3

recipe_count = 6

test_seq = "000000"
while True:
	recipe_a = recipes[current_recipe_a]
	recipe_b = recipes[current_recipe_b]

	total = recipe_a + recipe_b

	if total >= 10:
		lowest = total - 10
		
		recipes.append(1)
		test_seq = test_seq[1:]
		test_seq += "1"

		if test_seq == desired_recipe_seq:
			break;

		recipes.append(lowest)
		test_seq = test_seq[1:]
		test_seq += str(lowest)

	else:
		recipes.append(total)
		test_seq = test_seq[1:]
		test_seq += str(total)

	if test_seq == desired_recipe_seq:
		break;

	recipe_count = len(recipes)
	current_recipe_a += recipe_a + 1
	current_recipe_b += recipe_b + 1
	if current_recipe_a >= recipe_count:
		current_recipe_a = current_recipe_a - recipe_count

	if current_recipe_b >= recipe_count:
		current_recipe_b = current_recipe_b - recipe_count

print(len(recipes) - desired_recipe_seq_len)
