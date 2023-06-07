<script lang="ts">
    import "@fontsource/montserrat"
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
        <h1 >Hi</h1>

    
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