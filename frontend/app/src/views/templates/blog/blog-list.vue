<template>
    <div class="container">
        <fetch-json url="http://localhost:5000/api/v1/blogposts">
            <div class="" slot-scope="{ response: posts, loading }">
                <h1 class=""></h1>
                <div v-if="loading" class="text-grey-darker">
                    Loading...
                </div>
                <div v-else>
                    <div class="post__card" v-for="post in posts" v-bind:key="post.id">
                        <div v-if="isAuth">
                            <button @click.prevent="deletePost(post)">Delete</button>
                            <!--                            <button @click.prevent="editPost()">Edit</button>-->
                        </div>
                        <!--                        <div class="">{{ post.id }}</div>-->
                        <div class="">{{ post.category }}</div>

                        <div class="">{{ post.title }}</div>
                        <div class="">{{ post.description }}</div>
                        <!--                        <div class="">{{ post.contents }}</div>-->
                        <div class="post__card--datetime">{{ post.created_at | formatDate}}</div>
                        <div class="post__card--datetime">{{ post.modified_at | formatDate }}</div>
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
    import {mapGetters} from 'vuex'
    import axios from 'axios'
    import moment from 'moment'


    export default {
        components: {
            FetchJson
        },
        data() {
            return {posts: []}
        },
        computed: {
            ...mapGetters('auth', {
                isAuth: 'isAuthenticated',
            })
        },
        methods: {
            deletePost(post) {
                let token = localStorage.getItem('token');
                console.log("delete", post.id)
                axios({
                    method: 'DELETE',
                    url: 'http://localhost:5000/api/v1/blogposts/' + post.id,
                    headers: {
                        'api-token': token,
                        'Content-Type': 'application/json'
                    }
                })
            }
        },
        filters: {
            formatDate: function (value) {
                if (value) {
                    return moment(String(value)).format('MM/DD/YYYY hh:mm')
                }
            }
        },
    }
</script>

<style lang="scss" scoped>
    @import '@/assets/scss/components/post.scss'

</style>
