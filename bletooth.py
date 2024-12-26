import subprocess
import re

def scan_bluetooth_devices():
    """Scans for nearby classic Bluetooth devices using system commands."""
    print("Scanning for Bluetooth devices...")

    try:
        # Run the system command to scan for Bluetooth devices
        result = subprocess.run(["hcitool", "scan"], capture_output=True, text=True, check=True)
        output = result.stdout

        # Parse the output to extract device information
        devices = []
        for line in output.splitlines():
            match = re.search(r"([0-9A-F:]{17})\s+(.+)", line)
            if match:
                addr, name = match.groups()
                devices.append((addr, name))

        # Print the results
        if not devices:
            print("No devices found.")
        else:
            print(f"Found {len(devices)} devices:")
            for addr, name in devices:
                print(f"  Device Name: {name}, MAC Address: {addr}")
    except FileNotFoundError:
        print("Error: The 'hcitool' command is not available. Ensure it is installed and accessible.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while scanning: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    scan_bluetooth_devices()
