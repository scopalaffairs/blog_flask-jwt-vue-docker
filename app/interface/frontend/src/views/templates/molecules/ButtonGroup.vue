<template>
    <div>
        <primary-radio-button-pill-bar :name="name" value="any">&nbsp;any&nbsp;</primary-radio-button-pill-bar>
        <primary-radio-button-pill-bar :name="name" value="CDS">&nbsp;CDS&nbsp;</primary-radio-button-pill-bar>
        <primary-radio-button-pill-bar :name="name" value="5prime">&nbsp;5' UTR&nbsp;</primary-radio-button-pill-bar>
        <primary-radio-button-pill-bar :name="name" value="3prime">&nbsp;3' UTR&nbsp;</primary-radio-button-pill-bar>
        <primary-radio-button-pill-bar :name="name" value="intron">&nbsp;intron&nbsp;</primary-radio-button-pill-bar>
        <primary-radio-button-pill-bar :name="name" value="intergenic">&nbsp;intergenic&nbsp;</primary-radio-button-pill-bar>
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