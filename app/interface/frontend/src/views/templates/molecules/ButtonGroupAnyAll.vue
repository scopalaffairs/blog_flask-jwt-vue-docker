<template>
    <div>
        <primary-radio-button-pill-bar :name="name" value="any">any</primary-radio-button-pill-bar>
        <primary-radio-button-pill-bar :name="name" value="any">all</primary-radio-button-pill-bar>
    </div>
</template>

<script>
    import PrimaryRadioButtonPillBar from "../atoms/PrimaryRadioButtonPillBar";

    import '../../../assets/css/tailwind.css'


    export default {
        name: "ButtonGroup",
        components: {PrimaryRadioButtonPillBar},
        props: {
            'name': String
        }
    }
</script>

<style>


</style>