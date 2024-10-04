import random
import time

# Global list for storing blocked IPs
blocked_ips = []


# Mock traffic data generator
def generate_traffic():
    traffic_types = ["normal", "normal", "normal", "suspicious", "normal", "normal", "malicious"]
    return random.choice(traffic_types)


# Log the traffic activity
def log_traffic(activity, log_file="traffic_log.txt"):
    with open(log_file, "a") as file:
        file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {activity}\n")


# Simulate traffic monitoring
def monitor_traffic():
    print("Monitoring traffic...")
    while True:
        traffic = generate_traffic()
        print(f"Traffic detected: {traffic}")
        log_traffic(traffic)
        time.sleep(1)


# Detect anomalies from the logs
def detect_anomalies(log_file="traffic_log.txt"):
    with open(log_file, "r") as file:
        lines = file.readlines()

    anomaly_count = 0
    for line in lines:
        if "suspicious" in line or "malicious" in line:
            anomaly_count += 1

    return anomaly_count


# Alert the user based on anomaly count
def alert_user(anomaly_count):
    if anomaly_count > 3:
        print(f"ALERT! {anomaly_count} suspicious activities detected!")
    else:
        print("No significant threat detected.")


# Block IP address automatically if malicious traffic is detected
def block_ip(ip_address):
    if ip_address not in blocked_ips:
        blocked_ips.append(ip_address)
        print(f"IP address {ip_address} has been blocked.")


# Automated response system based on detected traffic
def automatic_response(log_file="traffic_log.txt"):
    with open(log_file, "r") as file:
        lines = file.readlines()

    for line in lines:
        if "malicious" in line:
            ip_address = f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"
            block_ip(ip_address)


# Display a simple command-line dashboard
def display_dashboard(log_file="traffic_log.txt"):
    print("\nCloudGuard Dashboard")
    print("-------------------")
    print("Recent Activity Logs:")

    with open(log_file, "r") as file:
        lines = file.readlines()[-10:]  # Display last 10 activities
        for line in lines:
            print(line.strip())

    anomaly_count = detect_anomalies()
    print(f"\nDetected Anomalies: {anomaly_count}")
    alert_user(anomaly_count)


# Main function to run all components
def run_cloudguard():
    # Run traffic monitoring in a background thread
    import threading
    monitor_thread = threading.Thread(target=monitor_traffic)
    monitor_thread.daemon = True
    monitor_thread.start()

    while True:
        # Run anomaly detection, auto response, and display dashboard every 10 seconds
        time.sleep(10)
        print("\n[INFO] Running anomaly detection and automated responses...")
        anomalies = detect_anomalies()
        automatic_response()
        display_dashboard()


if __name__ == "__main__":
    run_cloudguard()
