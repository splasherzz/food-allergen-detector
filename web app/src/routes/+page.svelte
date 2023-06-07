<script lang="ts">
    import "@fontsource/montserrat"
    import { goto } from '$app/navigation'

    function onSubmit(e) {
        const formData = new FormData(e.target);

        const data: any = {};
		for (let field of formData) {
			const [key, value] = field;
			data[key] = value;

        }
            console.log(data);
    }
</script>
    
<main>
    <div class="all">
        <h1 >Welcome to AI.llergen</h1>

    <form on:submit={onSubmit}>
        <div style="text-align:center">
            <label for="name" class="prompt">Enter your food product here</label>
            <br>
            <br>
            <input 
                class="form" 
                type="text" 
                name="food" 
                value=""
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