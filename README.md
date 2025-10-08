

# LayCoder-Data

This repository contains the processed dataset subsets **DS1** and **DS2** used in the paper:

> **LayCoder: UI Layout Completion with an Encoder-Only Transformer and Layout Tokenizer**

---

## 📘 Overview

The **LayCoder** project focuses on UI layout completion using an encoder-only transformer architecture.  
This repository provides the **processed layout data** used for model training, validation, and testing.

- The data is derived from the **LayoutTransformer++** dataset ([Microsoft Research](https://github.com/microsoft/LayoutGeneration/tree/main/LayoutFormer++)),  
  which itself is based on the **Rico dataset** ([https://interactionmining.org/rico.html](https://interactionmining.org/rico.html)).
- We further preprocessed the original layouts to create two subsets, **DS1** and **DS2**, designed for different experimental configurations.
- Each subset contains **train**, **validation**, and **test** partitions serialized as `.pkl` files.

---

## 📂 Dataset Structure


| Folder | Description |
|---------|--------------|
| `DS1/` | Subset 1 – used for baseline training and primary evaluation |
| `DS2/` | Subset 2 – alternative processed version for comparison and ablation experiments |

Each `.pkl` file contains a Python list of layout objects, formatted for direct use with the LayCoder data loaders.

---

## ⚙️ Usage Example

```python
import pickle

# Load training data from DS1
with open('DS1/train_DS1.pkl', 'rb') as f:
    train_data = pickle.load(f)

print(f"Loaded DS1 training set with {len(train_data)} samples.")






