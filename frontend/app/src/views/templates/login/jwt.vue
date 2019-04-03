<template>
    <div>
        <p>JWT: {{jwt}}</p>
        <p>User ID: {{jwtSubject}}</p>
        <p>Issuer: {{jwtIssuer}}</p>
        <button @click.native="doSomethingWithJWT()">Do Something</button>
    </div>
</template>

<script>
    import {mapActions, mapGetters} from 'vuex';

    export default {
        computed: {
            ...mapGetters([
                'jwt',
                'jwtSubject',
                'jwtIssuer'
            ])
        },

        methods: {
            ...mapActions([
                'fetchJWT'
            ]),

            // The implementation here doesn't change at all!
            async doSomethingWithJWT() {
                const res = await fetch('http://localhost:5000/api/v1/blogposts/', {
                    method: 'POST',
                    headers: new Headers({
                        Authorization: 'Bearer: ${this.jwt}'
                    })
                });
                // Do stuff with res here.
            }
        },

        mounted() {
            this.fetchJWT({
                // #Security...
                username: 'username',
                password: 'password'
            });
        }
    }
</script>
