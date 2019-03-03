<template>
    <div>
        <slot name="label"></slot><br>
        <button-group class="mt-2"
                      :name="name">

        </button-group>
    </div>
</template>

<script>
    import ButtonGroup from "../molecules/ButtonGroup";
    export default {
        name: "FilterByFeature",
        components: {ButtonGroup},
        props: ['name']
    }
</script>

<style scoped>

</style>