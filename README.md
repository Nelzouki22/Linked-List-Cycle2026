# 🚀 Linked List Cycle — Detect Cycle in a Linked List  
LeetCode Problem #141  
Difficulty: Easy  

---

# 📘 Description (English)

Given the `head` of a linked list, determine whether the list contains a **cycle**.  
A cycle exists if any node in the list is revisited by continuously following `next` pointers.

LeetCode internally uses `pos` to indicate which node the tail points to, but **`pos` is NOT a parameter** in the function.  
You must simply detect whether a cycle exists.

### ✅ Return:
- `True` → if a cycle exists  
- `False` → if no cycle exists  

---

# 📘 الشرح بالعربي

المطلوب هو معرفة هل تحتوي **قائمة مرتبطة (Linked List)** على **حلقة (Cycle)** أم لا.

الحلقة تعني أن أحد العقد يشير إلى عقدة سابقة، مما يجعل الربط دائريًا عند تتبع `next`.  
نستمر في المشي داخل القائمة… فإذا رجعنا لعقدة رأيناها سابقًا → إذن يوجد **Cycle**.

`pos` في السؤال فقط للمحاكاة ولا يدخل في الحل.

### ✅ الإرجاع:
- `True` → توجد حلقة داخل الـ Linked List  
- `False` → لا توجد حلقة  

---

# 🔍 Examples

### Example 1
Input:
head = [3,2,0,-4], pos = 1
Cycle:
3 → 2 → 0 → -4
↑ |
|_______|
Output:
True

---

### Example 2
Input:
head = [1,2], pos = 0
Cycle:
Cycle:
1 → 2
↑ |
|____|

Output:
True

---

### Example 3
Input:
head = [1], pos = -1
List:
1 → None
Output:
False


---

# 🧠 Algorithm — Floyd’s Cycle Detection (Tortoise & Hare)

We use two pointers:

- 🐢 **slow pointer** → moves 1 step at a time  
- 🐇 **fast pointer** → moves 2 steps at a time  

### Logic:
- If the list has **no cycle**, the fast pointer will reach `None`
- If there **is a cycle**, fast will eventually meet slow inside the loop

### Why this works?
Because the fast pointer “laps” the slow pointer, just like running on a circular track.

---

# 🧩 الخوارزمية — شرح عربي مبسّط

نعمل بمؤشرين:

- **slow** يتحرك خطوة واحدة
- **fast** يتحرك خطوتين

إذا لم توجد حلقة:
- fast سيصل إلى `None` وينتهي

إذا وجدت حلقة:
- المستعرضان سيقابلان بعضهما في نقطة داخل الدورة → يوجد Cycle

---

# 🧮 Time & Space Complexity

| Complexity | Value |
|-----------|--------|
| **Time**  | `O(n)` |
| **Space** | `O(1)` |

لا نستخدم أي مساحة إضافية — فقط مؤشرين ثابتين.

---

# 🧑‍💻 Python Code (O(1) Memory) — Official Solution

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next         # move 1 step
            fast = fast.next.next    # move 2 steps

            if slow == fast:         # they meet -> cycle exists
                return True
        
        return False  # fast reached null -> no cycle
📊 ASCII Visual Diagram (Cycle vs No Cycle)
✔ Cycle Linked List
3 → 2 → 0 → -4
      ↑       |
      |_______|
✘ No Cycle Linked List
1 → 2 → 3 → 4 → None
📁 Project Structure
📦 linked-list-cycle
│
├── README.md
└── solution.py
✨ Notes for Beginners

This is one of the most famous Linked List problems.

Floyd’s algorithm is used in competitive programming and interview questions.

No need to modify the list or use sets — the algorithm is optimal.

❤️ Happy Coding!

A clean, efficient, beginner-friendly solution for detecting cycles in linked lists.
