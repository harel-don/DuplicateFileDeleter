import os
import hashlib

def remove_duplicates(folder_path):
    """
    Removes duplicate files in a given folder and its subfolders,
    and shows how much storage was freed.

    Args:
        folder_path (str): Path to the folder to check for duplicates.
    """
    seen_hashes = {}  # Dictionary to store file hashes and their paths
    total_freed_space = 0  # Counter for storage freed

    for root, _, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = calculate_hash(file_path)  # Calculate file hash
            if file_hash in seen_hashes:
                duplicate_size = os.path.getsize(file_path)  # Get the file size
                total_freed_space += duplicate_size  # Add size to freed space
                print(f"Duplicate found: {file_path} (same as {seen_hashes[file_hash]})")
                os.remove(file_path)  # Delete duplicate file
            else:
                seen_hashes[file_hash] = file_path  # Store the unique file hash

    # Convert bytes to a human-readable format (MB)
    freed_mb = total_freed_space / (1024 * 1024)
    print(f"\nTotal storage freed: {freed_mb:.2f} MB")


def calculate_hash(file_path, chunk_size=1024):
    """
    Calculates the MD5 hash of a file for duplicate detection.

    Args:
        file_path (str): Path to the file.
        chunk_size (int): Size of chunks to read at a time.

    Returns:
        str: MD5 hash of the file.
    """
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


# Main execution
if __name__ == '__main__':
    folder_path = "C:/Users/harel/Pictures"  # Replace with your folder path
    if os.path.exists(folder_path):
        print(f"The folder exists: {folder_path}")
    else:
        print(f"The folder does not exist: {folder_path}")

    remove_duplicates(folder_path)

# C:\Users\harel\Pictures
# C:\Users\harel\Documents
