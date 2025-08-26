export default defineNuxtConfig({
  modules: ['@nuxt/ui', '@pinia/nuxt'],
  css: ['~/assets/css/main.css'],
  runtimeConfig: {
    public: {
      apiBase: process.env.API_BASE || 'http://localhost:8000/api',
    },
  },

  compatibilityDate: '2025-08-23',
})
