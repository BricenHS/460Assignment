# The Torchbearer

**Student Name:** _Bricen Humphrey-Schaefer__
**Student ID:** ___________________________
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
  _Your answer here._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _Your answer here._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _Your answer here._

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_Your answer here._

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

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
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
