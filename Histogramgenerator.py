import csv
import random
import matplotlib.pyplot as plt

def generate_random_count():
    # Replace with your preferred random number generation logic
    return random.randint(1, 100)  # Example: Generates counts between 1 and 100

def plot_histogram(alphabets, counts):
    plt.hist(alphabets, bins=26)
    plt.xlabel('Alphabet')
    plt.ylabel('Count')
    plt.title('Histogram of Alphabet Counts')
    plt.show()

# Generate CSV file
with open('alphabet_counts.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['alphabet', 'count'])
    for alphabet in chr(65, 90):  # Iterate from A (65) to Z (90)
        count = generate_random_count()
        writer.writerow([alphabet, count])

# Read CSV file and prepare data for histogram
alphabets = []
counts = []
with open('alphabet_counts.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    for row in reader:
        alphabets.append(row[0])
        counts.append(int(row[1]))

# Plot histogram
plot_histogram(alphabets, counts)
