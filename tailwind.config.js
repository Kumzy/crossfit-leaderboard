/** @type {import('tailwindcss').Config} */
import forms from 'tailwindcss';
import typography from 'tailwindcss';

export default  {
  darkMode: ["class"],
  content: [
    "src/app/domain/web/{resources,templates}/**/*.{js,jsx,ts,cjs,mjs,tsx,vue,j2,html,htm}",
    "{resources,templates}/**/*.{js,cjs,mjs,jsx,ts,tsx,vue,j2,html,htm}",
  ],
  theme: {
    extend: {},
  },
  plugins: [forms, typography],
}
