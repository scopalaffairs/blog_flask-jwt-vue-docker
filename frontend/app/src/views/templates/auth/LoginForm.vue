<template>
    <form>
        <div class="form-group">
            <label>Email</label>
            <input v-model="email" type="email" placeholder="Email">
        </div>
        <div class="form-group">
            <label>Password</label>
            <input v-model="password" type="password" placeholder="Password">
        </div>
        <button type="submit" @click.prevent="login()" class="btn btn--primary">Login</button>
    </form>
</template>
 

<script>
    import {mapActions, mapGetters} from 'vuex'

    export default {
        data() {
            return {
                email: '',
                password: '',
            }
        },
        computed: {
            ...mapGetters({
                //
            })
        },
        methods: {
            ...mapActions({
                auth: 'auth/login'
            }),

            login() {
                let authData = {
                    email: this.email,
                    password: this.password,
                }
                this.$store.dispatch('auth/login', authData).then(() => {
                });
            }
        }
    }
</script>
<style lang="scss">
    @import '@/assets/scss/components/forms.scss'



</style>
