
import random
import time


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

    def hash_function(self, key):
        return sum(ord(char) for char in str(key)) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)

        for stored_key, value in self.table[index]:
            if stored_key == key:
                return value

        return None


def graph_bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    result = []

    while queue:
        vertex = queue.pop(0)
        result.append(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def graph_dfs(graph, start):
    visited = set()
    result = []

    def visit(vertex):
        visited.add(vertex)
        result.append(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return result


def topological_sort(graph):
    visited = set()
    recursion_stack = set()
    result = []

    def visit(vertex):
        if vertex in recursion_stack:
            return False

        if vertex in visited:
            return True

        visited.add(vertex)
        recursion_stack.add(vertex)

        for neighbor in graph.get(vertex, []):
            if not visit(neighbor):
                return False

        recursion_stack.remove(vertex)
        result.append(vertex)
        return True

    for vertex in graph:
        if vertex not in visited:
            if not visit(vertex):
                return None

    result.reverse()
    return result


def has_cycle(graph):
    return topological_sort(graph) is None


def busiest_window(requests, window_size):
    current_sum = sum(requests[:window_size])
    maximum_sum = current_sum
    best_start = 0

    for i in range(window_size, len(requests)):
        current_sum += requests[i] - requests[i - window_size]

        if current_sum > maximum_sum:
            maximum_sum = current_sum
            best_start = i - window_size + 1

    return best_start, maximum_sum


def find_pairs(values, target):
    left = 0
    right = len(values) - 1
    pairs = []

    while left < right:
        total = values[left] + values[right]

        if total == target:
            pairs.append((values[left], values[right]))

            left_value = values[left]
            right_value = values[right]

            while left < right and values[left] == left_value:
                left += 1

            while left < right and values[right] == right_value:
                right -= 1

        elif total < target:
            left += 1
        else:
            right -= 1

    return pairs


def main():
    print("ECOMMERCE CATALOGUE AND TRAFFIC ANALYSIS")

    print("\nTASK 1: BINARY SEARCH TREE")

    categories = [
        "Electronics",
        "Fashion",
        "Books",
        "Home",
        "Sports",
        "Beauty",
        "Furniture",
        "Groceries",
        "Toys",
        "Automotive",
        "Jewellery",
        "Footwear",
        "Appliances",
        "Stationery",
        "Gaming"
    ]

    bst = BinarySearchTree()

    for category in categories:
        bst.insert(category)

    print("Inorder traversal:")
    bst.inorder(bst.root)

    print("\nPreorder traversal:")
    bst.preorder(bst.root)

    print("\nPostorder traversal:")
    bst.postorder(bst.root)

    print("\n\nSearch Electronics:", bst.search("Electronics"))
    print("Search Pharmacy:", bst.search("Pharmacy"))

    print("\nTASK 2: HASHING AND HASHMAP")

    custom_hash = HashTable(5)

    custom_hash.insert("SKU100", "Laptop")
    custom_hash.insert("SKU105", "Mobile")
    custom_hash.insert("SKU300", "Keyboard")

    print("Hash table:", custom_hash.table)
    print("SKU100 lookup:", custom_hash.search("SKU100"))

    collision_found = any(
        len(bucket) > 1 for bucket in custom_hash.table
    )

    print("Collision demonstrated:", collision_found)

    random.seed(42)

    sku_data = {
        f"SKU{i}": f"Product{i}"
        for i in range(100000)
    }

    lookup_keys = [
        f"SKU{i}" for i in range(0, 100000, 10)
    ]

    start = time.perf_counter()

    for key in lookup_keys:
        custom_value = sku_data.get(key)

    hashmap_time = time.perf_counter() - start

    large_hash = HashTable(200003)

    for key, value in sku_data.items():
        large_hash.insert(key, value)

    start = time.perf_counter()

    for key in lookup_keys:
        large_value = large_hash.search(key)

    custom_time = time.perf_counter() - start

    print("Total SKUs:", len(sku_data))
    print("Lookups performed:", len(lookup_keys))
    print("Built-in dictionary lookup time:", round(hashmap_time, 6))
    print("Custom hash table lookup time:", round(custom_time, 6))

    print("\nTASK 3: GRAPH AND DEPLOYMENT DEPENDENCIES")

    graph = {
        "cart": ["pricing"],
        "pricing": ["inventory"],
        "inventory": ["payment"],
        "payment": ["notification"],
        "notification": []
    }

    print("Dependency graph:", graph)
    print("BFS traversal:", graph_bfs(graph, "cart"))
    print("DFS traversal:", graph_dfs(graph, "cart"))

    deployment_order = topological_sort(graph)
    print("Valid deployment order:", deployment_order)

    cyclic_graph = {
        "cart": ["pricing"],
        "pricing": ["inventory"],
        "inventory": ["cart"]
    }

    print("Circular dependency detected:", has_cycle(cyclic_graph))

    print("\nTASK 4: SLIDING WINDOW")

    random.seed(10)
    requests = [random.randint(10, 100) for _ in range(1440)]

    window_size = 180

    start_minute, maximum_requests = busiest_window(
        requests, window_size
    )

    print("Total hourly data points:", len(requests))
    print("Window duration:", window_size, "minutes")
    print("Busiest window starts at minute:", start_minute)
    print("Busiest window ends at minute:", start_minute + window_size)
    print("Maximum requests in 3-hour window:", maximum_requests)
    print("Average requests per minute:", round(maximum_requests / window_size, 2))

    print("\nTASK 5: TWO POINTERS")

    order_values = [
        10, 20, 30, 40, 50, 60, 70, 80, 90, 100
    ]

    gift_card_value = 100

    pairs = find_pairs(order_values, gift_card_value)

    print("Sorted order values:", order_values)
    print("Gift card value:", gift_card_value)
    print("Matching pairs:")

    for pair in pairs:
        print(pair)

    print("\nALL FIVE TASKS COMPLETED")


if __name__ == "__main__":
    main()
