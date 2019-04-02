<template>
    <div class="bg-grey-light">
        <Navigation></Navigation>
    </div>
</template>
<script>

    import Navigation from './views/Navigation'
    export default {
        components: {Navigation}
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
