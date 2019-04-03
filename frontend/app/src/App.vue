<template>
    <div class="bg-grey-light">
        <app-header/>
        <Navigation></Navigation>
    </div>
</template>
<script>
    import Header from '@/components/header/Header.vue'
    import Navigation from './views/Navigation'

    export default {
        created() {
            this.$store.dispatch('auth/autoLogin');
        },
        components: {
            AppHeader: Header,
            Navigation
        },
        data() {
            return {
                apiUrl: process.env.VUE_APP_API_URL
            }
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
