<template>
    <div>
        <div class="pb-1">
            <label>
                Define set operations
            </label>
        </div>
        <div class="mb-5">
            <primary-radio-button-pill-bar name="set_op_group" value="and">AND</primary-radio-button-pill-bar>
            <primary-radio-button-pill-bar name="set_op_group" value="or">OR</primary-radio-button-pill-bar>
            <primary-radio-button-pill-bar name="set_op_group" value="xor">XOR</primary-radio-button-pill-bar>
            <primary-radio-button-pill-bar name="set_op_group" value="not">NOT</primary-radio-button-pill-bar>
        </div>

        <p class=""
           id="readable-set-operation"
           data-bind="text: 'Return binding sites of set A and set B being ' + readableSetOperation()">
            readableSetOperation()
        </p>
    </div>
</template>

<script>
    import PrimaryRadioButtonPillBar from "../atoms/PrimaryRadioButtonPillBar";

    export default {
        components: {PrimaryRadioButtonPillBar},
        name: "SetOperations",
        props: ['name', 'value']
    }
</script>

<style scoped>

</style>