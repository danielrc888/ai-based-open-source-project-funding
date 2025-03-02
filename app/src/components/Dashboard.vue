<template>
  <div class="min-h-screen bg-gray-100 text-gray-900">
    <header class="bg-white shadow flex justify-between">
      <div class="max-w-7xl py-6 px-4 sm:px-6 lg:px-8">
        <h1 class="text-3xl font-bold text-gray-900">GenLayer Open Source Project Funding</h1>
      </div>
      <div class="max-w-7xl py-6 px-4 sm:px-6 lg:px-8 text-right">
        <div v-if="!userAddress">
          <button
            @click="createUserAccount"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          >
            Create Account
          </button>
        </div>
        <div v-else>
          <p class="text-lg">Your address: <Address :address="userAddress" /></p>
          <p class="text-lg">Your points: {{ userPoints }}</p>
          <button
            @click="disconnectUserAccount"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          >
            Disconnect
          </button>
        </div>
      </div>
    </header>

    <main class="mx-auto py-6 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- Projects List -->
        <div class="col-span-1 md:col-span-2 lg:col-span-2">
          <ProjectList
            :projects="projects"
            :userAddress="userAddress"
            :rankingProject="rankingProject"
            @openCreateModal="openCreateModal"
            @rankProject="rankProject"
            @showReasoning="showReasoning"
          />
        </div>

        <!-- Leaderboard -->
        <div class="col-span-1 md:col-span-2 lg:col-span-1">
          <Leaderboard :leaderboard="projects" />
        </div>
      </div>

      <!-- Submit Project Modal -->
      <ProjectForm
        v-if="showSubmitModal"
        :projectName="projectName"
        :projectDescription="projectDescription"
        :projectRepoURL="projectRepoURL"
        @update:projectName="projectName = $event"
        @update:projectDescription="projectDescription = $event"
        @update:projectRepoURL="projectRepoURL = $event"
        @submit="submitProject"
        @close="showSubmitModal = false"
      />
      <!-- Show Reasoning Modal-->
      <Modal v-if="showReasoningModal && selectedProject" @close="showReasoningModal = false">
        <template #title>{{ selectedProject.name }}</template>
        <template #body>
          <p>Score: {{ selectedProject.score }}</p>
          <p>{{ selectedProject.reasoning }}</p>
        </template>
      </Modal>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { account, createAccount, removeAccount } from "../services/genlayer";
import OpenSourceProjectFunding from "../logic/OpenSourceProjectFunding";
import Address from "./Address.vue";
import ProjectList from "./ProjectList.vue";
import Leaderboard from "./Leaderboard.vue";
import Modal from "./Modal.vue";
import ProjectForm from "./ProjectForm.vue";

// State
const projectName = ref("");
const projectDescription = ref("");
const projectRepoURL = ref("");
const rankingProject = ref(false);
const contractAddress = import.meta.env.VITE_CONTRACT_ADDRESS;
const studioUrl = import.meta.env.VITE_STUDIO_URL;
const openSourceProjectFunding = new OpenSourceProjectFunding(contractAddress, account, studioUrl);
const userAccount = ref(account);
const userPoints = ref(0);
const userAddress = computed(() => userAccount.value?.address);
const projects = ref([]);
const showSubmitModal = ref(false);
const showReasoningModal = ref(false);
const selectedProject = ref(null);

// Methods
const createUserAccount = async () => {
  userAccount.value = createAccount();
  openSourceProjectFunding.updateAccount(userAccount.value);  
  userPoints.value = 0;
};

const disconnectUserAccount = async () => {
  userAccount.value = null;
  removeAccount();
  userPoints.value = 0;
};

const openCreateModal = () => {
  showSubmitModal.value = true;
};

const loadProjects = async () => {
  projects.value = await openSourceProjectFunding.getProjects();
};

const rankProject = async (projectId) => {
  rankingProject.value = true;
  await openSourceProjectFunding.rankProject(projectId);
  rankingProject.value = false;
  await loadProjects();
};

const showReasoning = (project) => {
  selectedProject.value = project;
  showReasoningModal.value = true;
};

const submitProject = async () => {
  if (projectName.value && projectDescription.value && projectRepoURL.value) {
    await openSourceProjectFunding.submitProject(
      projectName.value,
      projectDescription.value,
      projectRepoURL.value
    );
    await loadProjects();
    projectName.value = "";
    projectDescription.value = "";
    projectRepoURL.value = "";
    showSubmitModal.value = false;
  }
}

// Initialize with some sample data
onMounted(async () => {
  await loadProjects();
});
</script>
