def move_player(position, direction):
    x, y = position

    if direction == "up":
        y += 1
    elif direction == "down":
        y -= 1
    elif direction == "right":
        x += 1
    elif direction == "left":
        x -= 1
    else:
        print("Invalid direction!")
        return position  

    return (x, y)

x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))
direction = input("Enter direction : ")

new_position = move_player((x, y), direction)

print("New position:", new_position)