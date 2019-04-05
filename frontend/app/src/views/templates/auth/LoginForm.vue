<template>
    <div class="row">
        <div class="col-md-6 offset-md-3 col-xl-4 offset-xl-4">
            <form>
                <div class="form-group">
                    <label>Email</label>
                    <input v-model="email" type="email" class="form-control" placeholder="Email">
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <input v-model="password" type="password" class="form-control" placeholder="Password">
                </div>
                <button type="submit" @click.prevent="login()" class="btn btn-primary">Login</button>
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
