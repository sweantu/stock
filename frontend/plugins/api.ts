export interface PagingResponse<T> {
  total: number
  page: number
  page_size: number
  items: T[]
}

export default defineNuxtPlugin(() => {
  const api = $fetch.create({
    baseURL: useRuntimeConfig().public.apiBase,
    credentials: 'include',
    onRequest({ request, options }) {
      console.log('➡️ Request:', request, options)
    },
    onResponse({ response }) {
      console.log('✅ Response:', response)
    },
    onRequestError({ error }) {
      console.error('❌ Request error:', error)
    },
    onResponseError({ error }) {
      console.error('❌ Response error:', error)
    },
  })

  return {
    provide: {
      api,
    },
  }
})
