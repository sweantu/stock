// stores/user.ts
import { defineStore } from 'pinia'
import type { PagingResponse } from '~/plugins/api'

export interface User {
  id: string
  name: string
  email: string
  role: string
  created_at: string
  updated_at: string
  deleted_at: string | null
}

interface CreateUserPayload {
  name: string
  email: string
  password: string
  role: string
}

export const useUserStore = defineStore('user', () => {
  const { $api } = useNuxtApp()
  const users = ref<User[]>([])
  const total = ref(0)
  const page = ref(1)
  const page_size = ref(10)
  const sort = ref<'asc' | 'desc'>('desc')

  const create = async (payload: CreateUserPayload) => {
    return await $api<User>('/admin/users/', {
      method: 'POST',
      body: payload,
    })
  }

  const getMany = async () => {
    const data = await $api<PagingResponse<User>>('/admin/users/', {
      query: { page: page.value, page_size: page_size.value, sort: sort.value },
    })
    users.value = data.items
    total.value = data.total
    page.value = data.page
    page_size.value = data.page_size
    return data
  }

  const setPage = async (p: number) => {
    page.value = p
    await getMany()
  }

  return { users, total, page, page_size, sort, create, getMany, setPage }
})
