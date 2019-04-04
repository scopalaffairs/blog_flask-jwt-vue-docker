<template>
    <div class="bg-grey-light">
        <app-header/>
    </div>
</template>
<script>
    import Header from './views/templates/header/Header'

    export default {
        components: {
            AppHeader: Header,
        }
    }
</script>

<style lang="scss">
	@import './assets/css/_app.css';

	#app {
		font-family: "Avenir", Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		color: #2c3e50;
	}

</style>
