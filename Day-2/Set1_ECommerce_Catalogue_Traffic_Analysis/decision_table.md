# Decision Table – Day 2 Set 1

| Problem | Data Structure / Pattern | Reason |
|---|---|---|
| Product category management | Binary Search Tree | Supports insertion, searching and ordered traversal |
| SKU lookup | Hash Table / HashMap | Provides efficient key-based lookup |
| Microservice dependencies | Graph with BFS and DFS | Represents service relationships and identifies dependencies and cycles |
| Busiest 3-hour traffic window | Sliding Window | Efficiently calculates sums over consecutive time intervals |
| Gift-card matching | Two Pointers | Finds pairs in a sorted list without nested loops |

## Complexity Analysis

| Task | Time Complexity | Space Complexity |
|---|---|---|
| BST insert and search | O(h), h = tree height | O(h) for recursive traversals |
| Custom hash table lookup | O(1) average, O(n) worst | O(n) |
| Built-in HashMap lookup | O(1) average | O(n) |
| BFS and DFS | O(V + E) | O(V) |
| Topological sorting and cycle detection | O(V + E) | O(V) |
| Sliding Window | O(n) | O(1) |
| Two Pointers | O(n) | O(k) for k matching pairs |

## Conclusion

The assignment demonstrates how trees, hashing, graphs and array-processing patterns can solve common e-commerce problems efficiently.