<script setup lang="ts">
import type { API } from "@/api/api-specs.ts";
import { router } from "@inertiajs/vue3";
import { reactive } from "vue";

defineProps({ errors: Object });

const form: API.AccountLogin.RequestBody = reactive({});

function submit() {
	router.post("/api/access/login", form);
}
</script>

<template>
  <form @submit.prevent="submit">
    <label for="uersname">Username:</label>
    <input id="username" v-model="form.username" />
    <div v-if="errors.username">{{ errors.username }}</div>
    <label for="password">Password:</label>
    <input id="password" type="password" v-model="form.password" />
    <div v-if="errors.password">{{ errors.password }}</div>
    <button type="submit">Login</button>
  </form>
</template>

<style scoped>

</style>
