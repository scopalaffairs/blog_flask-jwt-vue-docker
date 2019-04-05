<template>
    <div class="">
        <fetch-json url="http://localhost:5000/api/v1/blogposts">
            <div class="" slot-scope="{ response: posts, loading }">
                <h1 class="">bloglist</h1>
                <div v-if="loading" class="text-grey-darker">
                    Loading...
                </div>
                <div v-else>
                    <div class="" v-for="post in posts" v-bind:key="post.id">
                        <div class="">{{ post.id }}</div>
                        <div class="">{{ post.title }}</div>
                        <div class="">{{ post.description }}</div>
                        <div class="">{{ post.contents }}</div>
                        <div class="">{{ post.created_at }}</div>
                        <div class="">{{ post.modified_at }}</div>
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

</style>
