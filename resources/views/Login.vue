<script setup lang="ts">
import { router } from "@inertiajs/vue3";
import { reactive } from "vue";

defineProps({ errors: Object });

const form = reactive({
	first_name: null,
	last_name: null,
	email: null,
});

function submit() {
	router.post("/users", form);
}
</script>

<template>
  <form @submit.prevent="submit">
    <label for="first_name">First name:</label>
    <input id="first_name" v-model="form.first_name" />
    <div v-if="errors.first_name">{{ errors.first_name }}</div>
    <label for="last_name">Last name:</label>
    <input id="last_name" v-model="form.last_name" />
    <div v-if="errors.last_name">{{ errors.last_name }}</div>
    <label for="email">Email:</label>
    <input id="email" v-model="form.email" />
    <div v-if="errors.email">{{ errors.email }}</div>
    <button type="submit">Login</button>
  </form>
</template>

<style scoped>

</style>
