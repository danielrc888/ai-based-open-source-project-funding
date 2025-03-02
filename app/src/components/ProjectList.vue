<template>
  <div class="bg-white shadow overflow-hidden sm:rounded-lg">
    <div class="px-4 py-5 sm:px-6 flex justify-between items-center">
      <h2 class="text-lg leading-6 font-medium text-gray-900">Projects</h2>
      <button
        @click="$emit('openCreateModal')"
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded text-sm"
      >
        Submit Project
      </button>
    </div>
    <div class="border-t border-gray-200">
      <!-- Wrap the table in a div that allows horizontal scrolling -->
      <div class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">User</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Project</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Description</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Repository URL</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Score</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Reason</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Action</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="project in projects" :key="project.id">
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900"><Address :address="project.owner" /></td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ project.name }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ project.description }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ project.repository_url }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ project.score }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                <span :class="project.has_ranked ? 'text-green-600' : 'text-yellow-600'">
                  {{ project.has_ranked ? 'Ranked' : 'Unranked' }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                <button
                  v-if="project.has_ranked"
                  @click="$emit('showReasoning', project)"
                  class="text-indigo-600 hover:text-indigo-900"
                >
                  Show Reasoning
                </button>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                <button
                  v-if="project.owner === userAddress && !project.has_ranked"
                  :disabled="rankingProject"
                  @click="$emit('rankProject', project.id)"
                  class="text-indigo-600 hover:text-indigo-900"
                >
                  Rank
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>


<script setup>
import Address from './Address.vue';

const props = defineProps({
  projects: Array,
  userAddress: String,
  rankingProject: Boolean,
});

</script>
