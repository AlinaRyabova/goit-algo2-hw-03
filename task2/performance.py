import timeit

def measure_performance(func, structure, *args, repetitions=100):
    """Вимірювання часу виконання функції."""
    # Передаємо тільки необхідні аргументи в lambda
    timer = timeit.Timer(lambda: func(structure, *args))
    total_time = timer.timeit(repetitions)
    return total_time
