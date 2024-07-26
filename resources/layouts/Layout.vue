<script setup lang="ts">
import { route } from "@/utils/route.ts"
import { Link } from "@inertiajs/vue3"
import SidebarCompetition from "@/components/sidebar/SidebarCompetition.vue";
</script>

<template>
  <main>
    <header>
      <Link class="text-sm m-2" href="/">Home</Link>
      <Link class="text-sm m-2" href="/dashboard/">Dashboard</Link>
      <Link class="text-sm m-2" href="/login/">Login</Link>
      <Link class="text-sm m-2" href="/leaderboard/">Leaderboard</Link>
    </header>
    <div>
      <SidebarCompetition/>
      <slot />
    </div>
  </main>
</template>
