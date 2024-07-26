<script setup>
import { Head, Link } from "@inertiajs/vue3"
import Button from "primevue/button"
import DatePicker from "primevue/datepicker"
import InputNumber from "primevue/inputnumber"
import { useToast } from "primevue/usetoast"
import { ref } from "vue"
const toast = useToast()
defineProps({
  content: {
    message: String,
  },
})
const showToast = () => {
  toast.add({
    severity: "success",
    summary: "Competition created",
    detail: "test",
    life: 3000,
  })
}
const count = ref(0)
</script>

<template>
  <Head title="Dashboard" />
  <h1 class="text-xl">Dashboard</h1>
  <p class="text-sm">{{ content.message }}</p>
  <Button label="Success" severity="success" />
  <InputNumber v-model="value3" inputId="horizontal-buttons" showButtons buttonLayout="horizontal" :step="1" mode="currency" currency="EUR" fluid>
    <template #incrementbuttonicon>
        <span class="pi pi-plus" />
    </template>
    <template #decrementbuttonicon>
        <span class="pi pi-minus" />
    </template>
  </InputNumber>
  <DatePicker v-model="buttondisplay" showIcon fluid :showOnFocus="false" />
  <Toast />
  <Button @click="showToast" label="Count"></Button>
  <Link href="/schema">Visit Schema</Link>
</template>
