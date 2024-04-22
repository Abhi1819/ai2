from collections import deque


class State:
    def __init__(self, big, small):
        self.big = big
        self.small = small

    def __eq__(self, other):
        return self.big == other.big and self.small == other.small

    def __hash__(self):
        return hash((self.big, self.small))

    def __str__(self):
        return f"({self.big}, {self.small})"


def is_valid_state(state):
    return 0 <= state.big <= 3 and 0 <= state.small <= 2


def get_successors(state):
    successors = [State(3, state.small), State(state.big, 2), State(0, state.small), State(state.big, 0)]

    # Fill the big jug

    # Fill the small jug

    # Empty the big jug

    # Empty the small jug

    # Pour from small jug to big jug
    pour_amount = min(state.small, 3 - state.big)
    successors.append(State(state.big + pour_amount, state.small - pour_amount))

    # Pour from big jug to small jug
    pour_amount = min(state.big, 2 - state.small)
    successors.append(State(state.big - pour_amount, state.small + pour_amount))

    return [successor for successor in successors if is_valid_state(successor)]


def solve_water_jug_problem():
    start_state = State(0, 0)
    goal_state = State(1, 0)

    visited = set()
    queue = deque()
    queue.append((start_state, []))

    while queue:
        current_state, path = queue.popleft()

        if current_state in visited:
            continue

        visited.add(current_state)

        if current_state == goal_state:
            return path

        for successor in get_successors(current_state):
            queue.append((successor, path + [successor]))

    return None


path = solve_water_jug_problem()
if path:
    print("Steps to reach the goal:")
    for step, state in enumerate(path):
        print(f"Step {step + 1}: {state}")
else:
    print("No solution found.")
