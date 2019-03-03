<template>
    <!-- Extracting component classes: -->
    <div class="colors">
        <div class="flex flex-wrap m-8 text-xs border-b-2">
            <div v-for="(key, value) in colors" :key="key" :value="value" class="">
                {{ value }}
                <div :class="'rounded shadow h-48 w-24 bg-' + value">
                </div>
                <p class="text-xs text-grey mt-2 uppercase">{{ key }}</p>
            </div>
        </div>
    </div>

</template>

<script>
    import '../../../assets/css/tailwind.css'
    import TailwindConfig from "../../../../tailwind.js";


    export default {
        name: "Button",
        data: function () {
            return {
                colors: TailwindConfig.chosenColors
            }
        }
    }
</script>

<style scoped>


</style>