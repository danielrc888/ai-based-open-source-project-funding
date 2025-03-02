<template>
  <div class="fixed inset-0 bg-gray-600 bg-opacity-75 overflow-y-auto h-full w-full flex items-center justify-center">
    <div class="relative p-5 border w-96 shadow-lg rounded-md bg-white">
      <h3 class="text-lg font-medium leading-6 text-gray-900 mb-2"><slot name="title"></slot></h3>
      <div class="mb-4"><slot name="body"></slot></div>
      <div class="mt-4">
        <button
          @click="$emit('close')"
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mr-2"
          >
          Aceptar
        </button>
        <button
          @click="$emit('close')"
          class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded"
          >
          Cancel
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>
