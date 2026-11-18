
# Day 2 – Set 2: Insurance Claims Processing

## Complexity Analysis

| Task | Technique | Time Complexity | Space Complexity |
|---|---|---|---|
| Claim ID operations | Binary Search Tree | O(h) | O(n) |
| Duplicate claim detection | Hashing with Chaining | O(1) average, O(n) worst case | O(n) |
| Shortest approval path | BFS | O(V + E) | O(V) |
| Cycle detection | DFS | O(V + E) | O(V) |
| Longest consecutive run | Sliding Window | O(n) | O(1) |
| Merge regional claim lists | Two Pointers | O(n + m) | O(n + m) |

## Key Observations

- Inorder traversal of a BST produces claim IDs in sorted order.
- Hashing normalizes policy numbers by removing spaces and converting letters to uppercase.
- Chaining stores multiple entries in the same bucket when hash collisions occur.
- BFS finds the shortest path in an unweighted graph.
- DFS detects cycles using a recursion stack.
- Sliding Window finds the longest consecutive sequence of days with more than 100 claims.
- Two Pointers merges two already sorted lists without sorting them again.
