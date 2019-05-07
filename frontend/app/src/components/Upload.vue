<template>
    <div>
        <p>Upload</p>

        <picture-input ref="pictureInput" @change="onChange" width="100" height="100" margin="8"
                       accept="image/jpeg,image/png" size="10"
                       :removable="true" :customStrings="{
                upload: '',
                drag: 'Drag an Image'
              }">
        </picture-input>
    </div>
</template>

<script>
    import PictureInput from 'vue-picture-input'
    import axios from 'axios'

    export default {
        name: 'Upload',
        data() {
            return {}
        },
        components: {
            PictureInput
        },
        methods: {
            sendUploadToBackend(data) {
                let token = localStorage.getItem('token');
                const path = 'http://localhost:5000/api/v1/upload/';

                axios({
                    method: 'POST',
                    url: path,
                    headers: {
                        // 'api-token': token,
                        'Content-Type': 'multipart/form-data'
                    },
                    data
                });
                console.log('sendUploadToBackend')
            },
            onChange(image) {
                console.log('picture changed!');
                if (this.$refs.pictureInput.image) {
                    console.log('Picture is loaded.');
                    // this.sendUploadToBackend(this.$refs.pictureInput.file.name, this.$refs.pictureInput.image)
                    this.sendUploadToBackend(this.$refs.pictureInput.image)
                } else {
                    console.log('error')
                }
            },
        }

    }
</script>

<style lang="scss" scoped>
</style>
