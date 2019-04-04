<template>
    <div class="row">
        <div class="col-md-6 offset-md-3 col-xl-4 offset-xl-4">
            <form>
                <button type="submit" @click.prevent="logout()" class="btn btn-primary">Logout</button>
            </form>
        </div>
    </div>
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
                auth: 'auth/logout'
            }),

            logout() {
                let authData = {
                    email: this.email,
                    password: this.password,
                }
                this.$store.dispatch('auth/logout', authData).then(() => {
                    this.$router.push('/');
                });
            }
        }
    }
</script>
