from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import pickle

# Key generation
def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Encrypt data
def encrypt_data(public_key, data):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted_data = cipher.encrypt(pickle.dumps(data))
    return encrypted_data

# Decrypt data
def decrypt_data(private_key, encrypted_data):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    decrypted_data = pickle.loads(cipher.decrypt(encrypted_data))
    return decrypted_data

# Homomorphic addition (trivial example with encrypted numbers)
def homomorphic_addition(enc_data1, enc_data2, private_key):
    num1 = decrypt_data(private_key, enc_data1)
    num2 = decrypt_data(private_key, enc_data2)
    result = num1 + num2
    return encrypt_data(RSA.import_key(private_key).publickey().export_key(), result)

# Example usage
private_key, public_key = generate_keys()
data1 = 10
data2 = 20

encrypted_data1 = encrypt_data(public_key, data1)
encrypted_data2 = encrypt_data(public_key, data2)

# Perform addition on encrypted data
encrypted_result = homomorphic_addition(encrypted_data1, encrypted_data2, private_key)
decrypted_result = decrypt_data(private_key, encrypted_result)

print(f"Result of addition: {decrypted_result}")
