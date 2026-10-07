year = int(input())
colors = ["зеленый", "красный", "желтый", "белый", "черный"]
animals = ["крысы", "коровы", "тигра", "зайца", "дракона", "змеи", "лошади", "овцы", "обезьяны", "курицы", "собаки", "свиньи"]
offset = (year - 1984) % 60
color = colors[offset // 12]
animal = animals[offset % 12]
print(f"год {color} {animal}")