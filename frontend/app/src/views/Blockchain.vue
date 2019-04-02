<template>
    <div class="blockchain">
        <div class="center">

            <div class="border">
                <ul v-if="chain && chain.length" :key="chain">
                    <li v-for="item of chain" :key="item.key" :value="item.value">
                        <p>{{item.hash}}</p>
                        <p>{{item.index}}</p>
                        <p>{{item.nonce}}</p>
                        <p>{{item.previous_hash }}</p>
                        <p>{{item.timestamp | formatDate }}</p>
                        <p>{{item.transactions }}</p>
                    </li>
                </ul>
            </div>

            <ul v-if="errors && errors.length" :key="error.key" :value="error.value">
                <li v-for="error of errors" :key="error" :value="error.value">
                    {{error.message}}
                </li>
            </ul>

        </div>
    </div>
</template>

<script>
    // @ is an alias to /src
    import axios from 'axios'
    import moment from 'moment'


    export default {
        data() {
            return {
                chain: {},
                errors: {}
            }

        },
        filters: {
            round: function (value, accuracy, keep) {
                if (typeof value !== 'number') return value
                let fixed = value.toFixed(accuracy)
                return keep ? fixed : +fixed
            },
            capitalize: function (value) {
                if (!value) return ''
                value = value.toString()
                return value.charAt(0).toUpperCase() + value.slice(1)
            },
            formatDate: function (value) {
                if (value) {
                    return moment(String(value)).format('MM/DD/YYYY hh:mm')
                }
            }
        },

        mounted() {
            // console.log('mounted')
            axios.get('/api/chain')
                .then((response) => {
                    console.log(response)
                    this.chain = response.data.chain
                })
                .catch((error) => {
                    this.errors.push(error)
                })
        }
    }
</script>
<style lang="sass">

    .blockchain 

    .center 
        display: flex
        flex-wrap: wrap
        justify-content: center
        text-align: left
    

    .border 
        border: 1px solid darkgrey
    

    ul 
        list-style-type: none
        padding-right: 30px
    
</style>
