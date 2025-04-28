from flask import Flask, request, jsonify
import joblib
import re

# Charger le modèle entraîné
model = joblib.load('password_ai_model.pkl')

# Créer l'application Flask
app = Flask(__name__)

def extract_features(password):
    return [
        len(password),                          # Longueur totale
        sum(c.isdigit() for c in password),     # Nombre de chiffres
        sum(c.islower() for c in password),     # Nombre de minuscules
        sum(c.isupper() for c in password),     # Nombre de majuscules
        sum(c in '!@#$%^&*()' for c in password), # Nombre de symboles
        int(any(c.isdigit() for c in password)), # Contient au moins 1 chiffre (0/1)
        int(any(c in '!@#$%^&*()' for c in password)) # Contient au moins 1 symbole (0/1)
    ]

@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint API pour prédire si le mot de passe est safe ou exposé."""
    data = request.get_json()

    if not data or 'password' not in data:
        return jsonify({'error': 'Missing password'}), 400

    password = data['password']
    features = extract_features(password)

    prediction = model.predict([features])[0]

    result = {
        'password': password,
        'breached': bool(prediction)  # 1 = exposé, 0 = non exposé
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
