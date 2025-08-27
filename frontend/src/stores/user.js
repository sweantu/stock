import { defineStore } from 'pinia'
import { ref } from 'vue'
import * as userService from '@/services/user'

export const useUserStore = defineStore('user', () => {
  const users = ref([])

  const getMany = async () => {
    const { data } = await userService.getMany()
    users.value = data.items
  }

  const create = async (newUser) => {
    await userService.create(newUser)
    await getMany()
  }

  return { users, getMany, create }
})
