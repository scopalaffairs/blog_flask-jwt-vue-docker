<template>
    <div class="container">

        <div class="post_card">
            <div class="">{{ post.id }}</div>
            <div class="">{{ post.title }}</div>
            <div class="" v-html="post.contents"></div>
            <div class="">{{ post.created_at }}</div>
            <div class="">{{ post.modified_at }}</div>
        </div>
    </div>
</template>

<script>
    import {Carousel, Slide} from 'vue-carousel'

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
        mounted() {
            let postId = this.$route.params.postId;
            let url = 'http://localhost:5000/api/v1/blogposts/';

            fetch(url + postId)
                .then(response => response.json())
                .then(response => {
                    this.post = response;
                    // this.loading = false
                })
        },
        // render() {
        //     return this.$scopedSlots.default({
        //         post: this.response,
        //         loading: this.loading
        //     })
        // }
    }
</script>

<style scoped>
    .container {
        padding: 2rem;
    }

    .post_card {

        padding: 2rem;
        background: white;
        border: 1px solid gainsboro;
        margin-bottom: .5rem;

    }

</style>
