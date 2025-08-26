// composables/useUser.ts
import { storeToRefs } from 'pinia'

export function useUser() {
  const userStore = useUserStore()
  const { users, total, page, page_size } = storeToRefs(userStore)

  return {
    users,
    total,
    page,
    page_size,
    getMany: userStore.getMany,
    create: userStore.create,
  }
}
