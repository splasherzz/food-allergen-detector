<script lang="ts">
    import "@fontsource/montserrat";
    import axios from "axios";
    import { goto } from "$app/navigation";
    import { food, formValues } from "../../export.js";

    let isLoading = false;

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
        <p class="heading">
            ai.llergen
        </p>
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

    .title {
        
        
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

    .heading {
        font-family: "RB", sans-serif;
        font-size: 5em;
        color: #ebe3d3;
        letter-spacing: 3px;
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
