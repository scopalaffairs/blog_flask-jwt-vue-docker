<template>
    <div class="max-w-sm overflow-hidden shadow-lg">
        <div class="px-6 py-4">
            <div class="font-bold text-xl mb-2">
                <slot name="heading"></slot>
            </div>
            <p class="text-grey-darker text-base">
                <slot name="text-body"></slot>
            </p>
        </div>
        <div class="px-6 py-4">
            <slot name="tags"></slot>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Card"
    }
</script>

<style scoped>

</style>