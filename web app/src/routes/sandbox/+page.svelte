<script lang="ts">
    import "@fontsource/montserrat";
    import axios from "axios";
    import { goto } from "$app/navigation";
    import { food, formValues } from "../../export.js";
    import { onMount } from "svelte";

    let isLoading = false;
    let showContent = false;

    function toggleContent() {
        showContent = !showContent;
    }
    
    async function onSubmit() {
        isLoading = true;
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
                allergens: $formValues.aller,
            },
            {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            }
        );

        $formValues.pred = res.data;
        console.log($formValues.pred);
        isLoading = false;
        food.set(formData.product);
        goto("/result");
    }
</script>

<main>
    <div class="title">
        <p class="heading" on:click={toggleContent}>
            ai.llergen
            {#if !showContent}
            <span class="hover-text">click to start</span>
            {/if}
        </p>
        {#if showContent}
            <div class="expanded-content">
                <!-- Add your expandable content here -->
                <p>ai.llergen is your friendly food allergen detector. this
                    handy app can help you identify whether your food product
                    may or may not contain an allergen by prompting you to input
                    its main ingredient and other information. if information is
                    unknown, you may leave it blank.</p>
            </div>
        {/if}
    </div>
</main>




<style>
    @font-face {
        font-family: "RestoraExtraLight";
        src: url("/fonts/RestoraExtraLight.otf") format("opentype");
    }

    @font-face {
        font-family: "IntroCdReg";
        src: url("/fonts/IntroCd-Trial-Rg.otf") format("opentype");
    }

    @font-face {
        font-family: "Magic";
        src: url("/fonts/Magic Retro.ttf") format("truetype");
    }

    @font-face {
        font-family: "IntroCd";
        src: url("/fonts/IntroCd-Trial-Rg.otf") format("opentype");
    }

    @font-face {
        font-family: "BreakLove";
        src: url("/fonts/Break_Love_Font[1].ttf") format("truetype");
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

    .hover-text {
        position: absolute;
        top: 100%;
        left: 50%;
        transform: translateX(-50%);
        background-color: #ebe3d3;
        padding: 4px 8px;
        border-radius: 4px;
        font-family: "IntroCd", sans-serif;
        font-weight: 200;
        font-size: 12px;
        color: #3a3a3a;
        visibility: hidden;
        opacity: 0;
        transition: visibility 0s, opacity 0.3s ease-in-out;
    }

    .title {
        margin-bottom: 10px;
    }
    .heading {
        font-family: "RB", sans-serif;
        font-size: 6em;
        color: #ebe3d3;
        letter-spacing: 3px;
        cursor: pointer;
        position: relative;
    }

    .heading:hover .hover-text {
        visibility: visible;
        opacity: 1;
    }

    .expanded-content {
        text-align: justify;
        width: 450px;
        margin-top: 10px;
        padding: 16px;
        background-color: #ebe3d3;
        border-radius: 25px;
        font-family: "IntroCd", sans-serif;
        font-weight: 200;
        font-size: 16px;
        color: #3a3a3a;
    }

    .container1 {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background-color: #db7c7c;
        padding: 20px;
        border-radius: 25px;
    }

    .ai {
        color: #c1ece4;
    }

    .prompt {
        font-family: "IntroCd", sans-serif;
        font-weight: 200;
        font-size: 22px;
        color: aliceblue;
    }

    .prompt2 {
        font-family: "IntroCd", sans-serif;
        font-weight: 200;
        font-size: 16px;
        color: aliceblue;
    }
</style>
