<script setup lang="ts">
import { route } from "@/utils/route.ts"
import { Link } from "@inertiajs/vue3"
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
      <slot />
    </div>
  </main>
</template>
