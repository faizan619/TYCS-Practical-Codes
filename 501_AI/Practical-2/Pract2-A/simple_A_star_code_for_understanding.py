def a_star(start, goal, graph):
    open = []
    closed = []

    open.append((start, 0))

    while open:
        node, cost = open.pop(0)

        if node == goal:
            return cost

        closed.append(node)

        for neighbor in graph[node]:
            if neighbor not in closed:
                new_cost = cost + graph[node][neighbor]
                open.append((neighbor, new_cost))

    return None


def main():
    graph = {
        "A": {"B": 1, "C": 3},
        "B": {"C": 1, "D": 2},
        "C": {"D": 1},
        "D": {"E": 1},
    }

    start = "A"
    goal = "E"

    cost = a_star(start, goal, graph)

    print("The cost of the shortest path is", cost)


if __name__ == "__main__":
    main()
