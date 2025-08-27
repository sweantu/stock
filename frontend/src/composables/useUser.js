// composables/useUser.js
import { useUserStore } from '@/stores/user'
import { storeToRefs } from 'pinia'

export function useUser() {
  const userStore = useUserStore()

  const { users } = storeToRefs(userStore)

  const { getMany, create } = userStore

  return { users, getMany, create }
}
