// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: "https://Yaofang-Liu.github.io",
  base: '/Pusa_Web/',

  vite: {
    plugins: [tailwindcss()],
  },
});