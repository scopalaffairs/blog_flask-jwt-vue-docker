<template>
    <div class="container">
        <div class="">
            <div>Title:</div>
            <input type="text" v-model="title" placeholder="Title"/>
            <div>Category:</div>
            <select v-model="category" placeholder="Category">
                <option>Curatory/Arts</option>
                <option>Experimental/Film</option>
                <option>Experimental/Installation</option>
                <option>Video</option>
                <option>Audio</option>
            </select>

            <div>Header Image:</div>
            <Upload/>

            <br/>
            <div>Content:</div>
            <template>
                <div class="editor">
                    <editor-menu-bar :editor="editor">
                        <div slot-scope="{ commands, isActive }">
                            <button
                                class="menubar__button"
                                :class="{ 'is-active': isActive.bold() }"
                                @click="commands.bold"
                            >
                                <app-icon name="bold" size="m" fill></app-icon>
                            </button>

                            <button
                                class="menubar__button"
                                :class="{ 'is-active': isActive.italic() }"
                                @click="commands.italic"
                            >
                                <app-icon name="italic" size="m" fill></app-icon>
                            </button>

                            <button
                                class="menubar__button"
                                :class="{ 'is-active': isActive.strike() }"
                                @click="commands.strike"
                            >
                                <app-icon name="strike" size="m" fill></app-icon>
                            </button>

                            <button
                                class="menubar__button"
                                :class="{ 'is-active': isActive.underline() }"
                                @click="commands.underline"
                            >
                                <app-icon name="underline" size="m" fill></app-icon>
                            </button>

                            <button
                                class="menubar__button"
                                :class="{ 'is-active': isActive.code() }"
                                @click="commands.code"
                            >
                                <app-icon name="code" size="m" fill></app-icon>
                            </button>

                            <button
                                class="menubar__button"
                                :class="{ 'is-active': isActive.paragraph() }"
                                @click="commands.paragraph"
                            >
                                <app-icon name="paragraph" size="m" fill></app-icon>
                            </button>

                            <button
                                class="menubar__button"
                                :class="{ 'is-active': isActive.heading({ level: 1 }) }"
                                @click="commands.heading({ level: 1 })"
                            >
                                H1
                            </button>

                            <button
                                class="menubar__button"
                                :class="{ 'is-active': isActive.heading({ level: 2 }) }"
                                @click="commands.heading({ level: 2 })"
                            >
                                H2
                            </button>

                            <button
                                class="menubar__button"
                                :class="{ 'is-active': isActive.heading({ level: 3 }) }"
                                @click="commands.heading({ level: 3 })"
                            >
                                H3
                            </button>

                            <button
                                class="menubar__button"
                                :class="{ 'is-active': isActive.bullet_list() }"
                                @click="commands.bullet_list"
                            >
                                <app-icon name="ul" size="m" fill></app-icon>
                            </button>

                            <button
                                class="menubar__button"
                                :class="{ 'is-active': isActive.ordered_list() }"
                                @click="commands.ordered_list"
                            >
                                <app-icon name="ol" size="m" fill></app-icon>
                            </button>

                            <button
                                class="menubar__button"
                                :class="{ 'is-active': isActive.blockquote() }"
                                @click="commands.blockquote"
                            >
                                <app-icon name="quote" size="m" fill></app-icon>
                            </button>

                            <!--                            <button-->
                            <!--                                class="menubar__button"-->
                            <!--                                @click="commands.horizontal_rule"-->
                            <!--                            >-->
                            <!--                                <app-icon name="hr" size="m" fill></app-icon>-->
                            <!--                            </button>-->
                            <button
                                class="menubar__button"
                                :class="{ 'is-active': isActive.todo_list() }"
                                @click="commands.todo_list"
                            >
                                <app-icon name="checklist" size="m" fill></app-icon>
                            </button>

                            <button
                                class="menubar__button"
                                @click="commands.undo"
                            >
                                <app-icon name="undo" size="m" fill></app-icon>
                            </button>

                            <button
                                class="menubar__button"
                                @click="commands.redo"
                            >
                                <app-icon name="redo" size="m" fill></app-icon>
                            </button>
                        </div>
                    </editor-menu-bar>
                    <editor-content class="editor__content" :editor="editor"/>
                </div>
            </template>

            <button type="submit" class="btn btn--full" @click="createPost()">Submit</button>
        </div>
    </div>
</template>

<script>
    import AppIcon from '@/components/AppIcon'
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
        Image,
        Italic,
        Link,
        ListItem,
        OrderedList,
        Strike,
        TodoItem,
        TodoList,
        Underline,
    } from 'tiptap-extensions'
    import Carousel from './Carousel.js'
    import Upload from '@/components/Upload'

    export default {

        name: 'dashboard',
        components: {
            EditorMenuBar,
            EditorContent,
            AppIcon,
            Upload
        },
        data() {
            return {
                title: '',
                category: '',
                contents: null,
                header_img: null,
                avatar: null,
                saving: false,
                saved: false,

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
                        // custom extension
                        new Carousel(),
                    ],
                    content: 'some',
                }),
            }
        },
        beforeDestroy() {
            this.editor.destroy()
        },
        methods: {
            createPost() {
                let post = {
                    title: this.title,
                    category: this.category,
                    contents: this.editor.getHTML()
                }

                console.log("output", this.editor);
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
    @import '@/assets/scss/variables.scss';
    @import '@/assets/scss/components/editor.scss';
</style>
