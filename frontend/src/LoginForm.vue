<script setup lang="ts">
import { ref } from "vue"

interface LoginForm {
  email: string
  password: string
}

const form = ref<LoginForm>({
  email: "",
  password: "",
})

const loading = ref(false)
const error = ref<string | null>(null)

const handleSubmit = async () => {
  error.value = null
  loading.value = true

  try {
    // Example API call
    await new Promise((resolve) => setTimeout(resolve, 1000)) // mock delay
    console.log("Logging in with:", form.value)
    // Replace with actual API call, e.g.:
    // await axios.post("/api/login", form.value)

  } catch (err) {
    console.error("Login error:", err)
    error.value = "Login failed. Please try again."
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="flex min-h-screen items-center justify-center bg-gray-100">
    <div class="w-full max-w-md rounded-2xl bg-white p-8 shadow-lg">
      <h2 class="mb-6 text-center text-2xl font-bold text-gray-800">
        Login
      </h2>

      <form @submit.prevent="handleSubmit" class="space-y-5">
        <!-- Email -->
        <div>
          <label for="email" class="mb-1 block text-sm font-medium text-gray-700">
            Email
          </label>
          <input id="email" type="email" v-model="form.email" required
            class="w-full rounded-xl border border-gray-300 p-3 text-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" />
        </div>

        <!-- Password -->
        <div>
          <label for="password" class="mb-1 block text-sm font-medium text-gray-700">
            Password
          </label>
          <input id="password" type="password" v-model="form.password" required
            class="w-full rounded-xl border border-gray-300 p-3 text-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50" />
        </div>

        <!-- Error message -->
        <p v-if="error" class="text-sm text-red-600">
          {{ error }}
        </p>

        <!-- Submit button -->
        <button type="submit" :disabled="loading"
          class="w-full rounded-xl bg-indigo-600 px-4 py-3 text-white font-semibold transition hover:bg-indigo-700 disabled:opacity-50">
          <span v-if="loading">Logging in...</span>
          <span v-else>Login</span>
        </button>
      </form>
    </div>
  </div>
</template>
