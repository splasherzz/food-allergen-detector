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
                <button type="submit">Go!</button>
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
        height: 95vh;
    }

    h1 {
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        color: aliceblue;
    }

    .prompt {
        font-family: 'Montserrat', sans-serif;
        font-weight: 300;
        color: aliceblue;
    }
</style>