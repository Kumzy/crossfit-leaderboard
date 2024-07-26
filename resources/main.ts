import "@/assets/styles/main.css"

import Layout from "@/layouts/Layout.vue"
import PrimeVue from "primevue/config";
import Button from "primevue/button";
import InputNumber from 'primevue/inputnumber';
import DatePicker from 'primevue/datepicker';
import Toast from "primevue/toast";
import ToastService from "primevue/toastservice";
import Lara from '@primevue/themes/aura';

import { createInertiaApp } from "@inertiajs/vue3"
import { createApp, h } from "vue"

createInertiaApp({
  resolve: (name) => {
    const pages = import.meta.glob("./views/**/*.vue", {
      eager: true,
    })
    const page = pages[`./views/${name}.vue`]
    page.default.layout = page.default.layout || Layout
    return page
  },
  setup({ el, App, props, plugin }) {
    createApp({ render: () => h(App, props) })
      .use(plugin)
      .use(ToastService)
      .use(PrimeVue, {
        theme: {
          preset: Lara
        }
      })
      .component('Toast',Toast)
      .component('Button', Button)
      .component('InputNumber', InputNumber)
      .component('DatePicker', DatePicker)
      .mount(el)
  },
})
