<template>
  <div class="card">
    <h1 class="text-2xl font-bold mb-6">Your Contacts</h1>
    <div>
      <div v-for="contact in contacts" :key="contact.id" class="flex items-center spaced-y-6">
        <div>
          <div class="font-bold">
            {{ contact.userId }} {{ contact.title }}
          </div>
          <div class="text-grey-dark">
            {{ contact.completed }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["contacts"]
}
</script>
