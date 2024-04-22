# hanoi = lambda n, s, a, d: hanoi(n-1, s, d, a) or print(f"Move disk {n} from {s} to {d}") or hanoi(n-1, a, s, d) if n else None
# hanoi(3, 'A', 'B', 'C')  # Example usage


def hanoi(n, source, auxiliary, destination):
    if n == 0:
        return
    hanoi(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n-1, auxiliary, source, destination)

# Initial call to solve Tower of Hanoi for 3 disks
hanoi(3, 'A', 'B', 'C')
