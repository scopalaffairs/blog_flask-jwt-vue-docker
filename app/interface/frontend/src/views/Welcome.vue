<template>
    <div class="">
        <ProjectHeadline></ProjectHeadline>
        <ProjectDescription></ProjectDescription>
    </div>
</template>

<script>
    import Axios from '@/components/Axios.vue'

    import ProjectHeadline from "@/views/templates/project/Project-Headline"
    import ProjectDescription from "@/views/templates/project/Project-Description"

    export default {
        name: 'home',
        components: {
            ProjectDescription,
            ProjectHeadline,
            Axios,

        }
    }
</script>
<style lang="sass">
</style>
