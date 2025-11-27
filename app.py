from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Página Premium</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">

    <style>
        body {
            margin: 0;
            font-family: "Poppins", sans-serif;
            background: #0e0e0e;
            color: white;
        }

        header {
            background: linear-gradient(135deg, #4e54c8, #8f94fb);
            padding: 80px 20px;
            text-align: center;
            color: white;
            animation: fadeIn 1.2s ease-in-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h1 {
            font-size: 3.2rem;
            font-weight: 600;
            margin-bottom: 10px;
        }

        h2 {
            font-size: 2.2rem;
            font-weight: 600;
        }

        p {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        .section {
            padding: 40px 20px;
            max-width: 900px;
            margin: auto;
            text-align: center;
            animation: fadeSection 1.2s ease-in-out;
        }

        @keyframes fadeSection {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .card {
            background: #1a1a1a;
            border-radius: 15px;
            padding: 30px;
            margin-top: 20px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        }

        a.btn {
            display:inline-block;
            margin-top: 20px;
            padding: 14px 26px;
            background: #8f94fb;
            color: white;
            border-radius: 30px;
            font-weight: bold;
            text-decoration: none;
            transition: 0.3s;
        }

        a.btn:hover {
            background: #4e54c8;
        }

        footer {
            margin-top: 60px;
            padding: 20px;
            text-align: center;
            color: #888;
            font-size: 0.9rem;
        }
    </style>
</head>

<body>

<header>
    <h1>Página Premium</h1>
    <p>Diseño moderno totalmente dentro del return</p>
</header>

<div class="section">
    <div class="card">
        <h2>Hola 👋</h2>
        <p>Un servidor me trajo aquí… pero ahora sí da gusto quedarse 😎</p>
        <a href="/" class="btn">Botón de prueba</a>
    </div>
</div>

<footer>
    © 2025 pgmoreno.byronrm.com – powered by Flask ✨
</footer>

</body>
</html>
"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1001)