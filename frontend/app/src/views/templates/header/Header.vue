<template>
    <div toggleable type="light" variant="light" class="mb-5">
        <div target="nav_text_collapse"></div>
        <div>Analytics</div>


        <div is-nav id="nav_text_collapse">
            <div>
                <div v-if="!isAuth">
                    <router-link to="/">Home</router-link>
                    x
                    <router-link to="/blog">Blog</router-link>
                    x
                    <router-link to="/login">Login</router-link>
                    <router-view/>
                </div>
                <div v-if="isAuth">
                    <router-link to="/">Home</router-link>
                    x
                    <router-link to="/blog">Blog</router-link>
                    x
                    <router-link to="/dashboard">Dashboard</router-link>
                    x
                    <router-link to="/logout">Logout</router-link>
                    <router-view/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex'

    export default {
        components: {},
        computed: {
            ...mapGetters('auth', {
                isAuth: 'isAuthenticated',
            })
        }
    }
</script>
