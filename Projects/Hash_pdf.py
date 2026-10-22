import hashlib
def get_file_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename,"rb") as file:
        for chunk in iter(lambda: file.read(8192),b""):
            sha256.update(chunk)
    return sha256.hexdigest()

hash1 = get_file_hash("file1.pdf")
hash2 = get_file_hash("file2.pdf")

print(hash1 == hash2)