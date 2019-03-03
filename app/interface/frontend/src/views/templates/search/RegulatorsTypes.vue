<template>
    <div>
        <div class="mb-3">
            <div class="inline-block relative w-50">
                <label>
                    Regulator types to show
                </label>
                <select placeholder="Select regulator types to show..."
                        class="block text-grey-dark text-sm appearance-none w-full bg-white border border-grey-light hover:border-grey px-2 py-2 pr-10 rounded-none shadow leading-tight focus:outline-none focus:shadow-outline">
                    <option>Really long option that will likely overlap the chevron</option>
                    <option>Option 2</option>
                    <option>Option 3</option>
                </select>
                <div class="pointer-events-none absolute pin-y pin-r flex items-center px-2 text-grey-darker">
                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/>
                    </svg>
                </div>
            </div>
        </div>
        <div>
            <div class="inline-block relative w-50">
                <label>
                    Regulators ({{ set }})
                </label>
                <select placeholder="Select regulator types to show..."
                        class="block text-grey-dark text-sm appearance-none w-full bg-white border border-grey-light hover:border-grey px-2 py-2 pr-10 rounded-none shadow leading-tight focus:outline-none focus:shadow-outline">
                    <option>Really long option that will likely overlap the chevron</option>
                    <option>Option 2</option>
                    <option>Option 3</option>
                </select>
                <div class="pointer-events-none absolute pin-y pin-r flex items-center px-2 text-grey-darker">
                    <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                        <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/>
                    </svg>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "RegulatorsTypes",
        props: ['set']
    }
</script>

<style scoped>

</style>