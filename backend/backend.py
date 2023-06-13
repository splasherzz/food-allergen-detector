from flask import Flask, request
from flask_cors import CORS
import pandas as pd
import pickle

app = Flask(__name__)
CORS(app)
clf = pickle.load(open('model.pkl', 'rb'))

# Load the dataset
aug_food = pd.read_csv('food_allergen_dataset.csv')
aug_food['Prediction'] = aug_food['Prediction'].map({'Contains': 1, 'Does not contain': 0})

# Mirror dummy encoding to later reshape the input vector based on the dummy columns
aug_allerg = aug_food['Allergens'].str.replace(' ', '').str.get_dummies(',')
aug_allerg = aug_allerg.add_prefix('Allergens_')
aug_season = aug_food['Seasoning'].str.replace(' ', '').str.get_dummies(',')
aug_season = aug_season.add_prefix('Seasoning_')
aug_food.drop(['Seasoning','Allergens'], axis=1, inplace=True)
aug_food = pd.get_dummies(aug_food, drop_first=True)
aug_food = pd.concat([aug_food, aug_season, aug_allerg], axis=1)
aug_food = aug_food[[col for col in aug_food.columns if col != 'Prediction'] + ['Prediction']]

@app.route('/')
def home():
    return 'hello world'

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    food_product = request.form['food_product']
    main_ingredient = request.form['main_ingredient']
    sweetener = request.form['sweetener']
    fat_oil = request.form['fat_oil']
    seasoning = request.form['seasoning']
    allergens = request.form['allergens']

    input_data = []
    cols = {"Food Product": food_product,
            "Main Ingredient": main_ingredient,
            "Sweetener": sweetener,
            "Fat/Oil": fat_oil,
            "Seasoning": seasoning,
            "Allergens": allergens}

    for col in aug_food.columns:
        for label in cols:
            if col.startswith(label):
                if col == f"{label}_{cols[label]}":
                    input_data.append(1)
                else:
                    input_data.append(0)
                break

    prediction = clf.predict([input_data])
    prediction_label = 'Contains' if prediction[0] == 1 else 'Does not contain'
    return prediction_label

if __name__ == '__main__':
    app.run(debug=True)