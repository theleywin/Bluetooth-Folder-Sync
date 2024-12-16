# Bluetooth File Synchronization

## Overview
This project implements a Bluetooth-based file synchronization system designed for seamless transfer and synchronization of files between two devices. The system monitors a specific folder for file changes (creation, modification, deletion) and ensures that changes are reflected on the peer device.

The project is modularized into several scripts for better maintainability and readability.

## Features
- **Automatic File Synchronization**: Detects file changes and synchronizes them with a paired device.
- **File Deletion Notification**: Notifies and removes files deleted from the source device.
- **Bluetooth Communication**: Uses Bluetooth RFCOMM for device-to-device communication.
- **Modular Design**: Separated into distinct modules for configuration, server, client, and event handling.

## Project Structure
```
|-- config.py         # Configuration for Bluetooth and folder paths
|-- server.py         # Bluetooth server for receiving files
|-- client.py         # Bluetooth client for sending files and notifications
|-- sync_handler.py   # Handles file system events (creation, modification, deletion)
|-- main.py           # Entry point for starting the server and folder monitoring
|-- sync_folder/      # Folder to monitor for synchronization
```

## Installation

### Prerequisites
- Python 3.8 or higher
- `pybluez` library for Bluetooth communication
- `watchdog` library for monitoring file system changes

Install the dependencies using:
```bash
pip install pybluez watchdog
```

### Folder Setup
Ensure that the folder `sync_folder` exists in the project directory. This folder will be used for synchronization.

## Usage

### Configuration
1. Open the `config.py` file.
2. Set the following variables:
   - `LOCAL_MAC`: Bluetooth MAC address of the local device.
   - `PEER_MAC`: Bluetooth MAC address of the paired device.
   - `PORT`: The Bluetooth port (default is `30`).
   - `SYNC_FOLDER`: Path to the folder to monitor.

### Running the System
Start the system by running `main.py`:
```bash
python main.py
```
This will:
- Start the Bluetooth server to receive files.
- Begin monitoring the `sync_folder` for file changes.

## Modules

### `config.py`
Contains configuration variables, including Bluetooth addresses, port, and folder paths.

### `server.py`
Implements the Bluetooth server that:
- Listens for incoming file transfers.
- Receives files or deletion notifications.
- Saves received files to the `sync_folder`.

### `client.py`
Implements functions to:
- Send files to the peer device.
- Notify the peer device of file deletions.

### `sync_handler.py`
Handles file system events using the `watchdog` library:
- Detects file creation, modification, and deletion in `sync_folder`.
- Triggers corresponding actions (e.g., file transfer, deletion notification).

### `main.py`
Combines all modules and initializes:
- The Bluetooth server in a separate thread.
- The folder monitoring system.

## Troubleshooting

### Common Issues
1. **Bluetooth Connection Errors**: Ensure both devices have Bluetooth enabled and are discoverable.
2. **Permission Errors**: Run the script with the necessary permissions (e.g., `sudo` on Linux).
3. **Infinite Sync Loops**: The `sync_handler` includes a flag (`is_receiving`) to prevent re-triggering events caused by incoming transfers. Verify its usage if issues persist.

### Debugging
Check the console logs for detailed messages about file synchronization and Bluetooth connections.

## Future Improvements
- Implement conflict resolution for simultaneous file modifications.
- Add encryption for secure file transfers.
- Create a GUI for easier configuration and monitoring.

## License
This project is open-source and available under the MIT License.

