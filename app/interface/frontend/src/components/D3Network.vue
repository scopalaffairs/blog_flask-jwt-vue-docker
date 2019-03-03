<template>
    <d3-network :net-nodes="nodes" :net-links="links" :options="options"/>
</template>

<script>
    import D3Network from 'vue-d3-network'

    components: {
        D3Network
    }

</script>

<style src="vue-d3-network/dist/vue-d3-network.css" scoped>

</style>
