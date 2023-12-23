import os

local = os.listdir(r"C:\Users\kira\Projects\picacg-qt\src\downloads\pack")
remote = os.listdir(r"\\192.168.3.77\Komga\hentai")

local_set = set(local)
remote_set = set(remote)

print(local_set - remote_set)
