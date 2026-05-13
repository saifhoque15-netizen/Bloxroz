import time
import matplotlib.pyplot as plt

class Block:
    __slots__ = ['pos1', 'pos2']

    def __init__(self, start_position):
        self.pos1 = start_position
        self.pos2 = start_position

    def __eq__(self, other):
        if not isinstance(other, Block):
            return False
        return sorted([self.pos1, self.pos2]) == sorted([other.pos1, other.pos2])

    def __hash__(self):
        # Every time an Object is added, it is forced to run this slow Python logic
        positions = sorted([self.pos1, self.pos2])
        return hash((positions[0], positions[1]))

    def get_state(self):
        positions = sorted([self.pos1, self.pos2])
        return (positions[0], positions[1])

# ==========================================
# RUN THE FAIR BENCHMARK
# ==========================================
state_counts = [10000, 20000, 30000, 40000, 50000]
object_times = []
tuple_times = []

print("Running fair benchmark... Please wait.")

for num_states in state_counts:
    # 1. PRE-GENERATE ALL DATA (Outside the stopwatch!)
    test_objects = []
    test_tuples = []
    for i in range(num_states):
        b = Block((i, i))
        b.pos2 = (i, i+1)
        test_objects.append(b)
        test_tuples.append(b.get_state()) # Convert BEFORE starting the timer

    # 2. Benchmark Storing Full Objects (Slow due to __hash__ python execution)
    start_time = time.time()
    visited_objects = set()
    for obj in test_objects:
        visited_objects.add(obj)
    object_times.append(time.time() - start_time)

    # 3. Benchmark Storing Raw Tuples (Lightning fast native C-hashing)
    start_time = time.time()
    visited_tuples = set()
    for tup in test_tuples:
        visited_tuples.add(tup)
    tuple_times.append(time.time() - start_time)

# ==========================================
# GENERATE THE PLOT
# ==========================================
plt.figure(figsize=(8, 5))

# Plotting both lines
plt.plot(state_counts, object_times, marker='o', color='red', label='Object Storage (Custom Hash)', linewidth=2)
plt.plot(state_counts, tuple_times, marker='o', color='blue', label='Tuple Storage (Native Hash)', linewidth=2)

# Formatting the chart for the report
plt.title('State Space Tracking: Object vs. Tuple Over Time', fontsize=14)
plt.xlabel('Number of States Explored', fontsize=12)
plt.ylabel('Execution Time (seconds)', fontsize=12)
plt.xticks(state_counts, ['10k', '20k', '30k', '40k', '50k'])
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()