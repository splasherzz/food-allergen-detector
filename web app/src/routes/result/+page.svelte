<script lang="ts">
    import { goto } from "$app/navigation";
    import { food, formValues } from "../../export.js";
    import { onMount } from "svelte";

    let product;

    function goBack() {
        $formValues.product = "";
        $formValues.ingre = "";
        $formValues.sweet = "";
        $formValues.fat = "";
        $formValues.seas = "";
        $formValues.aller = "";
        $formValues.pred = "";
        goto("/");
    }

    onMount(() => {
        food.subscribe((value) => {
            product = value;
        });
    });

    $: if ($formValues.pred === "Does not contain") {
        $formValues.pred = "May not contain allergens";
    } else {
        $formValues.pred = "May contain allergens";
    }
</script>

<main>
    <div class="container">
        <h1 class="caption">
            <span class="food-name">{$food}</span><br />
            <span class="pred">{$formValues.pred}</span>
        </h1>

        <div class="button-container">
            <button type="button" class="back" on:click={goBack}>Back</button>
        </div>
    </div>

    <footer class="footer">
        <p class="disclaimer">
            Disclaimer: This is for informational purposes only. Consult with a
            medical professional regarding food allergies.
        </p>
    </footer>
</main>

<style>
    @font-face {
        font-family: "IntroCd";
        src: url("/fonts/IntroCd-Trial-Rg.otf") format("opentype");
    }

    @font-face {
        font-family: "RB";
        src: url("/fonts/RetroBoldy-Regular.otf") format("opentype");
    }

    :global(html, body) {
        height: 98%;
        background-color: #d35354;
    }

    main {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
    }

    .container {
        display: flex;
        text-align: center;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background-color: #ebe3d3;
        border-radius: 25px;
        padding: 16px;
        width: 450px;
        margin: 0 auto;
    }

    .caption {
        font-family: "IntroCd", sans-serif;
        font-weight: 200;
        font-size: 2.5em;
        color: #3a3a3a;
        margin-bottom: 20px;
        text-align: center;
    }

    .food-name {
        color: #3a3a3a;
    }

    .pred {
        color: #db7c7c;
    }

    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }

    .back {
        background-color: #3a3a3a;
        color: #ebe3d3;
        padding: 10px 20px;
        border: none;
        border-radius: 23px;
        font-size: 16px;
        cursor: pointer;
        width: 90px;
        transition: background-color 0.3s ease;
    }

    .back:hover {
        background-color: #555555;
    }

    .back:active {
        background-color: #3a3a3a;
    }

    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        padding: 10px;
        text-align: center;
    }

    .disclaimer {
        font-family: "IntroCd", sans-serif;
        font-size: 12px;
        color: #ebe3d3;
    }
</style>
