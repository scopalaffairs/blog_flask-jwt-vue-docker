<template>
    <div class="min-h-screen bg-grey-darker p-8">
        <div class="max-w-md mx-auto">

            <fetch-json url="http://localhost:5000/todo/api/v1.0/tasks">
                <div class="card" slot-scope="{ response: tasks, loading }">
                    <h1 class="text-2xl font-bold mb-6">bloglist</h1>
                    <div v-if="loading" class="text-grey-darker">
                        Loading...
                    </div>
                    <div v-else>
                        {{tasks}}
                        <div class="" v-for="task in tasks" v-bind:key="task.id">
                            <div class="">{{ task.id }}</div>
                            <h2 class="">{{ task.title }}</h2>
                            <p class="">{{ task.description }}</p>
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
            return {tasks: []}
        }
    }
</script>

<style scoped>

</style>
