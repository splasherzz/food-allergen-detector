<script lang="ts">
    import "@fontsource/montserrat"
    import { goto } from '$app/navigation';
    import { food } from '../../export.js';
    import { onMount } from 'svelte';

    let input;

    function goBack() {
        goto('/');
    }

    onMount(() => {
        food.subscribe(value => {
            input = value;
        });
    });
</script>

<main>
    <div class="all">
        <h1 class="caption">Your food: {$food}</h1>
        
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