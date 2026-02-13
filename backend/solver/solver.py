from collections import deque

class State:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_goal(self):
        return self.x == 2 or self.y == 2

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


def get_next_states(s):
    states = []

    states.append(State(4, s.y))     # Fill jug1
    states.append(State(s.x, 3))     # Fill jug2
    states.append(State(0, s.y))     # Empty jug1
    states.append(State(s.x, 0))     # Empty jug2

    pour = min(s.x, 3 - s.y)
    states.append(State(s.x - pour, s.y + pour))

    pour = min(s.y, 4 - s.x)
    states.append(State(s.x + pour, s.y - pour))

    return states


def bfs():
    start = State(0, 0)
    queue = deque([(start, [])])
    visited = set([start])

    while queue:
        current, path = queue.popleft()
        path = path + [(current.x, current.y)]

        if current.is_goal():
            return path

        for nxt in get_next_states(current):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path))

    return []
