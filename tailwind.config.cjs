const { fontFamily } = require("tailwindcss/defaultTheme")

/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ["class"],
  content: [
    "src/app/domain/web/{resources,templates}/**/*.{js,jsx,ts,cjs,mjs,tsx,vue,j2,html,htm}",
    "{resources,templates}/**/*.{js,cjs,mjs,jsx,ts,tsx,vue,j2,html,htm}",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("@tailwindcss/forms"), require("@tailwindcss/typography")],
}
