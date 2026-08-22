import random, subprocess, os
width = 9
height = 9
mines_count = 10
mines = []
tries = []
nums = []
def clear():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
def flood_fill(start):
    queue = [start]
    visited = set(tries)
    while queue:
        x, y = queue.pop(0)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        tries.append((x, y))
        if (x, y) in nums:
            continue
        for i in range(-1, 2):
            for j in range(-1, 2):
                nx, ny = x + i, y + j
                if 0 < nx <= width and 0 < ny <= height:
                    if (nx, ny) not in visited:
                        queue.append((nx, ny))
clear()
print(f"Generating {width}x{height} grid ({width*height} tiles)")
def render():
    first = False
    for row in range(height+1):
        print(f"{row} " if row != 0 else "  ", end = "")
        if not first:
            for nums1 in range(1, width+1):
                print(f"{nums1} ", end = "")
            print()
            first = True
            continue
        for tile in range(width):
            if (tile+1, row) in tries:
                if (tile+1, row) in nums:
                    print(f"{nums.count((tile+1, row))} ", end = "")
                else:
                    print("o ", end = "")
            else:
                print("x ", end = "")
        print()
for mine in range(mines_count):
    x = random.randint(1, width)
    y = random.randint(1, height)
    while (x, y) in mines:
        x = random.randint(1, width)
        y = random.randint(1, height)
    mines.append((x, y))
    for i in range(-1, 2):
        for j in range (-1, 2):
            if (0 < x+i <= width and 0 < y+j <= height) or (i == 0 and j == 0):
                nums.append((i+x, j+y))
while True:
    render()
    coords = str(input("Enter coordinates (x, y): "))
    coords = coords.replace(",", "").split()
    coords = (int(coords[0]), int(coords[1]))
    if (int(coords[0]) ,int(coords[1])) in mines:
        print("There was a mine! Watch out")
        break
    else:
        flood_fill(coords)
        clear()