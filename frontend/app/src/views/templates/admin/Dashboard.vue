<template>
    <div class="container">
        <div>Admin Dashboard</div>
        <div>
            <div>Enter text:</div>
            <input type="text" v-model="title" placeholder="title"/>
            <!--            <input type="text" v-model="contents" placeholder="content"/>-->
            <!--            <ckeditor :editor="editor" v-model="editorData" :config="editorConfig"></ckeditor>-->
            <template>
                <div>
                    <editor-menu-bar :editor="editor">
                        <div slot-scope="{ commands, isActive }">
                            <button :class="{ 'is-active': isActive.bold() }" @click="commands.bold">
                                Bold
                            </button>
                            <button :class="{ 'is-active': isActive.italic() }" @click="commands.italic">
                                Italic
                            </button>
                            <button :class="{ 'is-active': isActive.heading({ level: 2 }) }"
                                    @click="commands.heading({ level: 2 })">
                                H2
                            </button>
                            <button
                                class=""
                                @click="showImagePrompt(commands.image)"
                            >
                                Image
                            </button>
                        </div>
                    </editor-menu-bar>
                    <editor-content :editor="editor"/>
                </div>
            </template>

            <button type="submit" class="btn" @click="createPost()">Submit</button>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import {Editor, EditorContent, EditorMenuBar} from 'tiptap'
    import {
        Blockquote,
        Bold,
        BulletList,
        Code,
        CodeBlock,
        HardBreak,
        Heading,
        History,
        Italic,
        Image,
        Link,
        ListItem,
        OrderedList,
        Strike,
        TodoItem,
        TodoList,
        Underline,
    } from 'tiptap-extensions'

    export default {

        name: 'dashboard',
        components: {
            EditorMenuBar,
            EditorContent
        },
        data() {
            return {
                title: null,
                contents: null,
                // editorData: null,

                editor: new Editor({
                    extensions: [
                        new Blockquote(),
                        new CodeBlock(),
                        new HardBreak(),
                        new Heading({levels: [1, 2, 3]}),
                        new BulletList(),
                        new OrderedList(),
                        new ListItem(),
                        new TodoItem(),
                        new TodoList(),
                        new Bold(),
                        new Code(),
                        new Italic(),
                        new Image(),
                        new Link(),
                        new Strike(),
                        new Underline(),
                        new History(),
                    ],
                    content: 'some',
                }),
            }
        },
        methods: {
            showImagePrompt(command) {
                const src = prompt('Enter the url of your image here')
                if (src !== null) {
                    command({src})
                }
            },
            createPost() {
                let post = {
                    title: this.title,
                    contents: this.editor.getHTML()
                }

                console.log("output", this.title, this.editor.getJSON())
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
        color: white;
        border-radius: 0;
        /*height:20px;*/
        /*width: 123px;*/
    }
</style>
