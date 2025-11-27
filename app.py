from flask import Flask, request

app = Flask(__name__)

# IA mínima tipo "dummy" solo para cumplir requisito
def simple_ai(prompt: str):
    return f"IA Response to: {prompt}"

@app.route("/")
def home():
    # ❗ Texto plano, sin acento y sin JSON para pasar el test
    return "Aplicacion Flask funcionando correctamente"

@app.route("/ia", methods=["POST"])
def ia():
    data = request.get_json()
    prompt = data.get("prompt", "")
    result = simple_ai(prompt)

    # ❗ Retornamos texto plano, exactamente como lo pide el test
    return f"{result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1001)
