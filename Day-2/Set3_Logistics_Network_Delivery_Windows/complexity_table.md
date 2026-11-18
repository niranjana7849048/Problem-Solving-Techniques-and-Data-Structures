
# Day 2 – Set 3: Logistics Network and Delivery Windows

## Complexity Analysis

| Task | Technique | Time Complexity | Space Complexity |
|---|---|---|---|
| Hub insertion and search | Binary Search Tree | O(h) | O(n) |
| Height calculation | Tree Traversal | O(n) | O(h) |
| Parcel tracking | HashMap | O(1) average | O(n) |
| Duplicate scan detection | HashSet | O(n) average | O(n) |
| Shortest route | BFS | O(V + E) | O(V) |
| Reachable hubs | DFS | O(V + E) | O(V) |
| Highest 4-hour average | Sliding Window | O(n) | O(1) |
| Palindrome validation | Two Pointers | O(n) | O(n) |

## Key Observations

- Sorted BST insertion can produce an unbalanced tree.
- HashMap provides efficient parcel tracking.
- HashSet detects repeated parcel scans at the same hub.
- BFS finds the route with the fewest hops in an unweighted graph.
- DFS identifies all reachable hubs.
- Sliding Window calculates the highest average parcel volume.
- Two Pointers checks palindrome hub codes after normalization.

