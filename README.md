# Backdoor

This is a server side backdoor that has the ability to execute shell commands, capture and exfiltrate sensitive data, and persist across system reboots.


## Usage

1. Replace `{server_ip}` and `{port}` in `main.py` with your server IP and port.
2. Start the backdoor by running `python main.py`.
3. Use `utils/shell.py` to send commands to the backdoor.
4. Use `utils/exfiltrate.py` to exfiltrate data from the compromised system.
5. Use `utils/persist.py` to make the backdoor persist across system reboots.

Note: Use at your own risk. This software is meant for educational purposes only. The author is not responsible for any illegal usage of this software.
