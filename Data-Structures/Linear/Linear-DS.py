# **📚 Linear Data Structures – In-Depth Explanation**

# A **Linear Data Structure** arranges elements **sequentially**, meaning each element has a **direct predecessor and successor** (except the first and last elements).

# ✅ **Key Characteristics:**
# - Stored in **a single level (one after another)**
# - **Easier to implement** than non-linear structures
# - **Memory-efficient** when elements are accessed sequentially

# ---

## **📌 1. Arrays – Fixed-Size Containers**
# 💡 **Analogy:** **A row of lockers** in a school where each locker has an index (number).
# 🔧 **Use Cases:**
# - **Storing sensor data** (e.g., temperature logs)
# - **Game high scores**
# - **Image pixels (2D array)**

# ### **Python Example**
# ```python
# arr = [10, 20, 30, 40, 50]
# print(arr[2])  # Accessing index 2 (Output: 30)
# ```
# ⏳ **Time Complexity:**
# - **Access:** O(1)
# - **Search:** O(n)
# - **Insert/Delete:** O(n)

# ---

## **📌 2. Linked List – A Train with Carriages**
# 💡 **Analogy:** **A train** where each carriage (node) is linked to the next.
# 🔧 **Use Cases:**
# - **Undo feature** in software (text editors, Photoshop)
# - **Dynamic memory allocation**
# - **Navigation (browser forward/back buttons)**


# ### **Python Example**
# ```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


ll = LinkedList()
ll.head = Node(10)
ll.head.next = Node(20)
# ```
# ⏳ **Time Complexity:**
# - **Access:** O(n)
# - **Insert/Delete:** O(1) (if head/tail known)

# ---

## **📌 3. Stack – Last In, First Out (LIFO)**
# 💡 **Analogy:** **A stack of plates** in a cafeteria – you take the top plate first.
# 🔧 **Use Cases:**
# - **Function calls (Recursion Stack)**
# - **Undo operations** in editors
# - **Backtracking algorithms** (e.g., solving a maze)

### **Python Example**
stack = []
stack.append(10)  # Push
stack.append(20)
print(stack.pop())  # Pop (Output: 20)
# ```
# ⏳ **Time Complexity:**
# - **Push:** O(1)
# - **Pop:** O(1)

# ---

## **📌 4. Queue – First In, First Out (FIFO)**
# 💡 **Analogy:** **A queue at a ticket counter** – the first person in line gets served first.
# 🔧 **Use Cases:**
# - **CPU task scheduling**
# - **Print job queue**
# - **Breadth-First Search (BFS) in graphs**

### **Python Example**
from collections import deque

queue = deque()
queue.append(10)  # Enqueue
queue.append(20)
print(queue.popleft())  # Dequeue (Output: 10)
# ```
# ⏳ **Time Complexity:**
# - **Enqueue:** O(1)
# - **Dequeue:** O(1)

# ---

## **📌 5. Deque (Double-Ended Queue) – Insert/Delete from Both Ends**
# 💡 **Analogy:** **A train with doors on both sides** – you can enter/exit from front or back.
# 🔧 **Use Cases:**
# - **Sliding window problems** (e.g., max of subarrays)
# - **Undo/redo operations**

# ### **Python Example**
# ```python
# dq = deque()
# dq.append(10)   # Add to right
# dq.appendleft(20)  # Add to left
# print(dq.pop())  # Remove from right (Output: 10)
# ```
# ⏳ **Time Complexity:**
# - **Insert/Delete (Both Ends):** O(1)

# ---

# **🎯 Summary Table**
# | **Data Structure** | **Analogy** | **Best For** | **Insertion** | **Deletion** | **Access/Search** |
# |-------------------|------------|-------------|-------------|------------|---------------|
# | **Array** | Row of lockers | Fast indexed access | O(n) | O(n) | O(1) / O(n) |
# | **Linked List** | Train with carriages | Dynamic memory, frequent insertions | O(1) | O(1) | O(n) |
# | **Stack** | Plates stack | Function calls, undo operations | O(1) | O(1) | O(n) |
# | **Queue** | People in line | Scheduling, BFS | O(1) | O(1) | O(n) |
# | **Deque** | Train with doors on both ends | Sliding window problems | O(1) | O(1) | O(n) |
