import os

folder = "screws_clean"
name = "screw"
for i, image in enumerate(os.listdir(folder)):
    old_path = os.path.join(folder, image)
    new_path = os.path.join(folder, f"{name}_{i}.jpeg")
    os.rename(old_path, new_path)