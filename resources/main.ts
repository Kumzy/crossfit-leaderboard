import "@/assets/styles/main.css"

import Layout from "@/layouts/Layout.vue"
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
      .mount(el)
  },
})
