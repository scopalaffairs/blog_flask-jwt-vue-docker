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
                        <div class="post__card--category">{{ post.category }}</div>
                        <div class="post__card--title">{{ post.title }}</div>
                        <div class="post__card--contents" v-html="truncate(post.contents)"></div>
                        <router-link :to="{ name: 'blogContent', params: { postId: post.id }}">
                            <button class="post__card--continue">continue reading...</button>
                        </router-link>
                        <div class="">
                            <div class="post__card--datetime">created {{ post.created_at | formatDate}}</div>
                            <div class="post__card--datetime">modified {{ post.modified_at | formatDate }}</div>
                        </div>

                        <!-- admin interface -->
                        <div v-if="isAuth">
                            <div class="post__card--adminPanel">
                                <button class="btn btn--primary"
                                        @click.prevent="deletePost(post)"
                                >
                                    Delete
                                </button>

                            </div>
                        </div>
                        <!-- /admin interface -->
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
    import Truncate from 'truncate'


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
            truncate: function (description) {
                return Truncate(description, 140)
            },
            deletePost: function (post) {
                let token = localStorage.getItem('token');
                console.log("delete", post.id);
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
    @import '@/assets/scss/components/post.scss';

</style>
