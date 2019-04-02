<template>
    <div class="w-4/5 block flex-grow">
        <div class="text-sm">
            <route-wrapper route="/">
                Home
            </route-wrapper>
            <route-wrapper route="/News">
                News
            </route-wrapper>
            <route-wrapper route="/Search">
                Search Regulators
            </route-wrapper>
            <route-wrapper route="/Documentation">
                Documentation
            </route-wrapper>
            <route-wrapper route="/Acknowledgements">
                Acknowledgements
            </route-wrapper>
        </div>
    </div>
</template>

<script>
        import RouteWrapper from "./RouteWrapper";

    export default {
        name: "MenuItems",
        components: {RouteWrapper},
        props:['route']
    }
</script>

<style scoped>

</style>