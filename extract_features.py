import pandas as pd
import string

# Fonction pour extraire les features
def extract_features(password):
    features = {
        'length': len(password),
        'digits': sum(c.isdigit() for c in password),
        'lowercase': sum(c.islower() for c in password),
        'uppercase': sum(c.isupper() for c in password),
        'symbols': sum(c in string.punctuation for c in password),
        'sequential_letters': has_sequential_letters(password),
        'sequential_digits': has_sequential_digits(password),
    }
    return features

def has_sequential_letters(password):
    sequence = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(sequence) - 2):
        if sequence[i:i+3] in password.lower():
            return 1
    return 0

def has_sequential_digits(password):
    sequence = "0123456789"
    for i in range(len(sequence) - 2):
        if sequence[i:i+3] in password:
            return 1
    return 0

# Lire le dataset et extraire les features
def process_dataset(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    feature_list = []

    for pwd in df['password']:
        feature_list.append(extract_features(pwd))

    features_df = pd.DataFrame(feature_list)
    features_df['label'] = df['label']
    
    features_df.to_csv(output_csv, index=False)
    print(f"✅ Features extraites dans : {output_csv}")

if __name__ == "__main__":
    process_dataset('dataset.csv', 'features_dataset.csv')
