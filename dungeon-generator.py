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

    # An array containing the coordinates of the first room (x, y)
    rooms = [(0, 0)]

    # A array containing the coordinates of rooms that should be considered for branching off of
    available_rooms = [(0, 0)]

    # A list of doors. The doors are defined by the structure: (room, direction)
    # where room is a coordinate representing the room's position, and direction is an integer
    # constant representing one of the four directions (RIGHT = 0, DOWN = 1, LEFT = 2, RIGHT = 3)
    # that the door is facing in. For example, ((3, 4), RIGHT) means the door is to the RIGHT of
    # the room at coordinate (3, 4)
    doors = []

    while len(rooms) < num_rooms:

        door_positions = [RIGHT, DOWN, LEFT, UP]

        # Choose a random room from the available rooms to branch off of
        room = random.choice(available_rooms)

        # Get the x and y values of the current room
        x = room[0]
        y = room[1]

        if (x + 1, y) in rooms:
            door_positions.remove(RIGHT)

        if (x, y + 1) in rooms:
            door_positions.remove(DOWN)

        if (x - 1, y) in rooms:
            door_positions.remove(LEFT)

        if (x, y - 1) in rooms:
            door_positions.remove(UP)

        if len(door_positions) == 0:
            # If there are no doors available to branch off of, this room needs to be removed
            # from the list of available rooms
            available_rooms.remove(room)

        else:
            # Otherwise, add the neighbour room

            # This is basically picking a random door position to make the neighbour
            # branch off of
            neighbour_direction = random.choice(door_positions)

            # Calculates the coordinates of the neighbour based on it's position
            if neighbour_direction == RIGHT:
                neighbour = (x + 1, y)
            elif neighbour_direction == DOWN:
                neighbour = (x, y + 1)
            elif neighbour_direction == LEFT:
                neighbour = (x - 1, y)
            elif neighbour_direction == UP:
                neighbour = (x, y - 1)

            # Add the door representation
            doors.append((room, neighbour_direction))

            # Add the neighbour to the room arrays. Since it hasn't been checked yet, we
            # consider it available to branch off of. Once it has been checked and identified
            # as not available, we can remove it from the available_rooms array.
            rooms.append(neighbour)
            available_rooms.append(neighbour)

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

