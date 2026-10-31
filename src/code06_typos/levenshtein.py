class Levenshtein:
    """Levenshtein Distance dengan Dynamic Programming."""
    @staticmethod
    def distance(a, b):
        a, b = a.lower(), b.lower()
        if len(a) < len(b):
            a, b = b, a
        previous = list(range(len(b) + 1))
        for i, ca in enumerate(a, 1):
            current = [i]
            for j, cb in enumerate(b, 1):
                insert_cost = current[j - 1] + 1
                delete_cost = previous[j] + 1
                replace_cost = previous[j - 1] + (ca != cb)
                current.append(min(insert_cost, delete_cost, replace_cost))
            previous = current
        return previous[-1]
