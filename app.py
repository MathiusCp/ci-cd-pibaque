from flask import Flask, request, jsonify

app = Flask(__name__)

# IA mínima tipo "dummy" solo para cumplir requisito
def simple_ai(prompt: str):
    return f"IA Response to: {prompt}"

@app.route("/")
def home():
    return jsonify({"message": "Aplicación Flask funcionando correctamente"})

@app.route("/ia", methods=["POST"])
def ia():
    data = request.get_json()
    prompt = data.get("prompt", "")
    result = simple_ai(prompt)
    return jsonify({"response": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1001)
