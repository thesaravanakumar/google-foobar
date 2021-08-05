def solution(map):
    stack_x = [0]
    stack_y = [0]
    stack_removal = [False]

    height = len(map)
    width = len(map[0])

    path_map = []
    for y in range(height):
        path_map.append([])
        for x in range(width):
            path_map[y].append([None,  # value for shortest path without wall removal
                                None,  # value for shortest path with wall removal
                                True if map[y][x] else False])  # position has wall underneath

    path_map[0][0][0] = 1

    while stack_x and stack_y and stack_removal:
        x = stack_x.pop()
        y = stack_y.pop()
        removal = stack_removal.pop()
        curr_pos = path_map[y][x]

        if x + 1 < width: # right (x + 1)
            next_pos = path_map[y][x + 1]
            calculate_path(stack_x, stack_y, x + 1, y, stack_removal, removal, curr_pos, next_pos)
        if y + 1 < height:  # down (y + 1)
            next_pos = path_map[y + 1][x]
            calculate_path(stack_x, stack_y, x, y + 1, stack_removal, removal, curr_pos, next_pos)
        if x - 1 >= 0:  # left (x - 1)
            next_pos = path_map[y][x - 1]
            calculate_path(stack_x, stack_y, x - 1, y, stack_removal, removal, curr_pos, next_pos)
        if y - 1 >= 0:  # up (y - 1)
            next_pos = path_map[y - 1][x]
            calculate_path(stack_x, stack_y, x, y - 1, stack_removal, removal, curr_pos, next_pos)


    end = path_map[-1][-1]
    return end[1] if end[1] <= end[0] or end[0] is None else end[0]


def calculate_path(stack_x, stack_y, x, y, stack_removal, removal, curr_pos, next_pos):
    best_path = True
    if removal and next_pos[2]:
        best_path = False
    elif removal:
        if next_pos[1] is not None and next_pos[1] <= curr_pos[1] + 1:
            best_path = False
        else:
            next_pos[1] = curr_pos[1] + 1
    elif next_pos[2]:
        if next_pos[1] is not None and next_pos[1] <= curr_pos[0] + 1:
            best_path = False
        else:
            removal = True
            next_pos[1] = curr_pos[0] + 1
    elif next_pos[0] is not None and next_pos[0] <= curr_pos[0] + 1:
        best_path = False
    else:
        next_pos[0] = curr_pos[0] + 1
    if best_path:
        stack_x.append(x)
        stack_y.append(y)
        stack_removal.append(removal)
        