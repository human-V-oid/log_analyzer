from database import getData
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

#PLOT REQUESTS BY IP ADDRESS
def plot_requests_by_ip(data = getData()):
    # Count the number of requests per IP address
    ip_counter = Counter(entry[1] for entry in data)

    # Plotting
    plt.figure(figsize=(10, 6))
    ips, counts = zip(*ip_counter.items())
    plt.bar(ips, counts, color='blue')
    plt.xlabel('IP Address')
    plt.ylabel('Number of Requests')
    plt.title('Number of Requests by IP Address')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

#PLOT REQUESTS OVER TIME
def plot_requests_over_time(data = getData()):
    # Extract timestamps and count requests per timestamp
    timestamps = [entry[2] for entry in data]
    timestamp_counter = Counter(timestamps)

    # Convert timestamps to datetime objects for sorting
    sorted_timestamps = sorted(timestamp_counter.keys(), key=lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

    # Plotting
    plt.figure(figsize=(12, 6))
    counts = [timestamp_counter[timestamp] for timestamp in sorted_timestamps]
    plt.plot(sorted_timestamps, counts, marker='o', linestyle='-')
    plt.xlabel('Timestamp')
    plt.ylabel('Number of Requests')
    plt.title('Number of Requests Over Time')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
