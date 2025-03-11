import csv
import matplotlib.pyplot as plt

def plot_histogram(labels, values, column_name):
    """Plots a histogram (bar chart) based on CSV data."""
    plt.bar(labels, values, color='skyblue')
    plt.xlabel('Categories')
    plt.ylabel(column_name)
    plt.title(f'Histogram of {column_name}')
    plt.xticks(rotation=45)  # Rotate labels for better readability
    plt.show()

def read_csv_and_plot(file_path):
    """Reads a CSV file and generates a histogram from user-selected columns."""
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Extract column headers
            
            print("\nAvailable columns:", headers)
            category_col = input("Enter the column name for categories (e.g., Product, Month): ").strip()
            value_col = input("Enter the column name for values (e.g., Sales, Expenditure): ").strip()
            
            if category_col not in headers or value_col not in headers:
                print("Error: One or both column names do not exist. Please check the column names.")
                return
            
            category_index = headers.index(category_col)
            value_index = headers.index(value_col)

            labels = []
            values = []

            for row in reader:
                labels.append(row[category_index])
                try:
                    values.append(float(row[value_index]))  # Convert values to float
                except ValueError:
                    print(f"Skipping invalid data: {row[value_index]} (Not a number)")
                    continue

        if labels and values:
            plot_histogram(labels, values, value_col)
        else:
            print("Error: No valid numerical data found in the selected column.")
    
    except FileNotFoundError:
        print("Error: File not found. Please check the file path and try again.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# User input for CSV file
file_path = input("Enter the path to the CSV file: ")
read_csv_and_plot(file_path)
