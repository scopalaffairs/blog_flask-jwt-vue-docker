import {Node} from 'tiptap'
// import {Carousel, Slide} from 'vue-carousel'


export default class Carousel extends Node {

    get name() {
        return 'carousel'
    }

    get schema() {
        return {
            attrs: {
                src: {
                    default: null,
                },
            },
            group: 'block',
            selectable: false,
            parseDOM: [{
                tag: 'Carousel',
                getAttrs: dom => ({
                    src: dom.getAttribute('src'),
                }),
            }],
            toDOM: node => ['Carousel', {
                src: node.attrs.src
            }],
        }
    }

    get view() {
        return {
            props: ['node', 'updateAttrs', 'editable'],
            computed: {
                src: {
                    get() {
                        return this.node.attrs.src
                    },
                    set(src) {
                        this.updateAttrs({
                            src,
                        })
                    },
                },
            },
            template: `
        <div class="carousel">
          <Carousel class="carousel__embed" :src="src" :perPage="1">
            <Slide class="carousel__slide" v-model="src" v-if="editable">
                <img :src="src" @paste.stop>
            </Slide>
          </Carousel>
        </div>
      `,
        }
    }

}
