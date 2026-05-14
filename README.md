# The Torchbearer

**Student Name:** _Bricen Humphrey-Schaefer__
**Student ID:** 827476527
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
A single Dikjstras run from S is not enough to know what the shortest path is. From every relic you must run Dikjstra's to find what the shortest path is all the way until T.

- **What decision remains after all inter-location costs are known:**
 The remaining decision is the choice of what order the relics get visited in so that less fuel is used.

- **Why this requires a search over orders (one sentence):**
  It is not a single computation because from the start point it checks for the shortest path reachable from relic to relic, until it has visited all relics, which it then finds shortest path to the exit (T).

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| _The start node S_ | _Fixed point, where you begin branching out._ |
| _Every other relic node_ | _Because Dijkstras needs to be ran to find shortest path to each relic._ |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | Dictionary hash map adjacency list |
| What the keys represent | Key represents the node where Dikjstra's starts |
| What the values represent | The nodes that are the neighbors of the keys |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Once stored to memory, the nodes in list can be accsessed at a constant time. |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** |M| = k We need 1 dikjstra's run from every node in the set M. And one from the entrance node S. A total of k+1 dikjstra's runs. 
- **Cost per run:** O(ElogV)
- **Total complexity:** (k+1)(ElogV)
- **Justification (one line):** Total Dikjstra's runs is k+1 and runs ElogV times.

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.
-So for the starting node it begins and checks for the next neighboring least cost node that it can reach assuming that the current node can be finalized.
-Then once it is now on that node it repeats the check for the surrounding neighboring nodes moving to the next least cost node.
-This will repeat to k+1 times because we know T does not need to run a dijkstra's algorithm

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.
- Once finalized the distance is the amount of fuel used by the torch to get to T, and will never change once a node path is finalized.
- For non-finalized nodes, their distance represents the shortest distance found so far, but it may still change if a shorter path is discovered.

- **For nodes already finalized (in S):**
  For each node that is finalized for S, it is the true minimum cost from the current starting relic node, to the next minimum node. This is finalized and the distance will not be changed at a later point.
- **For nodes not yet finalized (not in S):**
  The non-finalized nodes are ones that are the best fuel cost found so far for the current starting relic, however if a better cost path is found it can still be changed.

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  - Before the first iteration, the invariant holds true because S is the only source, so the distance is 0.
  - All other sources are considered to be infinity because other nodes have not been reached or found yet, which is true for all cases and is why it holds.

- **Maintenance : why finalizing the min-dist node is always correct:**
- Since u was chosen as the minimum-distance node, we know that distance[x] >= distance[u]. 
- Since all edge weights are nonnegative, then it is known that whatever the distance from the start to the current node is, when compared to the immediate path, Dikjstras can tell us what path will be a better choice in terms of cost between both distances and their weights.

- **Termination : what the invariant guarantees when the algorithm ends:**
- When the loop terminates normally, all relics have been visited, so the order list contains the order in which relic rooms were visited. The invariant guarantees that total_cost equals the accumulated shortest path cost for the chosen order so far. Then the algorithm checks whether T is reachable from the current node.

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.
- Since Dijkstra computes the true shortest distance between node, when the algorithm selects the next relic based on the smallest distance, it is choosing based on accurate shortest-path information.



---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** 
- The biggest failure that can occur is that greedy cannot consider the future minimal costs.
- Failure to take into account the total ending cost for the route
- Only chooses the immediate best choice with no consideration for later optimal costs.
- **Counter-example setup:**
- Say S goes to {A,B} and it costs 1 to reach A and 2 to reach B
- A is directed at nothing which is an issue
- This counter example will end up breaking because the route can never finalize
- **What greedy picks:** 
- Chooses closest least cost path
- So if it starts at S then moves to A at a 1 cost, it is now stuck at A because it cannnot backtrack to S and cannot just teleport to B
- This is how greedy choosing a least immediate cost path can end up breaking
- **What optimal picks:**
- Optimal pick the immediate least cost connecting node that is adjacent to the source
- If that source that it chooses has nothing to continue too after, then the code will not be able to finish that path, it will then parse to the next best path
- Optimal will continue searching for the next best path, while in comparison greedy will stop
- **Why greedy loses:** 
- Greedy loses to optimal because it can parse over orders to the next best path
- While greedy would break after not being able to continue the path, Optimal will continue to find the next best path
- So that means that in in a situation where greedy cannot preform, optimal will still be able to find a valid path.

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | current | node / string  tracks where the alg is currently| |
| Relics already collected | visited_relics | set | stores relics that have been visited |
| Fuel cost so far | total_cost | number / int | stores the added travel cost so far |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | set |
| Operation: check if relic already collected | Time complexity: O(1)|
| Operation: mark a relic as collected | Time complexity: O(1) |
| Operation: unmark a relic (backtrack) | Time complexity: O(1)|
| Why this structure fits | It fits because it can check for immediate least cost and update |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** The worst case possible would be k!.
- **Why:** Because there are k choices for the first relic, k−1 for the second, k−2 for the third, and so on, resulting in k! total possible orders.

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** 
- The minimum total cost found so far along with the order of visited relics
- **When it is used:** 
- When no routes are availiable it is used before it explores a path further
- **What it allows the algorithm to skip:** 
- It allows skipping the check of every branch of the search tree

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** 
- What the current source is, which relics have not been visited, what the current fuel cost is, and the order the relics have been visited
- **What the lower bound accounts for:** 
- The minimum additional cost required before reaching exit T after visiting all relic chambers
- **Why it never overestimates:** 
- It will never take the larger path, so it wont overestimates.

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- Because all edge weights are nonnegative pruning is a safe action.
- After finding a minimum path, adding any more points will only increase the total cost, so the path cannot have a better solution when running.

---

## References

> Bullet list. If none beyond lecture notes, write that.

- W3Schools.com
