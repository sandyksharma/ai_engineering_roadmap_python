"""Python data structures and common operations.

This module keeps the examples intentionally explicit.  It is useful as a
practice/reference file for Python fundamentals plus common DSA building
blocks such as stack, queue, heap, linked list, tree traversal, and graph
traversal.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from heapq import heappop, heappush
from typing import Any, Iterable

# ------------------------------------------------------------------
# Node classes for linked list and binary tree
# ------------------------------------------------------------------
@dataclass
class ListNode:
    """Node for a singly linked list."""

    value: Any
    next: "ListNode | None" = None


@dataclass
class TreeNode:
    """Node for a binary tree."""

    value: Any
    left: "TreeNode | None" = None
    right: "TreeNode | None" = None


class PythonDataStructures:
    """Reference implementations for Python data structures.

    The class stores one instance of each core structure and exposes methods
    for the operations learners usually practice: create, add, remove, search,
    traverse, sort, merge, and inspect.
    """

    def __init__(self) -> None:
        # Core data structures used by the methods below.  They are initialized as empty and mutated by the methods. 
        self.array: list[Any] = []
        self.stack: list[Any] = []
        self.queue: deque[Any] = deque()
        self.priority_queue: list[tuple[int, Any]] = []
        self.hash_set: set[Any] = set()
        self.hash_map: dict[Any, Any] = {}
        self.linked_list_head: ListNode | None = None
        self.graph: defaultdict[Any, list[Any]] = defaultdict(list)

    # ------------------------------------------------------------------
    # List / dynamic array
    # ------------------------------------------------------------------
    def list_create(self, values: Iterable[Any] = ()) -> list[Any]:
        self.array = list(values)
        return self.array

    def list_append(self, value: Any) -> list[Any]:
        self.array.append(value)
        return self.array

    def list_extend(self, values: Iterable[Any]) -> list[Any]:
        self.array.extend(values)
        return self.array

    def list_insert(self, index: int, value: Any) -> list[Any]:
        self.array.insert(index, value)
        return self.array

    def list_remove_value(self, value: Any) -> list[Any]:
        self.array.remove(value)
        return self.array

    def list_pop(self, index: int = -1) -> Any:
        return self.array.pop(index)

    def list_search(self, value: Any) -> int:
        try:
            return self.array.index(value)
        except ValueError:
            return -1

    def list_sort(self, reverse: bool = False) -> list[Any]:
        self.array.sort(reverse=reverse)
        return self.array

    def list_reverse(self) -> list[Any]:
        self.array.reverse()
        return self.array

    def list_slice(self, start: int | None = None, end: int | None = None, step: int | None = None) -> list[Any]:
        return self.array[slice(start, end, step)]

    def list_count(self, value: Any) -> int:
        return self.array.count(value)

    # ------------------------------------------------------------------
    # Tuple
    # ------------------------------------------------------------------
    @staticmethod
    def tuple_create(values: Iterable[Any] = ()) -> tuple[Any, ...]:
        return tuple(values)

    @staticmethod
    def tuple_index(values: tuple[Any, ...], value: Any) -> int:
        try:
            return values.index(value)
        except ValueError:
            return -1

    @staticmethod
    def tuple_count(values: tuple[Any, ...], value: Any) -> int:
        return values.count(value)

    @staticmethod
    def tuple_unpack_pair(values: tuple[Any, Any]) -> tuple[Any, Any]:
        first, second = values
        return first, second

    # ------------------------------------------------------------------
    # String
    # ------------------------------------------------------------------
    @staticmethod
    def string_length(text: str) -> int:
        return len(text)

    @staticmethod
    def string_reverse(text: str) -> str:
        return text[::-1]

    @staticmethod
    def string_is_palindrome(text: str) -> bool:
        normalized = "".join(char.lower() for char in text if char.isalnum())
        return normalized == normalized[::-1]

    @staticmethod
    def string_split(text: str, separator: str | None = None) -> list[str]:
        return text.split(separator)

    @staticmethod
    def string_join(values: Iterable[str], separator: str = "") -> str:
        return separator.join(values)

    @staticmethod
    def string_frequency(text: str) -> Counter[str]:
        return Counter(text)

    # ------------------------------------------------------------------
    # Set
    # ------------------------------------------------------------------
    def set_create(self, values: Iterable[Any] = ()) -> set[Any]:
        self.hash_set = set(values)
        return self.hash_set

    def set_add(self, value: Any) -> set[Any]:
        self.hash_set.add(value)
        return self.hash_set

    def set_remove(self, value: Any) -> set[Any]:
        self.hash_set.remove(value)
        return self.hash_set

    def set_discard(self, value: Any) -> set[Any]:
        self.hash_set.discard(value)
        return self.hash_set

    def set_contains(self, value: Any) -> bool:
        return value in self.hash_set

    @staticmethod
    def set_union(first: set[Any], second: set[Any]) -> set[Any]:
        return first | second

    @staticmethod
    def set_intersection(first: set[Any], second: set[Any]) -> set[Any]:
        return first & second

    @staticmethod
    def set_difference(first: set[Any], second: set[Any]) -> set[Any]:
        return first - second

    @staticmethod
    def set_symmetric_difference(first: set[Any], second: set[Any]) -> set[Any]:
        return first ^ second

    # ------------------------------------------------------------------
    # Dictionary / hash map
    # ------------------------------------------------------------------
    def dict_create(self, pairs: Iterable[tuple[Any, Any]] = ()) -> dict[Any, Any]:
        self.hash_map = dict(pairs)
        return self.hash_map

    def dict_set(self, key: Any, value: Any) -> dict[Any, Any]:
        self.hash_map[key] = value
        return self.hash_map

    def dict_get(self, key: Any, default: Any = None) -> Any:
        return self.hash_map.get(key, default)

    def dict_delete(self, key: Any) -> dict[Any, Any]:
        del self.hash_map[key]
        return self.hash_map

    def dict_keys(self) -> list[Any]:
        return list(self.hash_map.keys())

    def dict_values(self) -> list[Any]:
        return list(self.hash_map.values())

    def dict_items(self) -> list[tuple[Any, Any]]:
        return list(self.hash_map.items())

    def dict_merge(self, other: dict[Any, Any]) -> dict[Any, Any]:
        self.hash_map.update(other)
        return self.hash_map

    # ------------------------------------------------------------------
    # Stack: last in, first out
    # ------------------------------------------------------------------
    def stack_push(self, value: Any) -> list[Any]:
        self.stack.append(value)
        return self.stack

    def stack_pop(self) -> Any:
        if self.stack_is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def stack_peek(self) -> Any:
        if self.stack_is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    def stack_is_empty(self) -> bool:
        return not self.stack

    # ------------------------------------------------------------------
    # Queue / deque: first in, first out
    # ------------------------------------------------------------------
    def queue_enqueue(self, value: Any) -> deque[Any]:
        self.queue.append(value)
        return self.queue

    def queue_dequeue(self) -> Any:
        if self.queue_is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.popleft()

    def queue_peek(self) -> Any:
        if self.queue_is_empty():
            raise IndexError("peek from empty queue")
        return self.queue[0]

    def queue_is_empty(self) -> bool:
        return not self.queue

    # ------------------------------------------------------------------
    # Priority queue / min heap
    # ------------------------------------------------------------------
    def heap_push(self, priority: int, value: Any) -> list[tuple[int, Any]]:
        heappush(self.priority_queue, (priority, value))
        return self.priority_queue

    def heap_pop(self) -> tuple[int, Any]:
        if not self.priority_queue:
            raise IndexError("pop from empty priority queue")
        return heappop(self.priority_queue)

    def heap_peek(self) -> tuple[int, Any]:
        if not self.priority_queue:
            raise IndexError("peek from empty priority queue")
        return self.priority_queue[0]

    # ------------------------------------------------------------------
    # Linked list
    # ------------------------------------------------------------------
    def linked_list_insert_front(self, value: Any) -> ListNode:
        self.linked_list_head = ListNode(value, self.linked_list_head)
        return self.linked_list_head

    def linked_list_insert_back(self, value: Any) -> ListNode:
        new_node = ListNode(value)
        if self.linked_list_head is None:
            self.linked_list_head = new_node
            return new_node

        current = self.linked_list_head
        while current.next is not None:
            current = current.next
        current.next = new_node
        return new_node

    def linked_list_delete(self, value: Any) -> bool:
        previous: ListNode | None = None
        current = self.linked_list_head

        while current is not None:
            if current.value == value:
                if previous is None:
                    self.linked_list_head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next

        return False

    def linked_list_search(self, value: Any) -> bool:
        current = self.linked_list_head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def linked_list_to_list(self) -> list[Any]:
        values: list[Any] = []
        current = self.linked_list_head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values

    # ------------------------------------------------------------------
    # Binary tree traversal
    # ------------------------------------------------------------------
    def tree_inorder(self, root: TreeNode | None) -> list[Any]:
        if root is None:
            return []
        return self.tree_inorder(root.left) + [root.value] + self.tree_inorder(root.right)

    def tree_preorder(self, root: TreeNode | None) -> list[Any]:
        if root is None:
            return []
        return [root.value] + self.tree_preorder(root.left) + self.tree_preorder(root.right)

    def tree_postorder(self, root: TreeNode | None) -> list[Any]:
        if root is None:
            return []
        return self.tree_postorder(root.left) + self.tree_postorder(root.right) + [root.value]

    def tree_level_order(self, root: TreeNode | None) -> list[Any]:
        if root is None:
            return []

        values: list[Any] = []
        nodes: deque[TreeNode] = deque([root])
        while nodes:
            node = nodes.popleft()
            values.append(node.value)
            if node.left is not None:
                nodes.append(node.left)
            if node.right is not None:
                nodes.append(node.right)
        return values

    # ------------------------------------------------------------------
    # Graph: adjacency list
    # ------------------------------------------------------------------
    def graph_add_vertex(self, vertex: Any) -> defaultdict[Any, list[Any]]:
        self.graph[vertex]
        return self.graph

    def graph_add_edge(self, source: Any, destination: Any, undirected: bool = True) -> defaultdict[Any, list[Any]]:
        self.graph[source].append(destination)
        if undirected:
            self.graph[destination].append(source)
        return self.graph

    def graph_bfs(self, start: Any) -> list[Any]:
        visited = {start}
        order: list[Any] = []
        vertices: deque[Any] = deque([start])

        while vertices:
            vertex = vertices.popleft()
            order.append(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    vertices.append(neighbor)

        return order

    def graph_dfs(self, start: Any) -> list[Any]:
        visited: set[Any] = set()
        order: list[Any] = []

        def visit(vertex: Any) -> None:
            visited.add(vertex)
            order.append(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visit(neighbor)

        visit(start)
        return order

    # ------------------------------------------------------------------
    # General helper algorithms
    # ------------------------------------------------------------------
    @staticmethod
    def linear_search(values: list[Any], target: Any) -> int:
        for index, value in enumerate(values):
            if value == target:
                return index
        return -1

    @staticmethod
    def binary_search(sorted_values: list[Any], target: Any) -> int:
        left = 0
        right = len(sorted_values) - 1

        while left <= right:
            middle = (left + right) // 2
            if sorted_values[middle] == target:
                return middle
            if sorted_values[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1

    @staticmethod
    def frequency_map(values: Iterable[Any]) -> Counter[Any]:
        return Counter(values)


if __name__ == "__main__":
    structures = PythonDataStructures()

    structures.list_create([3, 1, 2])
    structures.list_append(4)
    structures.list_sort()

    structures.stack_push("first")
    structures.stack_push("second")
    structures.stack_pop()
    print("Stack peek:", structures.stack_peek())

    structures.queue_enqueue("first")
    structures.queue_enqueue("second")

    structures.graph_add_edge("A", "B")
    structures.graph_add_edge("A", "C")

    print("List:", structures.array)
    print("Stack pop:", structures.stack_pop())
    print("Queue dequeue:", structures.queue_dequeue())
    print("Graph BFS:", structures.graph_bfs("A"))
