import os
import psutil # type: ignore

for proc in psutil.process_iter(['name', 'exe']):
    if proc.info['name'] == 'LeagueClient.exe':
        klasor = os.path.dirname(proc.info['exe'])
        print("Klasör:", klasor)
        print("Dosyalar:", os.listdir(klasor))

LOCKFILE_PATH = f"{klasor}/lockfile"

with open(LOCKFILE_PATH) as f:
    content = f.read()
print("Lockfile içeriği:", content)