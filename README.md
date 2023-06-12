# AI for AI: Utilizing Artificial Intelligence for Allergen Identification in Food
by Juan Antonio Bonuan, Dean Ramirez, Julia Sabado & Andrei Tiangco
<br>
CS 180 Artificial Intelligence Course
<br>
Department of Computer Science
<br>
University of the Philippines Diliman

This project is done by  aims to develop an AI model for allergen detection in food products using a multi-label classification approach. It will utilize separate Random Forest classifiers for each allergen class, treating them as independent binary classification tasks. This project addresses the limitations of traditional allergen detection methods, ensuring consumer safety and improving food allergen detection accuracy and food quality control processes. Using the ["Food Ingredients & Allergens"](https://www.kaggle.com/datasets/uom190346a/food-ingredients-and-allergens) dataset from Kaggle, the model will be trained to predict the presence of allergenic ingredients in different food products. The model will learn how to recognize patterns and associations between ingredients and allergens. The developed model will then be integrated into a web application for user-friendly allergen detection, where people with allergies can make informed decisions about the food they buy and consume. This project has the potential to benefit food manufacturers, the food service industry, regulatory bodies, and people with allergies, ultimately improving food safety and promoting informed food choices.

## Project Code
The project code Jupyter Notebook can be found inside the `project code` folder of this [repository](https://github.com/splasherzz/food-allergen-detector). In there, we described each step of creating this AI model (from data collection up to data results).

## Web App: ai.llergen

We integrated the trained AI model into a web app named **ai.llergen**, built with SvelteKit (frontend) and Python (backend). We've deployed the web app for easier accessibility by all, which you can access [here](https://food-allergen-detector.vercel.app/).

To use the app locally, clone our public Github repository named [food-allergen-detector](https://github.com/splasherzz/food-allergen-detector). Make sure you're in the `web app` directory then run the following command to install the needed dependencies: `npm install`. Afterwards, run the command `npm run dev` and launch the web app using the `localhost` link provided. 

Once run, you will be prompted to enter your food product's name and main ingredient. The other fields are only optional as not all food product labels might include its specific sweetener, fat/oil, seasoning, and/or allergens. Press the `Go!` button to let the AI model predict whether your entered food product has allergens. Afterwards, the name of your food product and the prediction will be displayed. It will be either `Contains` or `Does not contain`. You can then press `Back` to enter another food product to check.
