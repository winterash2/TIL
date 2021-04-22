input_list = input()

base = input_list[0]
prev = base
count = 0

for i in input_list:
    if i == prev:
        continue
    else:
        prev = i
        if i != base:
            count += 1

print(count)