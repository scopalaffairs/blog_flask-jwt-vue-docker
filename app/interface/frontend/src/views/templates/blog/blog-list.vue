<template>
    <div class="min-h-screen bg-grey-darker p-8">
        <div class="max-w-md mx-auto">

            <fetch-json url="http://localhost:8000/bucketlists/1">
                <div class="card" slot-scope="{ response: test, loading }">
                    <h1 class="text-2xl font-bold mb-6">bloglist</h1>
                    <div v-if="loading" class="text-grey-darker">
                        Loading...
                    </div>
                    <div v-else>
                        <div class="" v-for="test in tests" v-bind:key="test">
                            <div class="">{{ test.id }}</div>
                            <h2 class="">{{ test.title }}</h2>
                            <p class="">{{ test.userId }}</p>
                        </div>
                    </div>
                </div>
            </fetch-json>

        </div>
    </div>
</template>

<script>
    import FetchJson from "@/components/FetchJson.vue"

    export default {
        components: {
            FetchJson
        },
        data() {
            return {}
        }
    }
</script>

<style scoped>

</style>
