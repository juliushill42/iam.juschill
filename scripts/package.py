from pathlib import Path
import zipfile
p=Path("IAM-Identity-Mesh-dist.zip")
if p.exists(): p.unlink()
with zipfile.ZipFile(p,"w",zipfile.ZIP_DEFLATED) as z:
    for f in sorted(Path("dist").rglob("*")):
        if f.is_file(): z.write(f,f.relative_to(Path(".")))
print(p)
