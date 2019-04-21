<template>
    <div class="">
        <div class="">
            <form>
                <div class="form-group">
                    <label>Email</label>
                    <input v-model="email" type="email" placeholder="Email">
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <input v-model="password" type="password" placeholder="Password">
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
<style lang="scss">

    form {
        width: 40%;
        margin: 0 auto;
    }

    input[type=text],
    input[type=email],
    input[type=password],
    select {
        width: 100%;
        padding: 12px 20px;
        margin: 8px 0;
        display: inline-block;
        border: 1px solid #ccc;
        border-radius: 1px;
        box-sizing: border-box;

        &:focus {
            border: 1px solid lightskyblue;
        }
    }

    button[type=submit] {
        width: 100%;
        background-color: lightblue;
        color: white;
        padding: 14px 20px;
        margin: 8px 0;
        border: none;
        border-radius: 1px;
        cursor: pointer;
        text-align: center;

        &:hover {
            background-color: lightskyblue;
        }
    }


</style>
