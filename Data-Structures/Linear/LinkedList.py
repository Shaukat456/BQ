# ### **📌 Linked List: A Deep Dive**

# A **Linked List** is a **linear** data structure, just like an array, but with one major difference:
# 🔹 **Elements (nodes) are not stored in contiguous memory locations.**
# 🔹 **Each node stores data + a pointer (or link) to the next node.**

# Unlike arrays, which use **indexes** to access elements, linked lists use **pointers** to navigate between nodes.

# ---

# # **📌 Why Use Linked Lists?**
# ### **✅ Problem with Arrays**
# 1. **Fixed Size:** Arrays have a **fixed size** (static allocation). If we need more space, we must create a new larger array and copy elements.
# 2. **Costly Insertions & Deletions:** To insert or delete elements **in the middle** of an array, we must **shift elements**, which is slow (**O(n)** time complexity).

# ### **✅ How Linked Lists Solve These Issues**
# ✔ **Dynamic Size:** Can grow or shrink without needing memory reallocation.
# ✔ **Efficient Insertions/Deletions:** No need to shift elements—just change pointers.

# ---

# # **📌 Types of Linked Lists**
# There are three main types:

# | Type | Structure | Characteristics |
# |------|-----------|----------------|
# | **Singly Linked List (SLL)** | Each node has a `data` field and a `next` pointer to the next node. | **One-directional**, can only traverse forward. |
# | **Doubly Linked List (DLL)** | Each node has `data`, a `next` pointer, and a `prev` pointer. | **Two-directional**, can traverse both forward and backward. |
# | **Circular Linked List (CLL)** | The last node’s `next` pointer links back to the first node. | Forms a **circular chain**, no `NULL` at the end. |

# ---

# # **📌 Singly Linked List (SLL)**
# Each **node** has:
# 1. **Data** (stores value)
# 2. **Next pointer** (points to the next node)

# ### **💡 Visual Representation of an SLL**
# ```
# HEAD -> [10 | ○ ] -> [20 | ○ ] -> [30 | None ]
# ```
# - The **last node** has `None` as its `next`, marking the end.


# ### **✅ Singly Linked List Implementation**
# ```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Points to the next node


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Empty list initially

    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If list is empty, set new node as head
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node  # Add new node at the end

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example Usage
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.display()  # Output: 10 -> 20 -> 30 -> None
# ```
# ### **⏳ Time Complexity of SLL**
# | Operation | Complexity |
# |-----------|------------|
# | **Insertion (at end)** | **O(n)** (traversing to last node) |
# | **Deletion (middle)** | **O(n)** (searching for the node) |
# | **Search** | **O(n)** |

# ---

# # **📌 Doubly Linked List (DLL)**
# Each **node** has:
# 1. **Data**
# 2. **Next pointer** (points to next node)
# 3. **Prev pointer** (points to previous node)

# ### **💡 Visual Representation of a DLL**
# ```
# None <- [10 | ○ | ○ ] <-> [20 | ○ | ○ ] <-> [30 | ○ | None ]
# ```
# - **Two-way navigation** possible.


# ### **✅ Doubly Linked List Implementation**
# ```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Extra pointer for backward traversal


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current  # Link back to previous node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


# Example Usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.display()  # Output: 10 <-> 20 <-> 30 <-> None
### **⏳ Time Complexity of DLL**
# | Operation | Complexity |
# |-----------|------------|
# | **Insertion (at end)** | **O(n)** |
# | **Deletion (middle)** | **O(n)** |
# | **Search** | **O(n)** |
# | **Reverse Traversal** | **O(n)** (extra pointer makes it easy) |

# ---

# **📌 Circular Linked List (CLL)**
# 🔄 **Last node points to the first node instead of `None`**.
# - **Used in CPU scheduling (Round-Robin), multiplayer gaming, OS memory allocation**.

# ### **💡 Visual Representation of a CLL**
# ```
# [10 | ○ ] -> [20 | ○ ] -> [30 | ○ ] --|
#    ^----------------------------------|
# ```
# - **No `NULL` termination** → forms a loop.


# ### **✅ Circular Linked List Implementation**
# ```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Point to itself
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head  # Point new node back to head

    def display(self):
        if not self.head:
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(Back to Head)")


# Example Usage
cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.append(30)
cll.display()  # Output: 10 -> 20 -> 30 -> (Back to Head)
### **⏳ Time Complexity of CLL**
# | Operation | Complexity |
# |-----------|------------|
# | **Insertion (at end)** | **O(n)** |
# | **Deletion (middle)** | **O(n)** |
# | **Traversal** | **O(n)** |

# ---

# **📌 When to Use Each Type?**
# | Use Case | Best Linked List Type |
# |----------|----------------------|
# | **Memory efficiency & Simple Traversal** | **Singly Linked List (SLL)** |
# | **Fast reverse traversal** | **Doubly Linked List (DLL)** |
# | **Cyclic processes (like OS Scheduling, Games, etc.)** | **Circular Linked List (CLL)** |

# ---

# # **📌 Summary**
# ✔ **Linked lists store elements as nodes** with pointers.
# ✔ **Singly Linked List (SLL):** Simple, one-way navigation.
# ✔ **Doubly Linked List (DLL):** Two-way navigation, extra memory usage.
# ✔ **Circular Linked List (CLL):** Forms a loop, used in cyclic systems.


# **📌 Advanced Operations & Use Cases of Linked Lists**

