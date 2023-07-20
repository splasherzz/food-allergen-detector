<script lang="ts">
    import { goto } from "$app/navigation";
    import { food, formValues } from "../../export.js";
    import { onMount } from "svelte";

    let product;
    let resultSrc;
    let resultCont;

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
        $formValues.pred = "may not contain allergens";
        resultSrc = "nogen.png";
        resultCont = "result-none";
    } else {
        $formValues.pred = "may contain allergens";
        resultSrc = "allergen.png";
        resultCont = "result-contains";
    }
</script>

<main>
    <div class="container floating">
        <button class="home-icon" on:click={goBack}>
            <i class="fas fa-home" />
        </button>

        <h1 class="caption">
            <span class="food-name">{$food}</span><br />
            <span class="pred">{$formValues.pred}</span>
        </h1>

        <img src={resultSrc} alt="result pic" class={resultCont} />
    </div>

    <footer class="footer">
        <p class="disclaimer">
            Disclaimer: This is for informational purposes only. Consult with a
            medical professional regarding food allergies.&nbsp;<span
                class="copy">&copy;</span
            >&nbsp;JADE
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
        border-radius: 10px;
        padding: 16px;
        width: 700px;
        height: 500px;
        margin: 0 auto;
        position: relative;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }

    .home-icon {
        position: absolute;
        top: 17px;
        left: 17px;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 24px;
        height: 24px;
        cursor: pointer;
        color: #3a3a3a;
        text-decoration: none;
        font-size: 1.6em;
        background-color: transparent;
        border: none;
    }

    .home-icon:hover {
        color: #555555;
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
        font-weight: 450;
    }

    .pred {
        color: #db7c7c;
        font-weight: 600;
    }

    .result-contains {
        width: 350px;
        height: auto;
        margin-bottom: -12px;
        filter: contrast(80%) saturate(75%);
    }

    .result-none {
        width: 250px;
        height: auto;
        margin-bottom: -31px;
        filter: contrast(80%) saturate(75%);
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

    .copy {
        font-family: "Courier New";
    }
</style>
