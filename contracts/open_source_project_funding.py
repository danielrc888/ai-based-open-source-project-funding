# { "Depends": "py-genlayer:test" }

import json
from dataclasses import dataclass
from genlayer import *

@dataclass
class Project:
    id: str
    name: str
    description: str
    repository_url: str
    reasoning: str
    has_ranked: bool
    score: u256

@gl.contract
class OpenSourceFunding:
    projects: TreeMap[Address, TreeMap[str, Project]]

    def __init__(self):
        pass
    
    def _check_project(self, repository_url: str, project_name: str, project_description: str) -> dict:
        def get_project_data() -> str:
            web_data = gl.get_webpage(repository_url, mode="text")

            task =f"""
Analyze this project's impact and contribution

Project Name: {project_name}
Project Description: {project_description}

Web content:
{web_data}

Key Metrics: [number of contributors, code quality, issue resolution rate]
Output 

Respond in JSON:
{{
    "score": int, // a score between 0 and 100 based on its sustainability and impact.
    "reasoning": str // the reasoning why the project is receiving that score
}}

It is mandatory that you respond only using the JSON format above,
nothing else. Don't include any other words or characters,
your output must be only JSON without any formatting prefix or suffix.
This result should be perfectly parsable by a JSON parser without errors.
        """
            result = gl.exec_prompt(task).replace("```json", "").replace("```", "")
            return json.dumps(json.loads(result), sort_keys=True)
        result_json = json.loads(
            gl.eq_principle_prompt_comparative(
                get_project_data, 
                "The score result must not differ more than 5 %"
            )
        )
        return result_json


    @gl.public.view
    def get_projects(self) -> dict:
        return {k.as_hex: v for k, v in self.projects.items()}
    
    @gl.public.write
    def submit_project(
        self,
        name: str,
        description: str,
        repository_url: str,
    ) -> None:
        sender_address = gl.message.sender_account
        project_id = name.lower()
        project = Project(
            id=project_id,
            name=name,
            description=description,
            repository_url=repository_url,
            reasoning="",
            has_ranked=False,
            score=0
        )
        self.projects.get_or_insert_default(sender_address)[project_id] = project

    @gl.public.write
    def rank_project(self, project_id: str) -> None:
        if self.projects[gl.message.sender_account][project_id].has_ranked:
            raise Exception("Project already ranked")
        project = self.projects[gl.message.sender_account][project_id]
        project_status = self._check_project(project.repository_url, project.name, project.description)
        project.reasoning = project_status.get("reasoning", "")
        project.score = project_status.get("score", 0)
        project.has_ranked = True