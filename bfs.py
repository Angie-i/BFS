def bfs(n, adj, start):
    visited = [False] * n
    queue = []
    head = 0
    order = []
    visited[start] = True
    queue.append(start)
    while head < len(queue):
        v = queue[head]
        head += 1
        order.append(v)
        for to in adj[v]:
            if 0 <= to < n and not visited[to]:
                visited[to] = True
                queue.append(to)

    return order


def read_ints(path: str):
    ints = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for token in f.read().split():
                try:
                    ints.append(int(token))
                except ValueError:
                    pass
    except FileNotFoundError:
        return None
    return ints

def write_output(path: str, order):
    with open(path, "w", encoding="utf-8") as f:
        f.write(" ".join(map(str, order)))


def main():
    data = read_ints("input.txt")
    if not data or len(data) < 2:
        write_output("output.txt", [])
        return
    n, m = data[0], data[1]
    if n <= 0 or m < 0:
        write_output("output.txt", [])
        return
    need = 2 + 2 * m + 1
    if len(data) < need:
        write_output("output.txt", [])
        return
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u, v = data[idx], data[idx + 1]
        idx += 2
        if 0 <= u < n and 0 <= v < n:
            adj[u].append(v)
            adj[v].append(u)

    start = data[idx]
    if not (0 <= start < n):
        write_output("output.txt", [])
        return

    order = bfs(n, adj, start)
    write_output("output.txt", order)

if __name__ == "__main__":
    main()