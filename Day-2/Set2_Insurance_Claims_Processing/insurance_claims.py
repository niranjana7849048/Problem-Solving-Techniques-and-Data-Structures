
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
            if value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def normalize(self, policy_number, incident_date):
        policy = "".join(policy_number.upper().split())
        date = incident_date.strip()
        return policy + "|" + date

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, policy_number, incident_date, claim_id):
        key = self.normalize(policy_number, incident_date)
        index = self.hash_function(key)

        for entry in self.table[index]:
            if entry[0] == key:
                entry[1].append(claim_id)
                return True

        self.table[index].append([key, [claim_id]])
        return False

    def search(self, policy_number, incident_date):
        key = self.normalize(policy_number, incident_date)
        index = self.hash_function(key)

        for entry in self.table[index]:
            if entry[0] == key:
                return entry[1]

        return []


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


def has_cycle(graph):
    visited = set()
    recursion_stack = set()

    def dfs(node):
        visited.add(node)
        recursion_stack.add(node)

        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                if dfs(neighbour):
                    return True
            elif neighbour in recursion_stack:
                return True

        recursion_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False


def longest_exceeding_run(claim_counts, threshold):
    left = 0
    max_length = 0
    best_start = -1
    best_end = -1

    for right in range(len(claim_counts)):
        if claim_counts[right] <= threshold:
            left = right + 1
        else:
            current_length = right - left + 1

            if current_length > max_length:
                max_length = current_length
                best_start = left
                best_end = right

    if max_length == 0:
        return 0, -1, -1

    return max_length, best_start, best_end


def merge_sorted_lists(list1, list2):
    i = 0
    j = 0
    merged = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged


def main():
    print("INSURANCE CLAIMS PROCESSING")

    print("\nTASK 1: BINARY SEARCH TREE")

    claim_ids = [105, 102, 108, 101, 104, 107, 110]
    bst = BinarySearchTree()

    for claim_id in claim_ids:
        bst.insert(claim_id)

    print("Inorder traversal:")
    bst.inorder(bst.root)

    print("\nPreorder traversal:")
    bst.preorder(bst.root)

    print("\nPostorder traversal:")
    bst.postorder(bst.root)

    print("\n\nSearch claim 104:", bst.search(104))
    print("Search claim 115:", bst.search(115))
    print("Sorted order is produced by inorder traversal.")

    empty_bst = BinarySearchTree()
    print("Empty BST search:", empty_bst.search(100))

    print("\nTASK 2: HASHING AND DUPLICATE CLAIMS")

    claims = [
        ("POL123", "2026-01-10", "C1001"),
        (" pol 123 ", "2026-01-10", "C1002"),
        ("POL132", "2026-01-10", "C1003"),
        ("POL456", "2026-01-12", "C1004")
    ]

    claim_table = HashTable(10)

    for policy, date, claim_id in claims:
        duplicate = claim_table.insert(policy, date, claim_id)
        print(claim_id, "Duplicate:", duplicate)

    print("Matching claims for POL123:",
          claim_table.search("POL123", "2026-01-10"))

    key1 = claim_table.normalize("POL123", "2026-01-10")
    key2 = claim_table.normalize("POL132", "2026-01-10")

    print("Collision demonstrated:",
          claim_table.hash_function(key1) ==
          claim_table.hash_function(key2))

    print("Empty hash lookup:",
          claim_table.search("POL999", "2026-01-10"))

    print("\nTASK 3: CLAIM APPROVAL GRAPH")

    graph = {
        "Registration": ["Assessment"],
        "Assessment": ["Surveyor", "Settlement"],
        "Surveyor": ["Settlement"],
        "Settlement": []
    }

    path = bfs_shortest_path(graph, "Registration", "Settlement")
    print("Shortest path:", " -> ".join(path))
    print("Cycle detected:", has_cycle(graph))

    cyclic_graph = {
        "Registration": ["Assessment"],
        "Assessment": ["Surveyor"],
        "Surveyor": ["Settlement"],
        "Settlement": ["Assessment"]
    }

    print("Cycle detected in cyclic graph:", has_cycle(cyclic_graph))

    print("\nTASK 4: SLIDING WINDOW")

    daily_claims = [
        85, 120, 135, 110, 95, 130, 145,
        108, 99, 115, 125, 140
    ]

    length, start, end = longest_exceeding_run(daily_claims, 100)

    print("Daily claims:", daily_claims)
    print("Threshold: More than 100 claims")
    print("Longest consecutive run:", length, "days")

    if length:
        print("Day positions:", start + 1, "to", end + 1)

    empty_result = longest_exceeding_run([], 100)
    print("Empty input result:", empty_result)

    print("\nTASK 5: TWO-POINTER MERGE")

    region_a = [1001, 1003, 1007, 1010]
    region_b = [1002, 1004, 1008, 1012]

    merged_claims = merge_sorted_lists(region_a, region_b)

    print("Region A:", region_a)
    print("Region B:", region_b)
    print("Merged sorted claims:", merged_claims)

    print("Empty list merge:",
          merge_sorted_lists([], [1001, 1002]))

    print("\nALL TASKS COMPLETED")


if __name__ == "__main__":
    main()
