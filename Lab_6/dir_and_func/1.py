import os

def list_contents(path):
    print("Directories:")
    print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])  

    print("\nFiles:")
    print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])  

    print("\nAll contents:")
    print(os.listdir(path)) 


path = input("Enter the path: ").strip()  
list_contents(path)
