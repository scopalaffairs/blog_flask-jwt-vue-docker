<template>
    <div class="bg-grey-light">
        <app-header/>
        <Navigation></Navigation>
    </div>
</template>
<script>
    import Header from './views/templates/header/Header'
    import Navigation from './views/Navigation'

    export default {
        components: {
            AppHeader: Header,
            Navigation
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
