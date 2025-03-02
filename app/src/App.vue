<template>
  <Suspense>
    <template #default>
      <div class="flex items-center justify-center h-screen w-full">
        <!-- Use flex-grow to make the Dashboard take all available space -->
        <Dashboard class="flex-grow" />
      </div>
    </template>
    <template #fallback>
      <div class="flex items-center justify-center h-screen w-full">
        <div class="spinner">Loading...</div>
      </div>
    </template>
  </Suspense>
</template>

<script setup>
import Dashboard from "./components/Dashboard.vue";
</script>
