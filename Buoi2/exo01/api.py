from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher  

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

# Chạy ứng dụng
if __name__ == "__main__":  # "nếu _name_ '_main_':" => "if __name__ == '__main__':"
    app.run(host="0.0.0.0", port=5000, debug=True)  # "debug=Đúng" => "debug=True"
