<template>
  <div class="fixed inset-0 bg-gray-600 bg-opacity-75 overflow-y-auto h-full w-full flex items-center justify-center">
    <div class="relative p-5 border w-96 shadow-lg rounded-md bg-white">
      <h3 class="text-lg font-medium leading-6 text-gray-900 mb-2">Submit Project</h3>
      <div class="mb-4">
        <input
          :value="projectName"
          @input="$emit('update:projectName', $event.target.value)"
          class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 mb-2"
          placeholder="Project Name"
        />
        <input
          :value="projectDescription"
          @input="$emit('update:projectDescription', $event.target.value)"
          class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 mb-2"
          placeholder="Description"
        />
        <input
          :value="projectRepoURL"
          @input="$emit('update:projectRepoURL', $event.target.value)"
          class="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 mb-2"
          placeholder="Repository URL"
        />
      </div>
      <div class="mt-4">
        <div v-if="!submittingProject">
          <button
            @click="submitProject"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mr-2"
          >
            Create
          </button>
          <button
            @click="$emit('close')"
            class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded"
          >
            Cancel
          </button>
        </div>
        <div v-else>
          <div class="spinner">Creating...</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
  projectName: String,
  projectDescription: String,
  projectRepoURL: String
});

const submittingProject = ref(false);

const emit = defineEmits(['close', 'submit', 'update:projectName', 'update:projectDescription', 'update:projectRepoURL']);

const submitProject = () => {
  if (
    props.projectName &&
    props.projectDescription &&
    props.projectRepoURL
  ) {
    submittingProject.value = true
    emit('submit')
  }
}

</script>
