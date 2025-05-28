from cipher.vigenere import VigenereCipher
from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher  
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher
app = Flask(__name__)

# Thuật toán mã hóa CAESAR
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])  # "phương thức" => "methods"
def caesar_encrypt():
    data = request.json  # "dữ liệu" => "data"
    plain_text = data['plain_text']  # "dữ liệu" => "data"
    key = int(data['key'])  # "key" => "key"
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])  # "giải mã" => "decrypt"
def caesar_decrypt():
    data = request.json  # "dữ liệu" => "data"
    cipher_text = data['cipher_text']  # "dữ liệu" => "data"
    key = int(data['key'])  # "khóa" => "key"
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)  # "văn bản giải mã" => "decrypted_text"
    return jsonify({'decrypted_message': decrypted_text})

vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key']) # Chuyển đổi key sang kiểu số nguyên
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key']) # Chuyển đổi key sang kiểu số nguyên
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

playfair_cipher = PlayFairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'playfair_matrix': playfair_matrix})

# BÀI 2: MÃ HÓA VỚI PYTHON
@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})

transposition_cipher = TranspositionCipher()

@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})
# Chạy ứng dụng
if __name__ == "__main__":  # "nếu _name_ '_main_':" => "if __name__ == '__main__':"
    app.run(host="0.0.0.0", port=5000, debug=True)  # "debug=Đúng" => "debug=True"
