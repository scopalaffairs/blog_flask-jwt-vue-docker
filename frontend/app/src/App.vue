<template>
    <div class="bg-grey-light">
        <app-header/>
    </div>
</template>
<script>
    import Header from './views/templates/header/Header'

    export default {
        components: {
            AppHeader: Header,
        }
    }
</script>

<style lang="scss">
	@import './assets/scss/app.scss';

</style>
