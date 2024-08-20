import "@/assets/styles/main.css"

import Layout from "@/layouts/Layout.vue"
import Lara from "@primevue/themes/aura"
import Button from "primevue/button"
import PrimeVue from "primevue/config"
import DatePicker from "primevue/datepicker"
import InputNumber from "primevue/inputnumber"
import Toast from "primevue/toast"
import ToastService from "primevue/toastservice"
import * as Sentry from "@sentry/vue";

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
    const app = createApp({ render: () => h(App, props) })

    Sentry.init({
      app: app,
      dsn: "https://3680a809128031157fb30980474bd515@sentry.laby.io/7",
      integrations: [
        Sentry.browserTracingIntegration(),
        Sentry.replayIntegration(),
      ],
      // Set tracesSampleRate to 1.0 to capture 100%
      // of transactions for performance monitoring.
      // We recommend adjusting this value in production
      tracesSampleRate: 1.0,

    });

    app.use(plugin)
      .use(ToastService)
      .use(PrimeVue, {
        theme: {
          preset: Lara,
        },
      })
      .component("Toast", Toast)
      .component("Button", Button)
      .component("InputNumber", InputNumber)
      .component("DatePicker", DatePicker)
      .mount(el)
  },
})
