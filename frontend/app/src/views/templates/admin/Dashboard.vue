<template>
    <div class="container">
        <div>Admin Dashboard</div>
        <div>
            some super secret Komponents to edit Blogposts and Analyse stuff nobody knows about
            <ckeditor :editor="editor" v-model="editorData" :config="editorConfig"></ckeditor>
        </div>
    </div>
</template>

<script>
    import ClassicEditor from '@ckeditor/ckeditor5-build-classic';

    export default {

        name: 'dashboard',
        components: {},
        data() {
            return {
                editor: ClassicEditor,
                editorData: '<p>Content of the editor.</p>',
                editorConfig: {
                    // toolbar: ['bold', 'italic', '|', 'link']
                }
            }
        }

    }
</script>
