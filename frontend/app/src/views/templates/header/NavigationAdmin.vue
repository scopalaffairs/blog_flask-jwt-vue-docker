<template>
    <div class="bg-grey-light">
        <div class="col-sm-6 offset-sm-3">
            <router-link to="/">Home</router-link>
            x
            <router-link to="/logout">Logout</router-link>
            x
            <router-link to="/blog">Blog</router-link>
            <router-view/>
        </div>
        <Dashboard></Dashboard>
    </div>
</template>

<script>

    import Dashboard from "../admin/Dashboard";

    export default {
        name: 'Navigation',
        components: {Dashboard}
    }
</script>
<style></style>
