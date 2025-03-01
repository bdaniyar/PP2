import os

def check_access(path):
    if not os.path.exists(path):
        return f"Path '{path}' does not exist."

    result = []
    result.append(f"Path '{path}' exists.")
    result.append(f"Readable: {'Yes' if os.access(path, os.R_OK) else 'No'}")
    result.append(f"Writable: {'Yes' if os.access(path, os.W_OK) else 'No'}")
    result.append(f"Executable: {'Yes' if os.access(path, os.X_OK) else 'No'}")
    
    return "\n".join(result)


path = input("Enter the path: ").strip()
print(check_access(path))
