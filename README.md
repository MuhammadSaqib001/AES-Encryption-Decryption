# AES Encryption and Decryption using Python [Info-Sec BS Project]

This project rovides an implementation of the Advanced Encryption Standard (AES) algorithm for encryption and decryption using Python. AES is a widely used symmetric encryption algorithm known for its security and efficiency.

## Description

The notebook demonstrates the step-by-step process of AES encryption and decryption, utilizing the `cryptography` library in Python. The encryption process involves applying substitution, permutation, and mixing operations to a plaintext message along with a secret encryption key, resulting in ciphertext. The decryption process reverses these operations to retrieve the original plaintext.

## How to Use

Follow these steps to run the AES algorithm successfully:

1. Open the Jupyter Notebook file `AES.ipynb` in your Jupyter environment.
2. Ensure the following files are in the same folder as the notebook:
   - `k.key`: Contains the initial encryption key.
   - `input.pt`: Contains the plaintext to be encrypted.
3. Run the notebook cells sequentially. These cells will perform encryption and decryption using the provided key and input text.
4. The results of encryption will be stored in `encryption.enc`, and decryption results will be stored in `encryption.dec`. Both files will be generated in the same folder as the notebook.

## Important Notes

- Keep `k.key` and `input.pt` files in the same directory as the notebook; these files are used for the initial key and plaintext.
- The notebook requires the `cryptography` library. Install it with: `pip install cryptography`.

Feel free to experiment with different plaintexts and keys to gain a better understanding of AES encryption and decryption.
