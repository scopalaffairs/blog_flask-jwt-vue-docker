<template>
    <div class="container">
        <fetch-json url="http://localhost:5000/api/v1/blogposts">
            <div class="" slot-scope="{ response: posts, loading }">
                <h1 class="">bloglist</h1>
                <div v-if="loading" class="text-grey-darker">
                    Loading...
                </div>
                <div v-else>
                    <div class="post_card" v-for="post in posts" v-bind:key="post.id">
                        <div class="">{{ post.id }}</div>
                        <div class="">{{ post.title }}</div>
                        <div class="">{{ post.description }}</div>
<!--                        <div class="">{{ post.contents }}</div>-->
                        <div class="">{{ post.created_at }}</div>
                        <div class="">{{ post.modified_at }}</div>
                        <router-link :to="{ name: 'blogContent', params: { postId: post.id }}">
                            more...
                        </router-link>
                    </div>
                </div>
            </div>
        </fetch-json>
    </div>
</template>

<script>
    import FetchJson from "@/components/FetchJson.vue"

    export default {
        components: {
            FetchJson
        },
        data() {
            return {posts: []}
        }
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
