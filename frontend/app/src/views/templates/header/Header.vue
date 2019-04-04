<template>
    <div toggleable type="light" variant="light" class="mb-5">
        <div target="nav_text_collapse"></div>
        <div>Analytics</div>


        <div is-nav id="nav_text_collapse">
            <div>
                <div v-if="!isAuth">
                    <Navigation></Navigation>
                </div>
                <div v-if="isAuth">
                    <NavigationAdmin></NavigationAdmin>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex'
    import Navigation from './Navigation'
    import NavigationAdmin from './NavigationAdmin'

    export default {
        components: {
            Navigation,
            NavigationAdmin
        },
        computed: {
            ...mapGetters('auth', {
                isAuth: 'isAuthenticated',
            })
        }
    }
</script>
