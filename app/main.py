import datetime
import os
import subprocess
import platform
from time import sleep

operating_sys = platform.system()

log_file = os.getenv("LOG_FILE")

def ping(ip):
    ping_command = ['ping', ip, '-n', '1'] if operating_sys == 'Windows' else ['ping', ip, '-c1']
    print(ping_command, flush=True)
    shell_needed = True if operating_sys == 'Windows' else False

    ping_output = subprocess.run(ping_command, shell=shell_needed, stdout=subprocess.PIPE)
    output = str(ping_output.stdout)
    success = ping_output.returncode
    if operating_sys == 'Windows':
        return (True, ip, output[output.find("Average = ") + len("Average = "):]) if success == 0 else (False, ip)
    else:
        return(True, ip, (output[output.find("time=") + len("time="):][:output.find("ms")-output.find("time=") + 2])) if success == 0 else (False, ip)


ping_list = []

for line in open("ping_addresses.txt", "r").readlines():
    ping_list.append(str(line.strip()))


while True:
    logs = []
    for address in ping_list:
        ping_result = ping(address)
        print(ping_result)

        if ping_result[0]:
            log_text = f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] PING {address} - {ping_result[2][:ping_result[2].find('ms') + 2]}."
        else:
            log_text = f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] PING {address} - FAILED."

        logs.append(log_text)

    f = open(log_file, "a")

    for log in logs:
        f.write(log + "\n")

    f.close()
    sleep(int(os.getenv("LOG_FREQUENCY", 64)))
