<script setup lang="ts">
import { Link } from "@inertiajs/vue3"
import { route } from "@/utils/route.ts"
</script>

<template>
  <main>
    <header>
      <Link class="text-sm m-2" href="/">Home</Link>
      <Link class="text-sm m-2" href="/dashboard/">Dashboard</Link>
      <Link class="text-sm m-2" href="/login/">Login</Link>
    </header>
    <div>
      <slot />
    </div>
  </main>
</template>
