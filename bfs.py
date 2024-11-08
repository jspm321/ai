BFS code

GRAPH = {\
    'Arad': {'Sibiu': 140, 'Zerind': 75, 'Timisoara': 118},\
    'Zerind': {'Arad': 75, 'Oradea': 71},\
    'Oradea': {'Zerind': 71, 'Sibiu': 151},\
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu': 80},\
    'Timisoara': {'Arad': 118, 'Lugoj': 111},\
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},\
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},\
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},\
    'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},\
    'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},\
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},\
    'Pitesti': {'Rimnicu': 97, 'Craiova': 138, 'Bucharest': 101},\
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},\
    'Giurgiu': {'Bucharest': 90},\
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},\
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},\
    'Eforie': {'Hirsova': 86},\
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},\
    'Iasi': {'Vaslui': 92, 'Neamt': 87},\
    'Neamt': {'Iasi': 87}\
}

def bestfirst(source, destination):
    """Optimal path from source to destination using straight line distance heuristic

    :param source: Source city name
    :param destination: Destination city name
    :returns: Heuristic value, cost, and path for optimal traversal
    """
    # Here the straight line distance values are in reference to Bucharest as the destination
    straight_line = {\
        'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Sibiu': 253, 'Timisoara': 329,\
        'Lugoj': 244, 'Mehadia': 241, 'Drobeta': 242, 'Craiova': 160, 'Rimnicu': 193,\
        'Fagaras': 176, 'Pitesti': 100, 'Bucharest': 0, 'Giurgiu': 77, 'Urziceni': 80,\
        'Hirsova': 151, 'Eforie': 161, 'Vaslui': 199, 'Iasi': 226, 'Neamt': 234\
    }

    from queue import PriorityQueue
    priority_queue = PriorityQueue()
    visited = {}

    # The priority queue holds tuples of (heuristic, cost, current_city, path_taken)
    priority_queue.put((straight_line[source], 0, source, [source]))
    visited[source] = 0  # We store the cost to reach each node

    while not priority_queue.empty():
        heuristic, cost, city, path = priority_queue.get()

        if city == destination:
            return heuristic, cost, path

        for next_city, travel_cost in GRAPH[city].items():
            new_cost = cost + travel_cost
            # If the node hasn't been visited or we found a better cost, add to queue
            if next_city not in visited or new_cost < visited[next_city]:
                visited[next_city] = new_cost
                priority_queue.put((straight_line[next_city], new_cost, next_city, path + [next_city]))

    return None  # If no path found

def main():
    """Main function"""
    print('ENTER SOURCE:', end=' ')
    source = input().strip()
    print('ENTER GOAL:', end=' ')
    goal = input().strip()

    # Convert the input to title case to match the city names in the GRAPH
    source = source.title()
    goal = goal.title()

    if source not in GRAPH or goal not in GRAPH:
        print('ERROR: CITY DOES NOT EXIST.')
    else:
        print('\nBEST-FIRST SEARCH PATH:')
        result = bestfirst(source, goal)
        if result:
            heuristic, cost, optimal_path = result
            print('PATH COST =', cost)
            print(' -> '.join(city for city in optimal_path))
        else:
            print('No path found.')

if __name__ == '__main__':
    main()
