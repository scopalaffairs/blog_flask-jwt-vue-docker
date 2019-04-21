<template>
    <div class="container">
        <div class="post__card">
            <div class="">{{ post.category }}</div>

            <div class="">{{ post.id }}</div>
            <div class="">{{ post.title }}</div>
            <div class="" v-html="post.contents"></div>
            <div class="post__card--datetime">{{ post.created_at | formatDate }}</div>
            <div class="post__card--datetime">{{ post.modified_at | formatDate }}</div>
        </div>
    </div>
</template>

<script>
    import {Carousel, Slide} from 'vue-carousel'
    import moment from 'moment'

    export default {
        name: 'blogpost',
        components: {
            Carousel,
            Slide
        },
        data() {
            return {
                post: {},
            }
        },
        filters: {
            formatDate: function (value) {
                if (value) {
                    return moment(String(value)).format('MM/DD/YYYY hh:mm')
                }
            }
        },
        mounted() {
            let postId = this.$route.params.postId;
            let url = 'http://localhost:5000/api/v1/blogposts/';

            fetch(url + postId)
                .then(response => response.json())
                .then(response => {
                    this.post = response;
                    // this.loading = false
                })
        }
    }
</script>

<style lang="scss" scoped>
    @import '@/assets/scss/components/post.scss'
</style>
