import hashlib

# for hash genarate fucntion

def generate_hash(text):

    text = text.encode("utf-8")

    hash_object = hashlib.sha256(text)

    return hash_object.hexdigest()



# if __name__ == "__main__":
#     password = "123456"

#     hashed_password = generate_hash(password)
#     print("original password", password)
#     print("Hasing password", hashed_password)

# function for hash verify

def verify_hash(text, stored_hash):
    generate_hash(text)

    # compare the hash with databash hash file
    new_hash = generate_hash(text)
    if new_hash == stored_hash:

        return True
    else:
        return False