import { createClient } from "genlayer-js";
import { simulator } from "genlayer-js/chains";

class OpenSourceProjectFunding {
  contractAddress;
  client;
  
  constructor(contractAddress, account = null, studioUrl = null) {
    this.contractAddress = contractAddress;
    const config = {
      chain: simulator,
      ...(account ? { account } : {}),
      ...(studioUrl ? { endpoint: studioUrl } : {}),
    };
    this.client = createClient(config);
  }
  
  updateAccount(account) {
    this.client = createClient({ chain: simulator, account });
  }
  
  async getProjects() {
    const projects = await this.client.readContract({
      address: this.contractAddress,
      functionName: "get_projects",
      args: [],
    });
    return Array.from(projects.entries()).flatMap(([owner, project]) => {
      return Array.from(project.entries()).map(([id, projectData]) => {
        const projectObj = Array.from(projectData.entries()).reduce((obj, [key, value]) => {
          obj[key] = value;
          return obj;
        }, {});
        return {
          id,
          ...projectObj,
          owner,
        };
      });
    });
  }

  async submitProject(projectName, projectDescription, projectRepoURL) {
    const txHash = await this.client.writeContract({
      address: this.contractAddress,
      functionName: "submit_project",
      args: [projectName, projectDescription, projectRepoURL],
    });
    const receipt = await this.client.waitForTransactionReceipt({
      hash: txHash,
      status: "FINALIZED",
      interval: 10000,
    });
    return receipt;
  }
  
  async rankProject(projectId) {
    const txHash = await this.client.writeContract({
      address: this.contractAddress,
      functionName: "rank_project",
      args: [projectId],
    });
    const receipt = await this.client.waitForTransactionReceipt({
      hash: txHash,
      status: "FINALIZED",
      interval: 10000,
      retries: 20,
    });
    return receipt;
  }
}

export default OpenSourceProjectFunding;
