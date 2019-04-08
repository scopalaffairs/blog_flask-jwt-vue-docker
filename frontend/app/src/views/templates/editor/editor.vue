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
            </div>
        </editor-menu-bar>
        <editor-content :editor="editor"/>
    </div>
</template>

<script>
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
        Link,
        ListItem,
        OrderedList,
        Strike,
        TodoItem,
        TodoList,
        Underline,
    } from 'tiptap-extensions'

    export default {
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
                        new Link(),
                        new Strike(),
                        new Underline(),
                        new History(),
                    ],
                    content: 'some',
                }),
            }
        },
    }
</script>
