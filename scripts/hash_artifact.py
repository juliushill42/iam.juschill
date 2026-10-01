from pathlib import Path
import hashlib
p=Path("IAM-Identity-Mesh-dist.zip")
print(hashlib.sha256(p.read_bytes()).hexdigest(), p)
