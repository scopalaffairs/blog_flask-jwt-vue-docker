<template>
    <router-link
            :to="route"
            class="inline-flex lg:mt-0 sm:mt-0 text-blue-lighter hover:text-white mr-4">
        <slot></slot>
    </router-link>
</template>

<script>
    export default {
        name: "RouterLinks",
        props: ['route']
    }
</script>

<style scoped>

</style>