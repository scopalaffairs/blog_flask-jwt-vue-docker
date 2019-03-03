<template>
    <nav class="flex items-center justify-between flex-wrap bg-blue-darkest p-6">
        <menu-logo></menu-logo>
        <!--<menu-button></menu-button>-->
        <menu-items></menu-items>
    </nav>
</template>

<script>
    import MenuButton from "./MenuButton";
    import MenuItems from "./MenuItems";
    import MenuLogo from "./MenuLogo";

    export default {
        name: "Navigation",
        components: {MenuLogo, MenuItems, MenuButton},
    }
</script>

<style lang="sass" scoped>
</style>