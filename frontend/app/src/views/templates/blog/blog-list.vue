<template>
    <div class="container">
        <fetch-json url="http://localhost:5000/api/v1/blogposts">
            <div class="" slot-scope="{ response: posts, loading }">
                <h1 class=""></h1>
                <div v-if="loading" class="text-grey-darker">
                    Loading...
                </div>
                <div v-else>
                    <template>
                        <v-autocomplete :items="posts" v-model="post" :get-label="getLabel"
                                        :component-item='template'
                                        @update-items="updateItems">
                        </v-autocomplete>
                    </template>
                    <div class="post__card" v-for="post in posts" v-bind:key="post.id">
                        <div class="post__card--image">
                            <img :src="post.header_img"/>
                        </div>
                        <div class="post__card--category">{{ post.category }}</div>
                        <div class="post__card--title">{{ post.title }}</div>
                        <div class="post__card--contents" v-html="truncate(post.contents)"></div>
                        <router-link :to="{ name: 'blogContent', params: { postId: post.id }}">
                            <button class="post__card--continue">continue reading...</button>
                        </router-link>
                        <div class="flex-container">
                            <div class="post__card--datetime mr-4">created: {{ post.created_at | formatDate}}</div>
                            <div class="post__card--datetime">modified: {{ post.modified_at | formatDate }}</div>
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
    import VAutocomplete from 'v-autocomplete'


    export default {
        components: {
            FetchJson,
            VAutocomplete
        },
        data() {
            return {
                posts: [],
                post: ["start"]
            }
        },
        computed: {
            ...mapGetters('auth', {
                isAuth: 'isAuthenticated',
            })
        },
        methods: {
            getLabel(post) {
                return post.title
            },
            updateItems(text) {
                this.post = posts.filter((post) => {
                    return (new RegExp(text.toLowerCase())).test(post.title.toLowerCase())
                })
            },
            truncate: function (description) {
                return Truncate(description, 140)
            }
            ,
            deletePost: function (post) {
                let token = localStorage.getItem('token');
                console.log("delete", post.id);
                axios({
                    method: 'DELETE',
                    url: 'http://localhost:5000/api/v1/blogposts/' + post.id,
                    headers: {
                        'api-token': token,
                        'Content-Type': 'application/json',
                        'Access-Control-Allow-Origin': '*'
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
        }
        ,
    }
</script>

<style lang="scss" scoped>
    @import '@/assets/scss/components/post.scss';

    .flex-container {
        width: 100%;
        display: flex;
        justify-content: flex-end;
    }

    .mr-4 {
        margin-right: 40px;
    }

</style>
