<template>
    <div>
        <slot name="label"></slot>
        <div class="mt-2">
            <primary-radio-button-pill-bar :name="name" value="any">&nbsp;any&nbsp;</primary-radio-button-pill-bar>
            <primary-radio-button-pill-bar :name="name" value="all">&nbsp;all&nbsp;</primary-radio-button-pill-bar>
        </div>
    </div>
</template>

<script>
    import PrimaryRadioButtonPillBar from "../atoms/PrimaryRadioButtonPillBar";

    export default {
        name: "RegulatorsMatch",
        components: {PrimaryRadioButtonPillBar},
        props: ['name']
    }
</script>

<style scoped>

</style>