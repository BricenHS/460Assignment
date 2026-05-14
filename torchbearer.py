"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Bricen Humphrey Schaefer
Student ID:   __________

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.
    """
    return """Part 1: Problem Analysis
Document why this problem is not just a shortest-path problem. Three bullet points, one per question. Each bullet should be 1-2 sentences max.

Why a single shortest-path run from S is not enough: A single Dikjstras run from S is not enough to know what the shortest path is. From every relic you must run Dikjstra's to find what the shortest path is all the way until T.

What decision remains after all inter-location costs are known: The remaining decision is the choice of what order the relics get visited in so that less fuel is used.

Why this requires a search over orders (one sentence): It is not a single computation because from the start point it checks for the shortest path reachable from relic to relic, until it has visited all relics, which it then finds shortest path to the exit (T)."""


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.
        TODO

    """
    sources = []

    if spawn not in sources:
        sources.append(spawn)

    for relic in relics:
        if relic not in sources:
            sources.append(relic)

    return sources


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').
        TODO
    """
    start_vertex = source
    distances ={node: float('inf') for node in graph}
    distances[start_vertex] = 0
    visited = {node: False for node in graph}

    for _ in range(len(graph)):
        min_distance = float('inf')
        u = None
        for i in graph:
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                u = i

        if u is None:
            break

        visited[u] = True

        for (v,weight) in graph[u]:
            if  not visited[v]:
                alt = distances[u] + weight
                if alt < distances[v]:
                    distances[v] = alt

    return distances
    
    

   

    


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    sources = [spawn] + relics
    dist_table = {}
        
    for source in sources:
        distances = run_dijkstra(graph, source)
        dist_table[source] = distances

    return dist_table
            



# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.
    """
    explanation = """Part 3: Algorithm Correctness
Document your understanding of why Dijkstra produces correct distances. Bullet points and short sentences throughout. No paragraphs. -So for the starting node it begins and checks for the next neighboring least cost node that it can reach assuming that the current node can be finalized. -Then once it is now on that node it repeats the check for the surrounding neighboring nodes moving to the next least cost node. -This will repeat to k+1 times because we know T does not need to run a dijkstra's algorithm

Part 3a: What the Invariant Means
Two bullets: one for finalized nodes, one for non-finalized nodes. Do not copy the invariant text from the spec.

Once finalized the distance is the amount of fuel used by the torch to get to T, and will never change once a node path is finalized.

For non-finalized nodes, their distance represents the shortest distance found so far, but it may still change if a shorter path is discovered.

For nodes already finalized (in S): For each node that is finalized for S, it is the true minimum cost from the current starting relic node, to the next minimum node. This is finalized and the distance will not be changed at a later point.

For nodes not yet finalized (not in S): The non-finalized nodes are ones that are the best fuel cost found so far for the current starting relic, however if a better cost path is found it can still be changed.

Part 3b: Why Each Phase Holds
One to two bullets per phase. Maintenance must mention nonnegative edge weights.

Initialization : why the invariant holds before iteration 1:

Before the first iteration, the invariant holds true because S is the only source, so the distance is 0.
All other sources are considered to be infinity because other nodes have not been reached or found yet, which is true for all cases and is why it holds.
Maintenance : why finalizing the min-dist node is always correct:

Since u was chosen as the minimum-distance node, we know that distance[x] >= distance[u].

Since all edge weights are nonnegative, then it is known that whatever the distance from the start to the current node is, when compared to the immediate path, Dikjstras can tell us what path will be a better choice in terms of cost between both distances and their weights.

Termination : what the invariant guarantees when the algorithm ends:

When the loop terminates normally, all relics have been visited, so the order list contains the order in which relic rooms were visited. The invariant guarantees that total_cost equals the accumulated shortest path cost for the chosen order so far. Then the algorithm checks whether T is reachable from the current node.

Part 3c: Why This Matters for the Route Planner
One sentence connecting correct distances to correct routing decisions.

Since Dijkstra computes the true shortest distance between node, when the algorithm selects the next relic based on the smallest distance, it is choosing based on accurate shortest-path information.
"""
    return explanation

# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.
    """
    explanation = """Why Greedy Fails State the failure mode. 
Then give a concrete counter-example using specific node names or costs (you may use the illustration example from the spec). Three to five bullets.

The failure mode:
The biggest failure that can occur is that greedy cannot consider the future minimal costs.
Failure to take into account the total ending cost for the route
Only chooses the immediate best choice with no consideration for later optimal costs.
Counter-example setup:
Say S goes to {A,B} and it costs 1 to reach A and 2 to reach B
A is directed at nothing which is an issue
This counter example will end up breaking because the route can never finalize
What greedy picks:
Chooses closest least cost path
So if it starts at S then moves to A at a 1 cost, it is now stuck at A because it cannnot backtrack to S and cannot just teleport to B
This is how greedy choosing a least immediate cost path can end up breaking
What optimal picks:
Optimal pick the immediate least cost connecting node that is adjacent to the source
If that source that it chooses has nothing to continue too after, then the code will not be able to finish that path, it will then parse to the next best path
Optimal will continue searching for the next best path, while in comparison greedy will stop
Why greedy loses:
Greedy loses to optimal because it can parse over orders to the next best path
While greedy would break after not being able to continue the path, Optimal will continue to find the next best path
So that means that in in a situation where greedy cannot preform, optimal will still be able to find a valid path.
What the Algorithm Must Explore
One bullet. Must use the word "order."

- It must explore the route it takes from chamber to chamber and store the order in which the relic chambers get visited."""
    
    return explanation
# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """

    best = [float('inf'), []]
    relics_remaining = set(relics)
    relics_visited_order = []
    cost_so_far = 0

    _explore(
        dist_table,
        spawn,
        relics_remaining,
        relics_visited_order,
        cost_so_far,
        exit_node,
        best
    )

    return best[0], best[1]



def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.


    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    TODO
    """
    if cost_so_far >= best[0]:
    # This pruning is safe because all edge costs are nonnegative, so any extra travel
    # can only keep the cost the same or increase it; this route cannot beat best.
        return

    if len(relics_remaining) == 0:
        exit_cost = dist_table[current_loc][exit_node]

        if exit_cost == float('inf'):
            return

        total_cost = cost_so_far + exit_cost

        if total_cost < best[0]:
            best[0] = total_cost
            best[1] = relics_visited_order.copy()

        return

    for relic in list(relics_remaining):
        travel_cost = dist_table[current_loc][relic]

        if travel_cost == float('inf'):
            continue

        relics_remaining.remove(relic)
        relics_visited_order.append(relic)

        _explore(
            dist_table,
            relic,
            relics_remaining,
            relics_visited_order,
            cost_so_far + travel_cost,
            exit_node,
            best
        )

        relics_visited_order.pop()
        relics_remaining.add(relic)
    pass


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    return find_optimal_route(dist_table, spawn, relics, exit_node)



# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }

    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")


    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
