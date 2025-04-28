import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# 1. Charger les données
df = pd.read_csv('features_dataset.csv')

# 2. Séparer les features (X) et les labels (y)
X = df.drop('label', axis=1)
y = df['label']

# 3. Séparer en données d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Créer le modèle Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)

# 5. Entraîner le modèle
model.fit(X_train, y_train)

# 6. Tester le modèle
y_pred = model.predict(X_test)

print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\n✅ Rapport de classification :\n", classification_report(y_test, y_pred))

# 7. Sauvegarder le modèle entraîné
joblib.dump(model, 'password_ai_model.pkl')
print("\n✅ Modèle sauvegardé sous 'password_ai_model.pkl'")
