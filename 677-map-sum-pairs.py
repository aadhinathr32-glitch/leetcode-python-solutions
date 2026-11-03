class MapSum:

    def __init__(self):
        self.map = {}

    def insert(self, key, val):
        self.map[key] = val

    def sum(self, prefix):
        total = 0

        for key in self.map:
            if key.startswith(prefix):
                total += self.map[key]

        return total


if __name__ == "__main__":
    map_sum = MapSum()
    map_sum.insert("apple", 3)
    assert map_sum.sum("ap") == 3

    map_sum.insert("app", 2)
    assert map_sum.sum("ap") == 5

    # Updating an existing key replaces its previous value.
    map_sum.insert("apple", 7)
    assert map_sum.sum("ap") == 9
    assert map_sum.sum("app") == 9

    print("All sample tests passed.")
