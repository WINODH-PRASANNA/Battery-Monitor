# Battery Monitor ⚡🔋

A simple Python script that monitors your system's battery level and sends a notification when it reaches 100%, reminding you to unplug the charger and help preserve battery health.

## Features 🎯

- Real-time battery monitoring ⏱️
- Desktop notifications when the battery is fully charged 🔔
- Cross-platform support (Windows, Linux, macOS) 🌐

## Requirements ⚙️

- Python 3.x 🐍
- External libraries:
  - `psutil` 📦
  - `plyer` 📲


- Standard libraries:
  - `time`⏳ (comes with Python)

## Installation 💻

Install the required Python libraries using:

```bash
pip install psutil plyer
```

## Usage 🏃‍♂️

Run the script with:

```bash
python main.py
```

- Checks battery status every 30 seconds ⏰.
- Sends a desktop notification when battery is 100% and plugged in 🔌🔋.
- After notifying, waits 30 minutes before checking again to avoid repeated alerts ⛔.

## Notes 📝

- `time` is a standard Python module and does not require installation 🚫.
- If your system does not have a battery, the script will exit with a message ⚠️.
- Notifications depend on OS support for `plyer`  📱.

## License 📝

This project is licensed under the MIT License.
