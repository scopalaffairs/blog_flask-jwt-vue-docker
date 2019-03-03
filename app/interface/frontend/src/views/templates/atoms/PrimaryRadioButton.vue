<template>
    <label class="btn-pill--wrapper">
        <input type="radio"
               :name="name"
               :value="value">
        <span class="checkmark"></span>
        <slot></slot>
    </label>
</template>

<script>
    export default {
        name: "PrimaryRadioButton",
        props: ['value', 'name']
    }
</script>

<style scoped>

</style>