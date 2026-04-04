import os

folder_path = "/Users/elango/Desktop/dl_project/chershil_raw_data"

for filename in os.listdir(folder_path):
    
    # Skip directories
    if os.path.isdir(os.path.join(folder_path, filename)):
        continue

    # Split name and extension
    name, ext = os.path.splitext(filename)

    parts = name.split("_")
    
    # Ensure format like XX_YY
    if len(parts) == 2:
        new_name = f"{parts[0]}_chershil_{parts[1]}{ext}"
        
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        
        os.rename(old_path, new_path)
        
        print(f"{filename} → {new_name}")

print("Done!")