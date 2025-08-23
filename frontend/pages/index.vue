<script setup lang="ts">

const counter = useCounter()
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