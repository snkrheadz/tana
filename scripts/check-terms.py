"""Fail if a tracked file contains a banned word.

The banned words are stored as SHA-256 hashes of their lowercase form, so this file does
not spell them out. Usage: python3 -I scripts/check-terms.py
"""
import hashlib
import re
import subprocess
import sys

BANNED = {
    "7171b73fae682f6d9ecd7f5df1e32181db261468c2819ee5f79f0bb55c83d700",
    "6381c40ceb0409268122819671f163463fa571bcf27a37a819356159924d0706",
}

files = subprocess.run(["git", "ls-files", "-z"], capture_output=True, check=True).stdout.split(b"\0")
hits = []
for name in filter(None, files):
    path = name.decode()
    try:
        text = open(path, encoding="utf-8").read().lower()
    except (UnicodeDecodeError, IsADirectoryError, FileNotFoundError):
        continue
    for n, line in enumerate(text.splitlines(), 1):
        for word in re.findall(r"[a-z0-9]+", line):
            if hashlib.sha256(word.encode()).hexdigest() in BANNED:
                hits.append(f"{path}:{n}")
if hits:
    print("banned word in:\n" + "\n".join(hits))
    sys.exit(1)
print(f"OK {len([f for f in files if f])} files")
