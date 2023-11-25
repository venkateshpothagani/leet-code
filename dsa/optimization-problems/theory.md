# Important Points

1. Optimization problems involve finding the best possible solution, either maximizing or minimizing a certain value.

2. The goal is to find the most efficient solution among all the possible options.

3. Three commonly used strategies for optimization are the greedy method, dynamic programming, and branch & bound.

Ex: Knapsack Problem

1. GREEDY METHOD:

    1. Makes local optimal solutions to find global optimal solution

    ```py
    def greedy_knapsack(weights, values, capacity):
        n = len(weights)
        ratio = [values[i] / weights[i] for i in range(n)]
        index = sorted(range(n), key=lambda i: ratio[i], reverse=True)
        max_value = 0
        knapsack = [0] * n
        
        for i in index:
            if weights[i] <= capacity:
                knapsack[i] = 1
                max_value += values[i]
                capacity -= weights[i]
        
        return max_value, knapsack
    ```

2. DYNAMIC PROGRAMMING

    > Divides problem into sub problems ,solves sub problems by storing their values.

    ```py
    def dynamic_knapsack(weights, values, capacity):
        n = len(weights)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(capacity + 1):
                if weights[i - 1] <= w:
                    dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
                else:
                    dp[i][w] = dp[i - 1][w]

        max_value = dp[n][capacity]
        return max_value
    ```

3. BRANCH & BOUND

    > Systematically explores the solution space by dividing it into subsets and pruning branches that cannot lead to an optimal solution.

    ```py
    class Node:
        def __init__(self, level, value, weight, bound, include):
            self.level = level
            self.value = value
            self.weight = weight
            self.bound = bound
            self.include = include


    def branch_and_bound_knapsack(weights, values, capacity):
        n = len(weights)
        root = Node(0, 0, 0, 0, [0] * n)
        queue = [root]
        max_value = 0

        while queue:
            current = queue.pop(0)

            if current.bound > max_value:
                left_child = Node(
                    current.level + 1,
                    current.value + values[current.level],
                    current.weight + weights[current.level],
                    current.bound,
                    current.include[:],
                )

                left_child.include[current.level] = 1

                if left_child.weight <= capacity and left_child.value > max_value:
                    max_value = left_child.value

                left_child.bound = bound(left_child, weights, values, capacity, n)

                if left_child.bound > max_value:
                    queue.append(left_child)

                right_child = Node(
                    current.level + 1,
                    current.value,
                    current.weight,
                    current.bound,
                    current.include[:],
                )

                right_child.include[current.level] = 0

                right_child.bound = bound(right_child, weights, values, capacity, n)

                if right_child.bound > max_value:
                    queue.append(right_child)

        return max_value


    def bound(node, weights, values, capacity, n):
        if node.weight >= capacity:
            return 0

        bound_value = node.value

        j = node.level + 1
        total_weight = node.weight

        while j < n and total_weight + weights[j] <= capacity:
            bound_value += values[j]
            total_weight += weights[j]
            j += 1

        if j < n:
            bound_value += (capacity - total_weight) * (values[j] / weights[j])

        return bound_value
    ```
