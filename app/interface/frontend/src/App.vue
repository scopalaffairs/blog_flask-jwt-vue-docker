<template>
    <div class="bg-grey-light">
        <Navigation></Navigation>
        <div class="mx-auto px-4">
            <div class="min-h-screen bg-white p-8">
                <div class="max-w-xl mx-auto">
                    <router-view/>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import Navigation from "./views/templates/menu/Navigation"
    import Card from "./views/templates/molecules/Card.vue"

    export default {
        components: {Card, Navigation}
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
