# **📌 Stacks – Last In, First Out (LIFO) Data Structure**

# A **stack** is a **linear data structure** that follows the **LIFO (Last In, First Out)** principle. The last item added (**pushed**) is the first one removed (**popped**).

# 💡 **Analogy:** **A Stack of Plates 🍽️**
# - The **last plate** placed on top is the **first one removed**.
# - Inserting and removing **happens at the same end (top)**.

# ---

# # **📌 How a Stack Works**
# ✔️ **Push** → Add an element to the **top** of the stack
# ✔️ **Pop** → Remove the **topmost** element
# ✔️ **Peek (Top)** → View the **top** element without removing it
# ✔️ **IsEmpty** → Check if the stack is empty

# ---

# **📌 Implementation of Stack**
### **1️⃣ Using Python List (Built-in)**
# Python lists can function as stacks since `append()` and `pop()` both operate at the **end** of the list (O(1) time complexity).

# ```python
stack = []  # Create an empty stack

stack.append(10)  # Push 10
stack.append(20)  # Push 20
stack.append(30)  # Push 30

print(stack.pop())  # Pop (removes 30) -> Output: 30
print(stack)  # Remaining stack: [10, 20]
# ```

# ⏳ **Time Complexity:**
# - **Push (append to end):** O(1)
# - **Pop (remove from end):** O(1)

# ---

### **2️⃣ Using `collections.deque` (More Efficient)**
# Python’s `deque` (double-ended queue) is faster than a list for stack operations.

# ```python
from collections import deque

stack = deque()  # Create an empty stack
stack.append(10)
stack.append(20)
stack.append(30)

print(stack.pop())  # Output: 30
print(stack)  # deque([10, 20])
# ```

# 🔹 **Advantage:** Unlike lists, `deque` avoids performance issues when popping elements.

# ---

### **3️⃣ Using a Linked List (Custom Implementation)**
# A **linked list-based stack** doesn’t use an array but instead **nodes** connected together.

# 💡 **Why use a Linked List?**
# ✔️ **Efficient memory usage** (No resizing issues like arrays)
# ✔️ **Faster Insert/Delete** (O(1) compared to array shifting)


# ```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return "Stack is empty"
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        return self.top.data if self.top else "Stack is empty"


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())  # Output: 30
print(stack.peek())  # Output: 20

# ⏳ **Time Complexity:**
# - **Push (O(1))** – Add new node at top
# - **Pop (O(1))** – Remove top node

# ---

# # **📌 Do We Only Use Stacks with Arrays?**
# **No!** Stacks can be implemented using:
# ✔️ **Arrays (Lists in Python)** – Simple & fast, but requires resizing
# ✔️ **Linked Lists** – More flexible, but slightly higher memory usage
# ✔️ **Queues (`deque`)** – Efficient stack operations

# ---

# **📌 When to Use Stacks?**
# ✅ **Use Stacks When:**
# ✔️ You need **LIFO** behavior (Last In, First Out)
# ✔️ **Function Call Stack** (Recursive calls use stacks)
# ✔️ **Undo/Redo functionality** in text editors
# ✔️ **Backtracking algorithms** (Maze solving, DFS)
# ✔️ **Expression evaluation** (Postfix, Prefix)

# ---

# # **📌 Summary**
# | **Implementation** | **Push Time Complexity** | **Pop Time Complexity** | **Best Use Case** |
# |----------------|----------------------|----------------------|----------------|
# | **List (Array-based)** | O(1) | O(1) | Simple use cases |
# | **Deque (`collections.deque`)** | O(1) | O(1) | More efficient than list |
# | **Linked List** | O(1) | O(1) | No resizing issues |


### **📌 Why Do We Implement Stacks Using Arrays or Linked Lists?**

# A **stack** is an **abstract data type (ADT)** that follows **LIFO (Last In, First Out)** ordering.
# Since **stacks are not built into Python**, we implement them using **arrays (lists in Python) or linked lists**.

# ---

## **📌 What Does It Mean to "Implement a Stack Using Arrays or Linked Lists"?**
# It means we use either **arrays** or **linked lists** as the **underlying data structure** to manage the stack operations (**push, pop, peek**).

