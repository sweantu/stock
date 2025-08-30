<script setup lang="ts">
import { useCounter } from '@/composables/useCounter';

const { count, increment } = useCounter();
</script>

<template>
  <h1 class="text-3xl font-bold underline text-blue-500">You did it!</h1>
  <p>
    Visit <a href="https://vuejs.org/" target="_blank" rel="noopener">vuejs.org</a> to read the
    documentation
  </p>
  <button @click="increment">Count: {{ count }}</button>
</template>
