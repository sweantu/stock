// composables/useUser.js
import { ref } from 'vue'
import { getUsers, createUser } from '@/services/user'

export function useUser() {
  const users = ref([])

  const fetchUsers = async () => {
    const { data } = await getUsers()
    users.value = data.items
  }

  const addUser = async (newUser) => {
    await createUser(newUser)
    await fetchUsers()
  }

  return { users, fetchUsers, addUser }
}
