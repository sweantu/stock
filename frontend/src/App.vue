<script setup>
import { onMounted } from "vue";
import { useUser } from "@/composables/useUser";

const { users, fetchUsers, addUser } = useUser();

onMounted(() => {
  fetchUsers();
});

const newUser = { name: "Alice", email: "alice@example.com", role: "admin", password: "123456" };

const handleAddUser = () => {
  addUser(newUser);
};
</script>

<template>
  <div>
    <h2>User List</h2>
    <ul>
      <li v-for="u in users" :key="u.id">{{ u.name }} {{ u.email }} ({{ u.role }}) </li>
    </ul>
    <button @click="handleAddUser">Add User</button>
  </div>
</template>

