import pandas as pd
import random
import string

# Charger RockYou.txt
def load_compromised_passwords(file_path, max_passwords=50000):
    passwords = []
    with open(file_path, 'r', encoding='latin-1') as file:
        for i, line in enumerate(file):
            if i >= max_passwords:
                break
            password = line.strip()
            if password:  # Ignore les lignes vides
                passwords.append(password)
    return passwords

# Générer des mots de passe sûrs (classe saine)
def generate_secure_passwords(n):
    secure_passwords = []
    for _ in range(n):
        pwd = ''.join(random.choices(
            string.ascii_letters + string.digits + string.punctuation,
            k=random.randint(10, 16)
        ))
        secure_passwords.append(pwd)
    return secure_passwords

# Sauvegarder dataset
def create_dataset(rockyou_path, output_path):
    compromised = load_compromised_passwords(rockyou_path)
    secure = generate_secure_passwords(len(compromised))

    data = {
        'password': compromised + secure,
        'label': [1] * len(compromised) + [0] * len(secure)
    }

    df = pd.DataFrame(data)
    df = df.sample(frac=1).reset_index(drop=True)  # Mélanger les données
    df.to_csv(output_path, index=False)
    print(f"✅ Dataset généré avec succès : {output_path}")

# Lancer préparation
if __name__ == "__main__":
    create_dataset('rockyou.txt', 'dataset.csv')
