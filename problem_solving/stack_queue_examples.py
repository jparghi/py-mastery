"""Stack and queue examples using list and collections.deque."""

from collections import deque

def valid_parentheses(s: str) -> bool:
    stack = []
    pairs = {')':'(', ']':'[', '}':'{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack

def bfs_levels(adj, start):
    q = deque([start])
    seen = {start}
    order = []
    while q:
        cur = q.popleft()
        order.append(cur)
        for nxt in adj.get(cur, []):
            if nxt not in seen:
                seen.add(nxt); q.append(nxt)
    return order

if __name__ == "__main__":
    print(valid_parentheses("([]){}"))  # True
    graph = {1:[2,3], 2:[4], 3:[4], 4:[]}
    print(bfs_levels(graph, 1))
