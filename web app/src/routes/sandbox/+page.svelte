<script lang="ts">
    import axios from "axios";
    import { goto } from "$app/navigation";
    import { food, formValues } from "../../export.js";
    import { onMount } from "svelte";

    let isLoading = false;
    const containerCount = 6; // Number of containers
    let showContent = false;
    let containerFlags = Array(containerCount).fill(false);
    let activeContainerIndex = -1;
    let showError = false;
let errorMessage = "";

function displayError(message) {
    showError = true;
    errorMessage = message;

    // Hide the error message after a certain duration (e.g., 3 seconds)
    setTimeout(() => {
        showError = false;
        errorMessage = "";
    }, 3000); // Adjust the duration as desired
}

    function toggleContent() {
        showContent = !showContent;
    }

    function handleUnderstoodClick(index) {
        activeContainerIndex = index;
        containerFlags[index] = true;
    }

    async function onSubmit() {
        isLoading = true;
        let formData = $formValues;

        for (const key in formData) {
        if (key === "product" && formData[key] === "") {
            const errorMessage = "Please enter the name of the product.";
            displayError(errorMessage);
            isLoading = false;
            return;
        }

        if (key === "ingre" && formData[key] === "") {
            const errorMessage = "Please enter the main ingredient.";
            displayError(errorMessage);
            isLoading = false;
            return;
        }

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
        {#if !showContent}
            <p class="heading" on:click={toggleContent}>
                ai.llergen
                <span class="hover-text">click to start</span>
            </p>
        {/if}

        {#if showContent && activeContainerIndex === -1}
            <div class="expanded-content">
                <p>
                    <span class="aititle">ai.llergen</span> is your friendly food
                    allergen detector. This handy app can help you identify whether
                    your food product may or may not contain an allergen by prompting
                    you to input its main ingredient and other information. If information
                    is unknown, you may leave it blank.
                </p>

                <p>
                    <span class="disc">DISCLAIMER:</span> ai.llergen is for informational
                    purposes only. It is not a substitute for professional medical
                    advice. Please consult with a qualified healthcare professional
                    before making any dietary decisions or if you have any concerns
                    about food allergies.
                </p>

                <div class="button-container">
                    <button
                        class="understood-button"
                        on:click={() => handleUnderstoodClick(0)}
                    >
                        Understood
                    </button>
                </div>
            </div>
        {/if}

        {#if activeContainerIndex !== -1}
            {#if activeContainerIndex === 0}
                <!-- Container 1 -->
                <div class="expanded-content">
                    <label for="product-name" class="input-label"
                        >Product Name</label
                    >
                    <input type="text" bind:value={$formValues.product} required />
                    <div class="button-container">
                        <button
                            class="understood-button"
                            on:click={() => handleUnderstoodClick(1)}
                            >Next</button
                        >
                    </div>
                </div>
            {/if}

            {#if activeContainerIndex === 1}
                <!-- Container 2 -->
                <div class="container">
                    <!-- Container 2 content -->
                    <div class="button-container">
                        <button
                            class="understood-button"
                            on:click={() => handleUnderstoodClick(2)}
                        >
                            Next
                        </button>
                    </div>
                </div>
            {/if}

            <!-- Repeat the pattern for the remaining containers -->
            <!-- Container 3 -->
            <!-- Container 3 content -->
            <!-- Next button -->

            <!-- Container 4 -->
            <!-- Container 4 content -->
            <!-- Next button -->

            <!-- Container 5 -->
            <!-- Container 5 content -->
            <!-- Next button -->

            <!-- Container 6 -->
            <!-- Container 6 content -->
            <!-- Next button -->
        {/if}
    </div>

    <div class="error-message" class:showError={showError}>
        <p class="error-text">{errorMessage}</p>
    </div>

    {#if showContent}
        <footer class="footer">
            <p class="disclaimer">
                Disclaimer: This is for informational purposes only. Consult
                with a medical professional regarding food allergies.
            </p>
        </footer>
    {/if}
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

    .heading {
        font-family: "RB", sans-serif;
        font-size: 6em;
        color: #ebe3d3;
        letter-spacing: 3px;
        cursor: pointer;
        position: relative;
        opacity: 0;
        animation: fadeInHeading 0.3s ease-in-out forwards;
    }

    .heading:hover .hover-text {
        visibility: visible;
        opacity: 1;
    }

    @keyframes fadeInHeading {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    .expanded-content-container {
        display: flex;
        justify-content: center;
        margin-top: 10px; /* Adjust the margin as desired */
        opacity: 0;
        animation: fadeInContent 0.3s ease-in-out forwards;
    }

    @keyframes fadeInContent {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }
    .expanded-content {
        text-align: justify;
        width: 450px;
        padding: 16px;
        background-color: #ebe3d3;
        border-radius: 25px;
        font-family: "IntroCd", sans-serif;
        font-weight: 200;
        font-size: 16px;
        color: #3a3a3a;
    }

    .aititle {
        color: #db7c7c;
        font-weight: 350;
    }

    .disc {
        color: #d42434;
        font-weight: 550;
    }

    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }

    .understood-button {
        background-color: #3a3a3a;
        color: #ebe3d3;
        width: 110px;
        height: 35px;
        padding: 8px 16px;
        border: none;
        border-radius: 23px;
        font-family: "IntroCd", sans-serif;
        font-weight: 200;
        font-size: 14px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .understood-button:hover {
        background-color: #555555;
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
