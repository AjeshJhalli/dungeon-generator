import pygame
import random


ROOM_COLOUR = (0, 0, 255)
DOOR_COLOUR = (255, 0, 0)
ROOM_WIDTH = 20
DOOR_WIDTH = 4

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3


def main():
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    
    running = True

    rooms, doors = generate_dungeon(200)
    print(len(rooms))

    for room in rooms:
        render_room(window, room[0], room[1])

    for door in doors:
        render_door(window, door)

    pygame.display.update()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


def generate_dungeon(num_rooms):

    # Add doors in after placing rooms together randomly

    rooms = [(0, 0)]

    # A list of rooms that should be considered for branching off of
    available_rooms = [(0, 0)]

    # The pair indexes will be in the stucture of (room1, room2, where room2 is relative to room1)
    # (room1, room2, right) means room2 is to the right of room1
    doors = []

    while len(rooms) < num_rooms:

        room_index = random.randint(0, len(available_rooms) - 1)

        # [right, down, left, up]
        generate_rooms = [0, 1, 2, 3]

        # Check what neighbours rooms[room_index] has
        # And then stop new neighbour rooms from being generated there

        room = available_rooms[room_index]
        x = room[0]
        y = room[1]

        if (x + 1, y) in rooms:
            generate_rooms.remove(0)

        if (x, y + 1) in rooms:
            generate_rooms.remove(1)

        if (x - 1, y) in rooms:
            generate_rooms.remove(2)

        if (x, y - 1) in rooms:
            generate_rooms.remove(3)

        if len(generate_rooms) == 0:
            available_rooms.remove(room)
            continue

        print('Generate rooms: ', generate_rooms)
        neighbour_choice = random.choice(generate_rooms)

        if neighbour_choice == 0:
            neighbour = (x + 1, y)
            direction = 0
        elif neighbour_choice == 1:
            neighbour = (x, y + 1)
            direction = 1
        elif neighbour_choice == 2:
            neighbour = (x - 1, y)
            direction = 2
        elif neighbour_choice == 3:
            neighbour = (x, y - 1)
            direction = 3

        doors.append((room, direction))

        rooms.append(neighbour)
        available_rooms.append(neighbour)

    """
    rooms_with_doors = [(False, False, False, False, room[0], room[1]) for room in rooms]

    for pair in pair_indexes:
        room1 = rooms[pair[0]]
        room2 = rooms[pair[1]]
        if direction == 0 and not rooms_with_doors[pair]:
            room1_with_door = ()
    """

    return rooms, doors


def render_room(window, x, y):

    render_x = x * ROOM_WIDTH + (DOOR_WIDTH * x)
    render_y = y * ROOM_WIDTH +  (DOOR_WIDTH * y)

    # Draw the room
    pygame.draw.rect(window, ROOM_COLOUR, (render_x, render_y, ROOM_WIDTH, ROOM_WIDTH))

    # Draw the doors if they exist
    """
    if right:
        pygame.draw.rect(window, DOOR_COLOUR, (render_x + ROOM_WIDTH - DOOR_WIDTH, render_y + (ROOM_WIDTH - DOOR_WIDTH) / 2, DOOR_WIDTH, DOOR_WIDTH))

    if down:
        pygame.draw.rect(window, DOOR_COLOUR, (render_x + (ROOM_WIDTH - DOOR_WIDTH) / 2, render_y + ROOM_WIDTH - DOOR_WIDTH, DOOR_WIDTH, DOOR_WIDTH))

    if left:
        pygame.draw.rect(window, DOOR_COLOUR, (render_x, render_y + (ROOM_WIDTH - DOOR_WIDTH) / 2, DOOR_WIDTH, DOOR_WIDTH))

    if up:
        pygame.draw.rect(window, DOOR_COLOUR, (render_x + (ROOM_WIDTH - DOOR_WIDTH) / 2, render_y, DOOR_WIDTH, DOOR_WIDTH))
    """

def render_door(window, door):

    room = door[0]
    direction = door[1]

    render_x, render_y = room

    render_x *= ROOM_WIDTH + DOOR_WIDTH
    render_y *= ROOM_WIDTH + DOOR_WIDTH

    if direction == RIGHT:
        render_x += ROOM_WIDTH
        render_y += (ROOM_WIDTH - DOOR_WIDTH) / 2
    elif direction == DOWN:
        render_y += ROOM_WIDTH
        render_x += (ROOM_WIDTH - DOOR_WIDTH) / 2
    elif direction == LEFT:
        render_x -= DOOR_WIDTH
        render_y += (ROOM_WIDTH - DOOR_WIDTH) / 2
    elif direction == UP:
        render_y -= DOOR_WIDTH
        render_x += (ROOM_WIDTH - DOOR_WIDTH) / 2


    pygame.draw.rect(window, DOOR_COLOUR, (render_x, render_y, DOOR_WIDTH, DOOR_WIDTH))




if __name__ == '__main__':
    main()

