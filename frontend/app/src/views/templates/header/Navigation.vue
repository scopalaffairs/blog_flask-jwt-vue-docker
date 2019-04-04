<template>
    <div class="bg-grey-light">
        <div class="col-sm-6 offset-sm-3">
            <router-link to="/">Home</router-link>
            x
            <router-link to="/login">Login</router-link>
            x
            <router-link to="/blog">Blog</router-link>
            <router-view/>
        </div>
    </div>
</template>

<script>

    export default {
        name: 'Navigation',
        components: {}
    }
</script>
<style></style>