# ✅ **Stack is just a concept** → It needs a **physical storage mechanism**, which can be:
# ✔ **Array-based stack** (Fixed-size, faster access)
# ✔ **Linked list-based stack** (Dynamic size, no wasted memory)

# ---

# # **📌 Stack Implementation Using Arrays (Python List)**
# In Python, we can use a **list** as an array to implement a stack:


# ### **✅ Example: Stack Using Array (Python List)**
# ```python
class StackArray:
    def __init__(self):
        self.stack = []  # Using a list as an array

    def push(self, item):
        self.stack.append(item)  # Insert at the end (top of stack)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # Remove last element
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]  # Get last element
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0


stack = StackArray()
stack.push(10)
stack.push(20)
print(stack.pop())  # Output: 20
print(stack.peek())  # Output: 10
### **🔹 How It Works?**
# - `push(item)`: Uses `.append()` to add items at the **end** (top).
# - `pop()`: Uses `.pop()` to remove the **last item**.
# - `peek()`: Accesses the **last item** without removing it.

# ### **⏳ Time Complexity (Array-Based Stack)**
# | Operation | Complexity |
# |-----------|------------|
# | **Push** (append at end) | **O(1)** |
# | **Pop** (remove from end) | **O(1)** |
# | **Peek** (access last item) | **O(1)** |

# ---

# **📌 Stack Implementation Using Linked List**
# Instead of an array, we use **nodes** (linked list elements) to form the stack.


# ### **✅ Example: Stack Using Linked List**
# ```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node


class StackLinkedList:
    def __init__(self):
        self.top = None  # Stack is initially empty

    def push(self, item):
        new_node = Node(item)  # Create new node
        new_node.next = self.top  # New node points to old top
        self.top = new_node  # New node becomes the top

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        popped_data = self.top.data
        self.top = self.top.next  # Move top pointer to next node
        return popped_data

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.top.data

    def is_empty(self):
        return self.top is None


stack = StackLinkedList()
stack.push(10)
stack.push(20)
print(stack.pop())  # Output: 20
print(stack.peek())  # Output: 10
### **🔹 How It Works?**
# - **Every element (node) is linked** to the next element.
# - **`push(item)`**: Adds a new **node at the top**.
# - **`pop()`**: Removes the **top node**.

# ### **⏳ Time Complexity (Linked List-Based Stack)**
# | Operation | Complexity |
# |-----------|------------|
# | **Push** (insert at top) | **O(1)** |
# | **Pop** (remove from top) | **O(1)** |
# | **Peek** (access top) | **O(1)** |

# ---

# # **📌 Why Use Arrays or Linked Lists for Stacks?**
# | Feature | **Array-Based Stack** | **Linked List-Based Stack** |
# |---------|----------------------|----------------------|
# | **Size** | Fixed (can be resized) | Dynamic (grows as needed) |
# | **Speed** | Fast (O(1) for push/pop) | Slightly slower (O(1) but requires extra memory for pointers) |
# | **Memory Usage** | May waste memory (preallocated space) | Uses extra memory (pointers for each node) |
# | **Best When?** | When stack size is known | When stack size is unknown |

# ---

# # **📌 When to Use Which Implementation?**
# ✅ **Use Array-Based Stack When:**
# ✔ You know the **maximum size** in advance.
# ✔ You want **fast access** to elements.
# ✔ Memory is not a major concern.

# ✅ **Use Linked List-Based Stack When:**
# ✔ You **don’t know** how many elements will be stored.
# ✔ You **want to avoid resizing overhead** of arrays.
# ✔ You don’t mind the **extra memory** for pointers.

# ---

# ## **📌 Summary**
# ✔ **A stack is an abstract data type (ADT), and we implement it using either** **arrays** (Python lists) or **linked lists**.
# ✔ **Both implementations support** push, pop, and peek **operations** efficiently (**O(1)**).
# ✔ **Arrays are faster** (direct memory access), while **linked lists are more flexible** (dynamic size).
