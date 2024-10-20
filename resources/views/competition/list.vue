<script setup>
import { Link } from "@inertiajs/vue3"
import { Head } from "@inertiajs/vue3"
import { route } from "litestar-vite-plugin/inertia-helpers"
import { onMounted } from "vue"

import { useAttrs } from "vue"
const attrs = useAttrs()
console.log(attrs.content.items)
</script>

<template>
  <div class="card">
    <DataView :value="attrs.content.items" paginator :rows="attrs.content.limit" :rowsPerPageOptions="attrs.content.total" dataKey="id">
      <template #list="slotProps">
        <div class="col-12">
          <div v-for="(item, index) in slotProps.items" :key="index">
          <div class="flex flex-col sm:flex-row justify-between items-center p-4 gap-4 bg-white shadow-md rounded-lg">
            <div>
              <h2 class="text-2xl font-semibold text-blue-600">{{ item.name }}</h2>
              <p class="text-gray-600">
                <span class="font-medium">Location:</span> {{ item.location }}
              </p>
            </div>
            <div>
              <span class="font-medium text-gray-700">Categories:</span>
              <div class="flex flex-wrap gap-2 mt-2">
                <span v-for="(division, index) in item.divisions" :key="index"
                  class="bg-blue-100 text-blue-800 text-sm font-medium px-3 py-1 rounded-full">
                  {{ division.name }}
                </span>
              </div>
            </div>
          </div>
          </div>
        </div>
      </template>
    </DataView>
</div>
</template>

<style scoped>

</style>
