from django.http import JsonResponse
from collections import deque

def water_jug_solver(request):
    jug1, jug2, target = 4, 3, 2
    visited = set()
    q = deque([(0, 0, [])])

    while q:
        a, b, path = q.popleft()
        if (a, b) in visited:
            continue
        visited.add((a, b))

        path = path + [(a, b)]
        if a == target or b == target:
            return JsonResponse({"solution": path})

        q.extend([
            (jug1, b, path),              # fill jug1
            (a, jug2, path),              # fill jug2
            (0, b, path),                 # empty jug1
            (a, 0, path),                 # empty jug2
            (min(jug1, a+b), max(0, a+b-jug1), path),  # pour jug2 → jug1
            (max(0, a+b-jug2), min(jug2, a+b), path)   # pour jug1 → jug2
        ])

    return JsonResponse({"solution": "No solution"})
