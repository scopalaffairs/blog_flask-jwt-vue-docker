<template>
    <div class="bg-grey-light">
        <Blog></Blog>
    </div>
</template>
<script>
    import Blog from "./views/Blog"

    export default {
        components: {
            Blog
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
