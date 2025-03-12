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

# Would you like to explore **real-world use cases of stacks** next? 😊
