#!/usr/bin/env python3
import os, shutil
from pathlib import Path
import kagglehub

DATASET = os.getenv("KAGGLE_DATASET", "alexsalama/laycoder")  
SRC_DIR = Path(kagglehub.dataset_download(DATASET))  

# Map: repo destination -> filename inside Kaggle dataset
FILES = {
    "DS1/train_DS1.pkl": "train_DS1.pkl",
    "DS1/val_DS1.pkl":   "val_DS1.pkl",
    "DS1/test_DS1.pkl":  "test_DS1.pkl",
    "DS2/train_DS2_nonover.pkl": "train_DS2_nonover.pkl",
    "DS2/val_DS2_nonover.pkl":   "val_DS2_nonover.pkl",
    "DS2/test_DS2_nonover.pkl":  "test_DS2_nonover.pkl",
}


for dest_rel, src_name in FILES.items():
    dest = Path(dest_rel); dest.parent.mkdir(parents=True, exist_ok=True)
    src = (SRC_DIR / src_name)
    if not src.exists():
        # also check one-level subfolders if you uploaded with dirs
        cand = list(SRC_DIR.rglob(src_name))
        if not cand: raise SystemExit(f"Missing in Kaggle archive: {src_name}")
        src = cand[0]
    shutil.copyfile(src, dest)
    print(f"✔ {src_name} → {dest}")