## **🔹 Additional Operations on Linked Lists**
# Apart from basic **insertion, deletion, and traversal**, there are several other important operations that can be performed on linked lists.

# | **Operation**          | **Description** | **Time Complexity** |
# |------------------------|----------------|------------------|
# | **Reverse a Linked List** | Change node links to reverse the order of nodes. | **O(n)** |
# | **Find Middle Element** | Get the middle node in a single scan. | **O(n)** |
# | **Detect Loop (Cycle Detection)** | Check if the list forms a loop using Floyd’s Cycle Detection Algorithm. | **O(n)** |
# | **Merge Two Sorted Linked Lists** | Merge two sorted lists into one sorted list. | **O(n)** |
# | **Remove Duplicates** | Remove duplicate elements from the list. | **O(n)** |
# | **Nth Node from End** | Find the Nth last element in one pass. | **O(n)** |
# | **Check if Palindrome** | Verify if a linked list forms a palindrome. | **O(n)** |
# | **Flatten a Linked List** | Convert a multi-level linked list into a single-level list. | **O(n)** |
# | **Rotate Linked List** | Shift nodes to the left or right by a given number of positions. | **O(n)** |
# | **Sort a Linked List** | Use Merge Sort or Quick Sort to sort the list. | **O(n log n)** |

# ---

# ## **🔹 Advanced Use Cases of Linked Lists**
# ### **📌 1. Dynamic Memory Allocation**
# - Since linked lists are **dynamic** (unlike arrays), they are heavily used in **memory management systems** where memory is allocated or deallocated on demand.

# 💡 **Example**:
# ✔ Used in **Operating System (OS) memory management** to keep track of **free and allocated blocks** dynamically.

# ---

# ### **📌 2. Implementing Stacks and Queues**
# - **Stacks** (LIFO) and **Queues** (FIFO) can be implemented efficiently using linked lists.
# - Unlike arrays, they don’t need **resizing** or **shifting elements**.

# 💡 **Example**:
# ✔ **Call Stack** in programming languages is implemented using a linked list.

# ---

# ### **📌 3. Graph Implementation (Adjacency List)**
# - Graphs are **best represented using linked lists**.
# - Instead of using a **matrix**, we use an **adjacency list**, where each **node** stores its connected neighbors.

# 💡 **Example**:
# ✔ Used in **Google Maps**, **Social Networks**, **AI pathfinding algorithms**.

# ---

# ### **📌 4. Web Browsers (Back/Forward Navigation)**
# - **Doubly Linked Lists** are used to implement **browser history**, allowing **forward and backward traversal**.

# 💡 **Example**:
# ✔ When you press **Back (<-) or Forward (->)** in a browser, it moves through a **linked list of previously visited pages**.

# ---

# ### **📌 5. Undo/Redo Functionality**
# - **Doubly Linked Lists** are also used in applications where we need **undo/redo** functionality.

# 💡 **Example**:
# ✔ **Microsoft Word, Photoshop, VS Code** use linked lists to **store history for undo/redo actions**.

# ---

# ### **📌 6. Music Playlist / Media Player**
# - Songs in a playlist are linked together in a **Circular Doubly Linked List**.
# - **Previous and Next buttons** work using **prev/next pointers**.

# 💡 **Example**:
# ✔ **Spotify, VLC, YouTube Playlist Navigation**

# ---

# ### **📌 7. Polynomial Arithmetic & Big Integer Calculations**
# - Large numbers in **cryptography** and **scientific computing** can’t be stored in primitive data types.
# - **Each digit of a number can be stored in a linked list**, allowing **arithmetic operations** without memory limitations.

# 💡 **Example**:
# ✔ **RSA Encryption**, **Polynomial Multiplication**.

# ---

# ### **📌 8. Blockchains & Cryptographic Hashing**
# - **Each block in a blockchain** stores:
#   - Data
#   - A link (pointer) to the **previous block**.
# - The **entire blockchain** acts as a **linked list** where each block references the previous one.

# 💡 **Example**:
# ✔ **Bitcoin, Ethereum, Other Cryptocurrencies** use a **linked list-like structure**.

# ---

# ### **📌 9. Real-Time CPU Scheduling (Circular Linked List)**
# - **Round-Robin Scheduling** in OS uses **Circular Linked Lists** to allocate CPU time to processes.

# 💡 **Example**:
# ✔ **Multitasking in Operating Systems (Windows, Linux)**.

# ---

# ### **📌 10. Garbage Collection in Programming**
# - Languages like **Java & Python** use **Doubly Linked Lists** to track objects in memory.
# - The **Garbage Collector (GC)** removes objects that are **no longer referenced**.

# 💡 **Example**:
# ✔ **JVM Garbage Collection, Python Memory Management**

# ---

# # **📌 When to Use Linked Lists?**
# | **Use Case** | **Best Data Structure** |
# |-------------|-----------------------|
# | **Need dynamic memory allocation** | **Linked List** |
# | **Frequent Insertions & Deletions** | **Linked List** |
# | **Need random access** | **Array** |
# | **Memory is limited** (avoid extra pointers) | **Array** |

# ---

# ## **📌 Summary**
# ✔ Linked Lists **support advanced operations** like reversing, detecting loops, sorting, etc.
# ✔ Used in **OS, databases, graphs, undo/redo, blockchains, and memory management**.
# ✔ **Different types** (Singly, Doubly, Circular) are used based on the requirements.
