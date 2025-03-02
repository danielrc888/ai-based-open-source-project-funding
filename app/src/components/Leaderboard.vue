<template>
  <div class="bg-white shadow overflow-hidden sm:rounded-lg">
    <div class="px-4 py-5 sm:px-6">
      <h2 class="text-lg leading-6 font-medium text-gray-900">Leaderboard</h2>
    </div>
    <div class="border-t border-gray-200">
      <table class="min-w-full divide-y divide-gray-200">
        <thead class="bg-gray-50">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Score</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Project Name</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Repo Link</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="project in sortedLeaderboard" :key="project.id">
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ project.score }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500"><Address :address="project.name" /></td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ project.repository_url }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import Address from './Address.vue';

const props = defineProps({
  leaderboard: Array,
});

const sortedLeaderboard = computed(() => {
  const leaderboard = props.leaderboard
  if (!leaderboard) { return [] }
  return [...leaderboard].sort((a, b) => Number(b.score) - Number(a.score)); // use spread to avoid mutating the prop
});
</script>
