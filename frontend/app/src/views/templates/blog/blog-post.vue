<template>
    <div class="">
        Individual BlogPost
        <fetch-json url="'http://localhost:5000/api/v1/blogposts/2">
            <div class="post_card">
                <div class="">{{ post.id }}</div>
                <div class="">{{ post.title }}</div>
                <div class="" v-html="post.contents"></div>
                <div class="">{{ post.created_at }}</div>
                <div class="">{{ post.modified_at }}</div>
            </div>
        </fetch-json>
    </div>
</template>

<script>
    import FetchJson from "@/components/FetchJson.vue"

    export default {
        name: 'blogpost',
        props: ['post'],
        components: {
            FetchJson,
        },
        data() {
            return {
                post: [],
            }
        }
    }
</script>

<style scoped>

</style>
