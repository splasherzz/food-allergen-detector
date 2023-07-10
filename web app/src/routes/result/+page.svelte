<script lang="ts">
    import { goto } from "$app/navigation";
    import { food, formValues } from "../../export.js";
    import activeContainerIndex  from "../+page.svelte";
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
        goto("/", { state: { activeContainerIndex: 2 } });
    }

    onMount(() => {
        food.subscribe((value) => {
            product = value;
        });
    });
</script>

<main>
    <div class="all">
        <h1 class="caption">
            {$food}:&nbsp;<span class="pred">{$formValues.pred}</span>
        </h1>

        <div>
            <button type="button" class="back" on:click={goBack}>Back</button>
        </div>
    </div>
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

    .all {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100%;
    }

    .caption {
        font-family: "IntroCd", sans-serif;
        font-weight: 200;
        font-size: 3em;
        color: #ebe3d3;
        margin-bottom: 20px;
    }

    .pred {
        color: #ffa552;
    }

    .back {
        background-color: #3a3a3a;
        color: #ebe3d3;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
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
</style>
