<template>
    <div class="container">
        <div>Admin Dashboard</div>
        <div>
            <div>Enter text:</div>
            <input type="text" v-model="title" placeholder="title"/>
<!--            <input type="text" v-model="contents" placeholder="content"/>-->
            <ckeditor :editor="editor" v-model="editorData" :config="editorConfig"></ckeditor>
            <button type="submit" class="btn" @click="createPost()">Submit</button>
        </div>
    </div>
</template>

<script>
    import ClassicEditor from '@ckeditor/ckeditor5-build-classic'
    import axios from 'axios'


    export default {

        name: 'dashboard',
        components: {},
        data() {
            return {
                editor: ClassicEditor,
                editorData: '<p>Content of the editor.</p>',
                editorConfig: {
                    // toolbar: ['bold', 'italic', '|', 'link']
                },
                title: null,
                contents: null,
            }
        },

        methods: {
            createPost() {
                let post = {
                    title: this.title,
                    contents: this.editorData
                }
                let token = localStorage.getItem('token');
                axios({
                    method: 'POST',
                    url: 'http://localhost:5000/api/v1/blogposts/',
                    headers: {
                        'api-token': token,
                        'Content-Type': 'application/json'
                    }, data: post
                })
            }
        }
    }
</script>
<style lang="scss">
    .btn {
        background: #2196F3;
        height:20px;
        width: 123px;
    }
</style>
