<template>
    <div class="bg-grey-light">
        <Navigation></Navigation>
        <h2>API URL is {{ apiUrl }}</h2>
    </div>
</template>
<script>

    import Navigation from './views/Navigation'

    export default {
        components: {Navigation},
        data() {
            return {
                apiUrl: process.env.VUE_APP_API_URL
            }
        }
    }
</script>

<style lang="sass">
    #app
        font-family: 'Avenir', Helvetica, Arial, sans-serif
        -webkit-font-smoothing: antialiased
        -moz-osx-font-smoothing: grayscale
        /*text-align: center*/
        /*color: #2c3e50*/




        label
            font-size: 10px

</style>
