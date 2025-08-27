<script setup>
import { onMounted } from "vue";
import { useUser } from "@/composables/useUser";

const userCompo = useUser();

onMounted(() => {
  userCompo.getMany();
});

const newUser = { name: "Alice3", email: "alice3@example.com", role: "admin", password: "123456" };

const handleAddUser = () => {
  userCompo.create(newUser);
};
</script>

<template>
  <div>
    <h2>User List</h2>
    <ul>
      <li v-for="u in userCompo.users.value" :key="u.id">{{ u.name }} {{ u.email }} ({{ u.role }}) </li>
    </ul>
    <button @click="handleAddUser">Add User</button>
  </div>
</template>

