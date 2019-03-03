<template>
    <div class="home">
        <primary-button color="bg-blue-darker" hover="bg-sealife">Clear</primary-button>
        <colors></colors>
    </div>
</template>

<script>
    // @ is an alias to /src
    import PrimaryButton from './templates/atoms/PrimaryButton'
    import Colors from '../views/templates/atoms/Colors'

    export default {
        name: 'home',
        components: {
            PrimaryButton,
            Colors
        }
    }
</script>
<style></style>
