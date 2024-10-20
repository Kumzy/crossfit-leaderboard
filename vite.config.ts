import path from "node:path";
import vue from "@vitejs/plugin-vue";
import litestar from "litestar-vite-plugin";
import { defineConfig } from "vite";

const ASSET_URL = process.env.ASSET_URL || "/static/";
const VITE_PORT = process.env.VITE_PORT || "5173";
const VITE_HOST = process.env.VITE_HOST || "localhost";
export default defineConfig({
	base: `${ASSET_URL}`,
	clearScreen: false,
	publicDir: "public/",
	server: {
		host: "0.0.0.0",
		port: +`${VITE_PORT}`,
		cors: true,
		hmr: {
			host: `${VITE_HOST}`,
		},
	},
	plugins: [
		vue({
			template: {
				transformAssetUrls: {
					// The Vue plugin will re-write asset URLs, when referenced
					// in Single File Components, to point to the Laravel web
					// server. Setting this to `null` allows the Laravel plugin
					// to instead re-write asset URLs to point to the Vite
					// server instead.
					base: null,

					// The Vue plugin will parse absolute URLs and treat them
					// as absolute paths to files on disk. Setting this to
					// `false` will leave absolute URLs un-touched so they can
					// reference assets in the public directory as expected.
					includeAbsolute: false,
				},
			},
		}),
		litestar({
			input: ["resources/main.ts"],
			assetUrl: `${ASSET_URL}`,
			bundleDirectory: "src/app/domain/web/public",
			resourceDirectory: "resources",
			hotFile: "src/app/domain/web/public/hot",
		}),
	],
	resolve: {
		alias: {
			"@": path.resolve(__dirname, "resources"),
		},
	},
	build: {
		rollupOptions: {
			output: {
				manualChunks(id) {
					if (id.includes("node_modules")) {
						return "vendor";
					}
				},
			},
		},
	},
});
