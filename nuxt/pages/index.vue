<!-- pages/index.vue -->
<script setup lang="ts">
import type { TableColumn } from '@nuxt/ui'
const userComposable = useUser()

const newUser = reactive({
    name: '',
    email: '',
    password: '',
    role: '',
})

const create = async () => {
    await userComposable.create(newUser)
    Object.assign(newUser, { name: '', email: '', password: '', role: '' })
}

onMounted(() => {
    userComposable.getMany()
})

const columns: TableColumn<User>[] = [
    {
        accessorKey: 'id',
        header: '#'

    },
    {
        accessorKey: 'name',
        header: 'Name',
        cell: ({ row }) => `@@${row.getValue('name')}`
    },
    {
        accessorKey: 'email',
        header: 'Email',
    },
    {
        accessorKey: 'role',
        header: 'Role',
    },
]

</script>

<template>
    <div>
        <h2>Add user</h2>
        <input v-model="newUser.name" placeholder="Name" />
        <input type="email" v-model="newUser.email" placeholder="Email" />
        <input type="password" v-model="newUser.password" placeholder="Password" />
        <input v-model="newUser.role" placeholder="Role" />
        <button :disabled="userComposable.loading.value" @click="create">
            {{ userComposable.loading.value ? 'Creating...' : 'Create' }}
        </button>
        <p v-if="userComposable.error" class="text-red-500">{{ userComposable.error }}</p>
    </div>

    <div>
        <h2 class="text-xl font-bold mb-2">Users</h2>
        <UTable :data="userComposable.users.value" :columns="columns" class="flex-1" />
        <p>Total: {{ userComposable.total.value }}</p>
    </div>
</template>