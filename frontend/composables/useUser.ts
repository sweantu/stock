// composables/useUser.ts
import { storeToRefs } from 'pinia'

export function useUser() {
  const userStore = useUserStore()
  const { users, total, page, page_size } = storeToRefs(userStore)

  const loading = ref(false)
  const error = ref<string | null>(null)

  const create = async (payload: {
    name: string
    email: string
    password: string
    role: string
  }) => {
    loading.value = true
    error.value = null
    try {
      await userStore.create(payload)
      await userStore.getMany()
    } catch (err: any) {
      error.value = err.message || 'Failed to create user'
    } finally {
      loading.value = false
    }
  }

  const getMany = async () => {
    loading.value = true
    error.value = null
    try {
      await userStore.getMany()
    } catch (err: any) {
      error.value = err.message || 'Failed to fetch users'
    } finally {
      loading.value = false
    }
  }

  return {
    // state from store
    users,
    total,
    page,
    page_size,

    // local states
    loading,
    error,

    // actions
    create,
    getMany,
  }
}