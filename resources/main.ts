// import "@/assets/main.css";
//
// import { createPinia } from "pinia";
// import { createApp } from "vue";
//
// import App from "./App.vue";
// import router from "./router";
//
// const app = createApp(App);
//
// app.use(createPinia());
// app.use(router);
//
// app.mount("#root");

import "@/assets/main.css";

import { createInertiaApp } from "@inertiajs/vue3";
import { createApp, h } from "vue";
import Layout from "@/Layout.vue";

createInertiaApp({
	resolve: (name) => {
		const pages = import.meta.glob("./views/**/*.vue", {
			eager: true,
		});
		const page = pages[`./views/${name}.vue`];
		page.default.layout = page.default.layout || Layout;
		return page;
	},
	setup({ el, App, props, plugin }) {
		createApp({ render: () => h(App, props) })
			.use(plugin)
			.mount(el);
	},
});
