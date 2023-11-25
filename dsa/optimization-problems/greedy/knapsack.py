'''
Knapsack problem 
'''

def fractional_knapsack(weights, values, capacity):
    """
    Calculate the maximum profit that can be obtained by selecting items with the highest 
    value-to-weight ratio and filling the knapsack up to its capacity.

    Args:
        weights (list): A list of positive integers representing the weights of the items.
        values (list): A list of positive integers representing the values of the items.
        capacity (int): The maximum weight the knapsack can hold.

    Returns:
        knapsack (list): A list of integers representing the weights of the selected 
        items in the knapsack.
        profit (float): The maximum profit that can be obtained by selecting the items.

    Raises:
        ValueError: If the capacity is negative.
        ValueError: If the lengths of `weights` and `values` are not equal.
        ValueError: If any weight or value is negative.

    Example:
        weights = [2, 3, 5, 7]
        values = [10, 5, 15, 7]
        capacity = 10
        knapsack, profit = fractional_knapsack(weights, values, capacity)
        print(knapsack)  # Output: [2, 3, 5, 0]
        print(profit)  # Output: 24
    """

    if capacity < 0:
        raise ValueError("Capacity cannot be negative.")

    if len(weights) != len(values):
        raise ValueError("The lengths of `weights` and `values` must be equal.")

    for index, item in enumerate(zip(weights, values)):
        if item[0] < 0 or item[1] < 0:
            raise ValueError("Weights and values must be non-negative.")

    n = len(weights)
    average_profits = [[values[i] / weights[i], weights[i]] for i in range(n)]

    sorted_profits = sorted(average_profits, key=lambda x: x[0], reverse=True)

    knapsack = [0] * n
    profit = 0

    index = 0
    while capacity > 0 and index < len(sorted_profits):
        item = sorted_profits[index]
        if capacity <= item[1]:
            knapsack[index] = capacity
            profit += capacity * item[0]
            capacity = 0
        else:
            knapsack[index] = item[1]
            profit += item[1] * item[0]
            capacity -= item[1]
        index += 1

    return knapsack, profit

 
 0
