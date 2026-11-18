
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right
            else:
                return

    def search(self, value):
        current = self.root

        while current:
            if current.value == value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    def height(self, node):
        if node is None:
            return 0

        return 1 + max(
            self.height(node.left),
            self.height(node.right)
        )


def dfs(graph, start):
    visited = set()

    def visit(node):
        if node not in visited:
            visited.add(node)

            for neighbour in graph.get(node, []):
                visit(neighbour)

    visit(start)
    return visited


def bfs_shortest_path(graph, start, destination):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        current, path = queue.popleft()

        if current == destination:
            return path

        for neighbour in graph.get(current, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path + [neighbour]))

    return []


def detect_duplicate_scans(scans):
    seen = set()
    duplicates = []

    for parcel_id, hub in scans:
        key = (parcel_id.strip().upper(), hub.strip().upper())

        if key in seen:
            duplicates.append(key)
        else:
            seen.add(key)

    return duplicates


def highest_average_window(parcel_counts, window_size):
    if window_size <= 0 or window_size > len(parcel_counts):
        return None

    current_sum = sum(parcel_counts[:window_size])
    max_sum = current_sum
    best_start = 0

    for i in range(window_size, len(parcel_counts)):
        current_sum += parcel_counts[i]
        current_sum -= parcel_counts[i - window_size]

        if current_sum > max_sum:
            max_sum = current_sum
            best_start = i - window_size + 1

    average = max_sum / window_size

    return best_start, best_start + window_size - 1, max_sum, average


def normalize_hub_code(code):
    return "".join(
        char.lower()
        for char in code
        if char.isalnum()
    )


def is_palindrome(code):
    normalized = normalize_hub_code(code)

    left = 0
    right = len(normalized) - 1

    while left < right:
        if normalized[left] != normalized[right]:
            return False

        left += 1
        right -= 1

    return True


def main():
    print("LOGISTICS NETWORK AND DELIVERY WINDOWS")

    print("\nTASK 1: BINARY SEARCH TREE")

    hub_codes = ["CHN", "BLR", "DEL", "HYD", "MUM", "PUN", "KOL"]

    bst = BinarySearchTree()

    for code in hub_codes:
        bst.insert(code)

    print("Hub codes:", hub_codes)
    print("Search BLR:", bst.search("BLR"))
    print("Search CBE:", bst.search("CBE"))
    print("BST height:", bst.height(bst.root))

    sorted_bst = BinarySearchTree()

    for code in sorted(hub_codes):
        sorted_bst.insert(code)

    print("Height with sorted input:", sorted_bst.height(sorted_bst.root))
    print("Height with unsorted input:", bst.height(bst.root))

    empty_bst = BinarySearchTree()
    print("Empty BST height:", empty_bst.height(empty_bst.root))

    print("\nTASK 2: HASHMAP PARCEL TRACKING")

    scans = [
        ("P1001", "CHN"),
        ("P1002", "BLR"),
        ("P1003", "HYD"),
        ("P1001", "CHN"),
        ("P1004", "MUM"),
        ("P1002", "BLR"),
        ("P1001", "DEL")
    ]

    parcel_tracking = {}

    for parcel_id, hub in scans:
        parcel_tracking.setdefault(parcel_id, []).append(hub)

    print("Parcel tracking:", parcel_tracking)

    duplicates = detect_duplicate_scans(scans)

    print("Duplicate scans:", duplicates)

    print("\nTASK 3: LOGISTICS GRAPH")

    graph = {
        "CHN": ["BLR", "HYD"],
        "BLR": ["CHN", "MUM"],
        "HYD": ["CHN", "MUM", "DEL"],
        "MUM": ["BLR", "HYD", "PUN"],
        "DEL": ["HYD", "KOL"],
        "PUN": ["MUM", "KOL"],
        "KOL": ["DEL", "PUN"],
        "CBE": ["CHN"],
        "GOA": ["MUM"],
        "JAI": ["DEL"]
    }

    path = bfs_shortest_path(graph, "CHN", "KOL")

    print("Shortest path from CHN to KOL:", " -> ".join(path))
    print("Fewest hops:", len(path) - 1 if path else "No path")

    reachable = dfs(graph, "CHN")
    print("Hubs reachable from CHN:", sorted(reachable))

    print("\nTASK 4: SLIDING WINDOW")

    hourly_counts = [
        120, 135, 150, 160, 140, 180,
        200, 190, 170, 155, 145, 130
    ]

    result = highest_average_window(hourly_counts, 4)

    print("Hourly parcel counts:", hourly_counts)

    if result:
        start, end, total, average = result
        print("Best 4-hour window: Hour", start + 1, "to Hour", end + 1)
        print("Total parcels:", total)
        print("Highest average:", round(average, 2))

    print("Empty input result:",
          highest_average_window([], 4))

    print("\nTASK 5: TWO-POINTER PALINDROME")

    hub_code1 = "CHN-NHC"
    hub_code2 = "CHN-BLR"

    print("Hub code:", hub_code1)
    print("Is palindrome:", is_palindrome(hub_code1))

    print("Hub code:", hub_code2)
    print("Is palindrome:", is_palindrome(hub_code2))

    print("Empty code palindrome:", is_palindrome(""))

    print("\nALL TASKS COMPLETED")


if __name__ == "__main__":
    main()
