import os

def delete_file(file_path):
    
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return
    
    
    if not os.access(file_path, os.R_OK | os.W_OK):
        print(f"Error: No permission to delete '{file_path}'.")
        return

    try:
        os.remove(file_path)  
        print(f"File '{file_path}' has been deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_to_delete = "test.txt"  
delete_file(file_to_delete)
