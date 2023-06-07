<script lang="ts">
    import "@fontsource/montserrat"
    import { goto } from '$app/navigation';
    import { food } from '../export.js';

    let input = '';

    function onSubmit() {
        console.log(input);
        food.set(input);
        goto('/result');
    }
</script>

<main>
    <div class="all">
        <h1>Welcome to AI.llergen</h1>

        <form on:submit|preventDefault={onSubmit}>
            <div style="text-align:center">
                <label for="name" class="prompt">Enter your food product here</label>
                <br>
                <br>
                <input
                    class="form"
                    type="text"
                    bind:value={input}
                    required
                />
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
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        font-size: 3em;
        color: aliceblue;
    }

    .prompt {
        font-family: 'Montserrat', sans-serif;
        font-weight: 300;
        font-size: 18px;
        color: aliceblue;
    }

    .go {
    background-color: #007bff;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
    }

    .go:hover {
    background-color: #0056b3;
    }

    .go:active {
    background-color: #003980;
    }

    .form {
    padding: 10px;
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
</style>
