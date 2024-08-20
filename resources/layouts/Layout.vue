<script setup lang="ts">
import SidebarCompetition from "@/components/sidebar/SidebarCompetition.vue"
import { Link } from "@inertiajs/vue3"
import { route } from "litestar-vite-plugin/inertia-helpers"
</script>

<template>
  <main>
    <header>
      <Link class="text-sm m-2" :href="route('home')">Home</Link>
      <Link class="text-sm m-2" :href="route('dashboard')">Dashboard</Link>
      <Link class="text-sm m-2" :href="route('login')">Login</Link>
      <Link class="text-sm m-2" :href="route('leaderboard')">Leaderboard</Link>
    </header>
    <div>
      <SidebarCompetition/>
      <slot />
    </div>
  </main>
</template>
