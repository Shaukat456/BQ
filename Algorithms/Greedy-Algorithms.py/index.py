# **🚀 Greedy Algorithms – The Smart Decision-Makers!**

## **📌 What is a Greedy Algorithm?**
# A **Greedy Algorithm** makes **locally optimal** (best at the moment) choices at each step in hopes of finding the **globally optimal** (best overall) solution.

# ### **🍕 Real-World Analogy: Choosing the Shortest Route**
# Imagine you’re **driving to a destination** 🏁, and at every intersection, you:
# ✅ **Always take the shortest road** available.

# This **may** get you to the best route, but sometimes, a **longer initial road** could have been a better choice overall.

# 💡 That’s how **Greedy Algorithms** work! They make decisions **step by step**, hoping it leads to the best final solution.

# ---

# ## **⚡ Characteristics of Greedy Algorithms**
# ✅ **Makes decisions step-by-step**
# ✅ **No backtracking** (it doesn't go back to fix choices)
# ✅ **Fast and simple** but **not always optimal**

# ---

## **🔍 Real-World Use Cases of Greedy Algorithms**

### **1️⃣ Activity Selection Problem – Scheduling Meetings**
# 📅 **Problem:** Suppose you are given multiple meetings with **start and end times**. You need to **schedule the maximum number of non-overlapping meetings**.

# 💡 **Solution:** Always **choose the meeting that ends the earliest**, so more meetings can fit later!

# ---

# ### **2️⃣ Huffman Encoding – File Compression (ZIP, JPEG, MP3)**
# 🎵 **Problem:** How does your **MP3, JPEG, or ZIP file reduce size** without losing important data?

# 💡 **Solution:**
# ✅ More **frequent characters get shorter codes**
# ✅ Less **frequent characters get longer codes**
# ✅ Saves space without losing quality!

# 🔧 **Used in:**
# 📂 File compression (ZIP, RAR)
# 🎵 Audio & video compression (MP3, JPEG)

# ---

# Huffman Coding Implementation
import heapq
from collections import defaultdict, Counter


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0]


def build_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        build_codes(node.left, prefix + "0", codebook)
        build_codes(node.right, prefix + "1", codebook)
    return codebook


def huffman_encoding(text):
    root = build_huffman_tree(text)
    codebook = build_codes(root)
    encoded_text = "".join(codebook[char] for char in text)
    return encoded_text, root


def huffman_decoding(encoded_text, root):
    decoded_text = []
    node = root
    for bit in encoded_text:
        node = node.left if bit == "0" else node.right
        if node.char is not None:
            decoded_text.append(node.char)
            node = root
    return "".join(decoded_text)


# Example usage
text = "this is an example for huffman encoding"
encoded_text, tree = huffman_encoding(text)
print("Encoded Text:", encoded_text)
decoded_text = huffman_decoding(encoded_text, tree)
print("Decoded Text:", decoded_text)

# ---

### **3️⃣ Kruskal’s Algorithm – Building Minimum Cost Networks**
# 🌉 **Problem:** You need to **connect multiple cities with roads**, but you want to **minimize the total construction cost**.

# 💡 **Solution:**
# ✅ **Pick the cheapest road first**
# ✅ **Keep adding roads that don’t create a loop**
# ✅ **Stop when all cities are connected**

# 🔧 **Used in:**
# 📡 **Network Design** (Internet, Telephone, Electrical Grids)
# 🚗 **Transport Systems** (Railway Networks, Road Networks)

# ---


# Kruskal's Algorithm Implementation
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def kruskal(vertices, edges):
    mst = []
    disjoint_set = DisjointSet(vertices)
    edges.sort(key=lambda x: x[2])  # Sort edges by weight

    for edge in edges:
        u, v, weight = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst.append(edge)

    return mst


# Example usage
vertices = ["A", "B", "C", "D", "E"]
edges = [
    ("A", "B", 1),
    ("A", "C", 3),
    ("B", "C", 1),
    ("B", "D", 6),
    ("C", "D", 4),
    ("C", "E", 2),
    ("D", "E", 5),
]

mst = kruskal(vertices, edges)
print("Minimum Spanning Tree:", mst)

# ---

### **4️⃣ Dijkstra’s Algorithm – Google Maps & GPS Navigation**
# 🗺️ **Problem:** Finding the **shortest route** from one location to another on a **map**.

# 💡 **Solution:**
# ✅ Always **choose the nearest unvisited city** first
# ✅ Continue until the **destination is reached**

# 🔧 **Used in:**
# 🚕 **Google Maps, Uber Routes, Flight Ticket Pricing**

# ---


# Dijkstra's Algorithm Implementation
def dijkstra(graph, start):
    import heapq

    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Example usage
graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1},
}

start_vertex = "A"
distances = dijkstra(graph, start_vertex)
print(f"Distances from {start_vertex}:", distances)

# ---

## **💻 Greedy Algorithm in Action – Python Code!**


### **📌 Example 1: Activity Selection (Meeting Room Problem)**
def activity_selection(activities):
    activities.sort(key=lambda x: x[1])  # Sort by end time
    selected = [activities[0]]  # Always pick the first activity

    for i in range(1, len(activities)):
        if (
            activities[i][0] >= selected[-1][1]
        ):  # If start time is after last selected end time
            selected.append(activities[i])

    return selected


# Example usage
activities = [(1, 3), (2, 5), (4, 6), (6, 8), (5, 7)]
print("Selected Activities:", activity_selection(activities))

# ✅ **Sorted meetings by end time**
# ✅ **Selected the maximum number of non-overlapping meetings**

# ---

# ## **⏳ Time Complexity of Greedy Algorithms**
# Most greedy algorithms run in **O(n log n)** because of sorting, making them **fast and efficient**!

# ---

## **🎯 When to Use Greedy Algorithms?**
# | ✅ **Use Greedy When** | ❌ **Don’t Use Greedy When** |
# |-----------------|------------------|
# | Making **locally best** choices gives the **global best** result | You might need to **backtrack** for a better solution |
# | Sorting and picking **smallest/largest** values works | Decisions **depend on previous choices** |
# | Problems with **greedy choice property** (e.g., shortest path, Huffman coding) | You need to **explore multiple paths** (like in dynamic programming) |

# ---

# ## **🚀 Conclusion**
# Greedy Algorithms are **fast, simple, and work well for many real-world problems** like:
# ✅ **Scheduling meetings** (Activity Selection)
# ✅ **File Compression** (Huffman Encoding)
# ✅ **Route Optimization** (Dijkstra’s Algorithm)
# ✅ **Network Design** (Kruskal’s Algorithm)

# 💡 But **be careful!** Greedy **doesn’t always** guarantee the best solution. If backtracking is needed, **Dynamic Programming** is a better choice!
