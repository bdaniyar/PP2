import shutil

def copy_file(source, destination):
    try:
        shutil.copyfile(source, destination)  
        print(f"File '{source}' successfully copied to '{destination}'")
    except FileNotFoundError:
        print(f"Error: File '{source}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


source_file = "source.txt"
destination_file = "destination.txt"

copy_file(source_file, destination_file)
