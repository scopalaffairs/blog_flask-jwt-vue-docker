<template>
    <div>
        <card>
            <template slot="heading">
                What's new
            </template>
        </card>
        <card>
            <template slot="heading">
                <h5 class="">Carina webpage first test</h5>
            </template>
            <template slot="text-body" class="text-sm">
                <div class="text-xs">22 Mar 2018</div>
                <a href="#">
                    <p class="">Just test</p>
                    <primary-button class=""> Click for more details</primary-button>
                </a>
            </template>
        </card>

        <card>
            <template slot="heading">
                <h5 class="">doRiNA was ported to python 3</h5>
            </template>
            <template slot="text-body" class="text-sm">
                <div class="text-xs">18 Dec 2017</div>
                <a href="https://github.com/dieterich-lab/dorina/commit/035fa4fc00d437a3ae2cbb825c233b2da4821da4">
                    <p class="">
                        doRiNA was updated to work with python3
                    </p>
                </a>
                    <primary-button class="">Click for more details</primary-button>
            </template>
        </card>

    </div>
</template>

<script>
    import axios from 'axios'
    import Truncate from 'truncate'
    import Card from '../views/templates/molecules/Card.vue'
    import PrimaryButton from '../views/templates/atoms/PrimaryButton.vue'

    export default {
        name: 'NewsRoom',
        components: {Card, PrimaryButton},
        data: function () {
            return {
                articles: {}
            }
        },
        methods: {
            loadArticles: function () {
                let url = 'https://newsapi.org/v2/top-headlines?country=de&apiKey=' + 'c6422b14c12d487da0fba725a3c1fa40';

                axios.get(url).then(response => {
                    this.articles = response.data.articles
                })
            },
            truncate: function (description) {
                return Truncate(description, 100)
            }
        },
        mounted() {
            this.loadArticles()
        }
    }
</script>
