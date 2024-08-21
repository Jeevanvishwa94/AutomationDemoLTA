# generate_report.py

import json
import matplotlib
import matplotlib.pyplot as plt

def generate_chart():
    # Load the JSON report
    with open('reports/report.json', 'r') as f:
        report = json.load(f)

    # Extract data
    test_cases = report['tests']
    statuses = [test['outcome'] for test in test_cases]

    # Count occurrences of each status
    status_counts = {status: statuses.count(status) for status in set(statuses)}

    # Prepare data for plotting
    labels = status_counts.keys()
    sizes = status_counts.values()

    # Create a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Test Results')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Save and show the plot
    plt.savefig('reports/test_results_chart.png')
    plt.show()

if __name__ == '__main__':
    generate_chart()
