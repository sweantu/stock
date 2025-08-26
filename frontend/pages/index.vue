
<script setup lang="ts">
const userComposable = useUser()
const newUser = reactive({
    name: '',
    email: '',
    password: '',
    role: '',
})
const create = async () => {
    await userComposable.create(newUser)
    await userComposable.getMany()
    newUser.name = ''
    newUser.email = ''
    newUser.password = ''
    newUser.role = ''
}

onMounted(() => {
    userComposable.getMany()
})
</script>

<template>
    <div>
        Add user
        <input type="text" v-model="newUser.name" placeholder="Name">
        <input type="text" v-model="newUser.email" placeholder="Email">
        <input type="password" v-model="newUser.password" placeholder="Password">
        <input type="text" v-model="newUser.role" placeholder="Role">
        <button @click="create">Create</button>
    </div>
    <div>
        <h2 class="text-xl font-bold mb-2">Users</h2>
        <ul>
            <li v-for="user in userComposable.users.value" :key="user.id">
                {{ user.name }} - {{ user.email }} ({{ user.role }})
            </li>
        </ul>

        <p>Total: {{ userComposable.total.value }}</p>
    </div>
</template>