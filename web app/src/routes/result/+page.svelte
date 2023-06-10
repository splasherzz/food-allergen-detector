<script lang="ts">
    import "@fontsource/montserrat";
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
    :global(body) {
        background: rgb(1, 31, 75);
    }

    .all {
        display: flex;
        flex-direction: column;
        box-sizing: border-box;
        justify-content: center;
        align-items: center;
        height: 95vh;
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

    .pred {
        color: #ffa552;
    }

    .back {
        background-color: #007bff;
        color: #fff;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        font-size: 16px;
        cursor: pointer;
        width: 90px;
    }

    .back:hover {
        background-color: #0056b3;
    }

    .back:active {
        background-color: #003980;
    }
</style>
