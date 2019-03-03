<template>
    <div>
        <h2>GET data from Flask API (/api/train)</h2>

        <div class="wrapper">
            <p>/api/train</p>
            <p class="results"><span>{{ testData[0] | capitalize }} {{ testData[2] | round('4', true) }}</span></p>
            <p class="results"><span>{{ testData[1] | capitalize }} {{ testData[3] | round('4', true) }}</span></p>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        data() {
            return {
                testData: {}
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
            }
        },

        mounted() {
            // console.log('mounted')
            axios.get('/api/train')
                .then((response) => {
                    console.log(response)
                    this.testData = response.data
                })
                .catch((error) => {
                    console.log(error)
                })
        }
    }

</script>

<style scoped>

    h1, h2 {
        font-weight: normal;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #42b983;
    }

    .wrapper {
        padding: 20px 40px;
        max-width: 400px;
        margin: 0 auto;
        background: orange;
    }

    .results {
        text-align: left;
    }
</style>
