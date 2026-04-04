import os
import subprocess

# Folder containing your WAV files
folder_path = "/Users/elango/Desktop/dl_project/own_dataset"

for filename in os.listdir(folder_path):
    if filename.lower().endswith(".wav"):
        input_path = os.path.join(folder_path, filename)
        temp_path = os.path.join(folder_path, "temp_" + filename)

        print(f"Processing: {filename}")

        # Run ffmpeg command
        command = [
            "ffmpeg",
            "-i", input_path,
            "-ar", "8000",     # set sample rate to 8kHz
            "-ac", "1",        # mono (optional but recommended)
            "-sample_fmt", "s16",
            "-y",              # overwrite temp file if exists
            temp_path
        ]

        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Replace original file
        os.replace(temp_path, input_path)

print("✅ All files converted to 8 kHz and replaced.")