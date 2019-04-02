<template>
    <div class="home">
        <blog-list></blog-list>
    </div>
</template>

<script>
    // @ is an alias to /src
    import BlogList from './templates/blog/blog-list'

    export default {
        name: 'blog',
        components: {
            BlogList,
        }
    }
</script>
<style></style>
