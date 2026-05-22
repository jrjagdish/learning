# from pathlib import Path
# import shutil
# import logging

# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

# class FileOrganizer:
#     def __init__(self, extensions_map):
#         self.extensions = extensions_map
#         self.organized_count = 0
#         logging.info("FileOrganizer initialized")
    
#     def get_category(self, ext):
#         # Your code here
#         for category,cat_list in self.extensions.items():
#             if ext in cat_list:
#                 return category
#         return "others"
        
    
#     def scan_files(self, path):
#         # Your code here
#         folder = Path(path)
#         if not folder.exists():
#             logging.error(f"Path {path} does not exist.")
#             return []
#         if not folder.is_dir():
#             logging.error(f"Path {path} is not a directory.")
#             return []
#         return [file for file in folder.iterdir() if file.is_file()]
    
#     def organize_files(self, source_path, dest_path):
#         # Your code here
#         # Remember: self.organized_count += 1 after each file move
#         folder = Path(dest_path)
#         if not folder.exists():
#             logging.error(f"Destination path {dest_path} does not exist.")
#             return []
#         if not folder.is_dir():
#             logging.error(f"Destination path {dest_path} is not a directory.")
#             return []
#         folder.mkdir(parents=True, exist_ok=True)
#         logging.info(f"Created destination folder: {dest_path}")
#         files = self.scan_files(source_path)
#         if not files:
#             logging.info(f"No files to organize in {source_path}.")
#             return []
#         try:
#             for file in files:
#                 category = self.get_category(file.suffix.lower())
#                 category_folder = folder / category
#                 category_folder.mkdir(parents=True,exist_ok=True)
#                 logging.info(f"Moving {file} to {category_folder}")
#                 shutil.move(str(file), str(category_folder / file.name))
#                 self.organized_count += 1
#         except PermissionError as e:
#             logging.error(f"Permission error: {e}")
#         except Exception as e:
#             logging.error(f"An error occurred: {e}")
    
#     def get_summary(self):
#         # Your code here
#         # Return: "Organized {self.organized_count} files"
#         return f"Organized {self.organized_count} files"


# def main():
#     extensions_map = {
#         "images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
#         "documents": ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
#         "videos": ['.mp4', '.avi', '.mkv', '.mov'],
#     }
    
#     organizer = FileOrganizer(extensions_map)
    
#     source = input("Enter source path: ")
#     dest = input("Enter destination path: ")
    
#     organizer.organize_files(source, dest)
#     print(organizer.get_summary())


# if __name__ == "__main__":
#     main()

