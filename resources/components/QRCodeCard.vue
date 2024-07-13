<script setup lang="ts">
import VueQrcode from "vue-qrcode"

interface Props {
  qrCodeSrc: string
  link: string
}

const props = defineProps<Props>()
</script>

<template>
<!--<div class="max-w-sm mx-auto bg-white shadow-md rounded-lg overflow-hidden">-->
<!--  <div class="flex items-center">-->
<!--    <div class="p-4">-->
<!--      <vue-qrcode :value="link" class="w-24 h-24 object-cover"/>-->
<!--    </div>-->
<!--    <div class="p-4">-->
<!--      <a :href="link" class="text-blue-500 hover:text-blue-700 underline">-->
<!--        {{ link }}-->
<!--      </a>-->
<!--    </div>-->
<!--  </div>-->
<!--</div>-->
<div class="divide-y divide-gray-200 overflow-hidden rounded-lg bg-white shadow">
  <div class="px-4 py-5 sm:px-6">
    Event link
  </div>
  <div class="px-4 py-5 sm:p-6">
    <div class="flex items-center">
      <vue-qrcode :value="link" class="w-24 h-24 object-cover"/>
      <a :href="link" class="text-blue-500 hover:text-blue-700 underline">
        {{ link }}
      </a>
    </div>
  </div>
</div>
</template>

<style scoped>

</style>
