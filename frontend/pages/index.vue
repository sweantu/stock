<script setup lang="ts">
import { useCounterStore } from '~/stores/counter'

const counter = useCounterStore()
</script>

<template>
    <UContainer>
        <UCard>
            <UButton @click="counter.increment">
                Count: {{ counter.count }}
            </UButton>
        </UCard>
    </UContainer>
</template>