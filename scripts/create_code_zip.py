import os
import zipfile

def create_code_zip():
    zip_filename = "Kaleva_Tasku_Source_Code.zip"
    exclude_dirs = {"node_modules", "dist", ".git", "test_video_out", "raw_scene_1", "raw_scene_2", "raw_scene_3", "raw_scene_4", "raw_scene_5", "video_parts", "__pycache__"}
    exclude_extensions = {".webm", ".mp4"}

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk("."):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for file in files:
                if any(file.endswith(ext) for ext in exclude_extensions) and "Demo_Video" in file:
                    continue
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, ".")
                if rel_path == zip_filename:
                    continue
                zipf.write(file_path, rel_path)

    size_mb = os.path.getsize(zip_filename) / (1024 * 1024)
    print(f"Created {zip_filename} ({size_mb:.2f} MB)")

if __name__ == '__main__':
    create_code_zip()
