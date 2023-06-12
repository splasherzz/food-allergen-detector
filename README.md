# AI for AI: Utilizing Artificial Intelligence for Allergen Identification in Food

This project aims to develop an AI model for allergen detection in food products using a multi-label classification approach. It will utilize separate Random Forest classifiers for each allergen class, treating them as independent binary classification tasks. This project addresses the limitations of traditional allergen detection methods, ensuring consumer safety and improving food allergen detection accuracy and food quality control processes. Using the "Food Ingredients and Allergens" dataset from Kaggle, the model will be trained to predict the presence of allergenic ingredients in different food products. The model will learn how to recognize patterns and associations between ingredients and allergens. The developed model will then be integrated into a web application for user-friendly allergen detection, where people with allergies can make informed decisions about the food they buy and consume. This project has the potential to benefit food manufacturers, the food service industry, regulatory bodies, and people with allergies, ultimately improving food safety and promoting informed food choices.

## Data Collection
We obtained the 2023 Kaggle dataset titled ["Food Ingredients & Allergens"](https://www.kaggle.com/datasets/uom190346a/food-ingredients-and-allergens) by Laksika Tharmalingam. We augmented data by manually adding 92 entries to the dataset, adding various food products and their allergen labels that we got from Google. The augmented dataset is then used to train and test our AI model for food allergen detection.

## Data Preprocessing
Before augmenting the dataset, we cleaned the original dataset by doing the following:

- did type formatting by changing all of the columns' data types from `object` to `category`
- checked for null values using `.isna()`, dropping the single entry containing a null value 
- checked for and dropped duplicates using `.drop_duplicates()`, keeping only the first instance of the food

We then added 92 more entries such that the dataset now has 400 entries with a total of 7 columns. After augmenting the dataset, we did categorical data encoding by doing the following:

- mapped the qualitative predictions into binary values `0` for `"Does Not Contain"` and `1` for `"Contains"`
- converted the rest of the categorical features into binary representations via one-hot encoding

One-hot encoding transforms each unique category in a variable to a separate binary feature. This was done as it allows us to represent categorical variables as numerical inputs, which is needed for our chosen model—multi-label classification.

## AI.llergen

The deployed web app, named AI.llergen, lets the user input the food product and its details (such as main ingredient, sweetener, allergen, etc) in order to find out whether the food product contains allergens or not. The AI model we trained will be used for predicting the presence of allergens.
