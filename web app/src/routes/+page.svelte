<script lang="ts">
  import "@fontsource/montserrat";
  import axios from "axios";
  import { goto } from "$app/navigation";
  import { food, formValues } from "../export.js";

  async function onSubmit() {
    let formData = $formValues;

    for (const key in formData) {
      if (formData[key] === "") {
        formData[key] = "None";
      }
    }

    console.log(formData);
    const res = await axios.post(
      "https://splasherz.pythonanywhere.com/predict",
      {
        food_product: $formValues.product,
        main_ingredient: $formValues.ingre,
        sweetener: $formValues.sweet,
        fat_oil: $formValues.fat,
        seasoning: $formValues.seas,
      },
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );
    $formValues.pred = res.data
    console.log($formValues.pred);
    // insert logic for backend connection here

    food.set(formData.product);
    goto("/result");
  }
</script>

<main>
  <div class="all">
    <h1>Welcome to AI.llergen</h1>
    <label for="name" class="prompt" style="margin-bottom: 20px;"
      >Enter your food product details here:</label
    >

    <form on:submit|preventDefault={onSubmit}>
      <div class="form-group">
        <label for="product" class="textlabel">Name of Food</label>
        <input
          class="form"
          type="text"
          bind:value={$formValues.product}
          required
        />
      </div>
      <div class="form-group">
        <label for="ingre" class="textlabel">Main Ingredient</label>
        <input
          class="form"
          type="text"
          bind:value={$formValues.ingre}
          required
        />
      </div>
      <div class="form-group">
        <label for="sweet" class="textlabel">Sweetener</label>
        <input class="form" type="text" bind:value={$formValues.sweet} />
      </div>
      <div class="form-group">
        <label for="fat" class="textlabel">Fat/Oil</label>
        <input class="form" type="text" bind:value={$formValues.fat} />
      </div>
      <div class="form-group">
        <label for="seas" class="textlabel">Seasoning</label>
        <input class="form" type="text" bind:value={$formValues.seas} />
      </div>
      <div class="form-group">
        <label for="aller" class="textlabel">Allergens</label>
        <input class="form" type="text" bind:value={$formValues.aller} />
      </div>
      <div style="text-align: center;">
        <button type="submit" class="go">Go!</button>
      </div>
    </form>
  </div>
</main>

<style>
  :global(body) {
    background: rgb(1, 31, 75);
  }

  .all {
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    justify-content: center;
    align-items: center;
    height: 93vh;
  }

  h1 {
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: "Montserrat", sans-serif;
    font-weight: 700;
    font-size: 3em;
    color: aliceblue;
  }

  .prompt {
    font-family: "Montserrat", sans-serif;
    font-weight: 300;
    font-size: 22px;
    color: aliceblue;
  }

  .textlabel {
    font-family: "Montserrat", sans-serif;
    font-weight: 300;
    font-size: 18px;
    color: aliceblue;
    margin-right: 10px;
    width: 160px;
  }

  .form-group {
    display: flex;
    align-items: center;
    margin-bottom: 12px;
  }

  .form {
    flex: 1;
    padding: 6px;
    border: 1px solid #007bff;
    border-radius: 4px;
    font-size: 16px;
    color: #333;
    outline: none;
  }

  .form:focus {
    border-color: #0056b3;
    box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.25);
  }

  .go {
    background-color: #007bff;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
    margin-top: 7px;
  }

  .go:hover {
    background-color: #0056b3;
  }

  .go:active {
    background-color: #003980;
  }
</style>
