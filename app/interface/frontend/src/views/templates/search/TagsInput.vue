<template>
    <div class="p-8 xs:p-0">
        <div class="max-w-sm mx-auto">
            <label class="form-label mb-2"></label>
            <renderless-tag-input v-model="tags">
                <div class="tag-input"
                     slot-scope="{ tags, removeTag, removeButtonEvents, inputProps, inputEvents }">
          <span v-for="tag in tags" :key="tag" class="tag-input-tag">
            <button type="button" class="btn-blue"
                    v-on="removeButtonEvents(tag)">
            <span>{{ tag }}</span>
                &times;</button>
          </span>
                    <input class="tag-input-text" placeholder="Add tags..."
                           v-bind="inputProps"
                           v-on="inputEvents"
                    >
                </div>
            </renderless-tag-input>
        </div>
    </div>
</template>

<script>
    import RenderlessTagInput from '../../../components/RenderlessTagInput.vue'

    export default {
        components: {
            RenderlessTagInput,
        },
        data() {
            return {
                tags: ['heidelberg', 'circRNA', 'human'],
            }
        }
    }
</script>
