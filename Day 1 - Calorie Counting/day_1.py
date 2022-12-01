# https://adventofcode.com/2022/day/1
#
# I just noticed that it is irrelevant to know the elf-ids...
# My code is way longer than it needs to be. In summary: ugly but functional ^^


# This will be the elf carrying the most calories
master_elf = 0
master_elf_calories = 0

# This one tries its best
master_elf2 = 0
master_elf2_calories = 0

# This elf also carries something
master_elf3 = 0
master_elf3_calories = 0


# Read inventory list
foodbox = []
with open('input.txt') as inventory_file:
    foodbox = inventory_file.readlines()


current_elf = 1
calorie_count = 0
for snac in foodbox:
    snac = snac.rstrip()
    
    if not snac == '':
        calorie_count += int(snac)
    else:
        if calorie_count > master_elf3_calories:
            # Better than no 3
            if not calorie_count > master_elf2_calories:
                master_elf3 = current_elf
                master_elf3_calories = calorie_count
            else:
                # Better than no 2
                master_elf3 = master_elf2
                master_elf3_calories = master_elf2_calories
                if not calorie_count > master_elf_calories:
                    master_elf2 = current_elf
                    master_elf2_calories = calorie_count
                else:
                    # Better than no 1
                    master_elf2 = master_elf
                    master_elf2_calories = master_elf_calories

                    master_elf = current_elf
                    master_elf_calories = calorie_count

        calorie_count = 0
        current_elf = current_elf + 1

print(f'Elf no. {master_elf} is contributing the most by carrying '
      f'{master_elf_calories} calories!')
print(f'Elf no. {master_elf2} is also contributing much by carrying '
      f'{master_elf2_calories} calories!')
print(f'Elf no. {master_elf3} tries his best much by carrying '
      f'{master_elf3_calories} calories!')
print()
print(f'The TOP-3 are carrying a total of '
      f'{master_elf_calories + master_elf2_calories + master_elf3_calories} calories!')
