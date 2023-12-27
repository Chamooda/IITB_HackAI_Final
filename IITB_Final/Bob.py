from uagents.setup import fund_agent_if_low
from uagents import Agent, Bureau, Context, Model
import json

bob = Agent(
    name = "Bob",
    port = 8000,
    seed = "Radhika_Desai",
    endpoint=["http://127.0.0.1:8000/c"],
)


fund_agent_if_low(bob.wallet.address())

@bob.on_interval(period = 1.0)
async def Add(ctx: Context):
    title = input("Enter a new job title: ")
    description = input("Enter a new job description: ")
    file_path = 'Jobs.json'
    Job_Queries = {}

    with open(file_path, 'r') as file:
            Job_Queries = json.load(file)
            print(type(Job_Queries))
            Job_Queries[title] = description
            Updated_Job_Queries = json.dumps(Job_Queries, indent=2)

    with open(file_path, 'w') as file:
        file.write(Updated_Job_Queries)



    # # Iterate through jobs
    # for job_title, job_details in data["jobs"].items():
    #     print(f"Job Title: {job_title}")
    #     print(f"Total Experience Required: {job_details['total_experience_required']}")
    #     print(f"Primary Skills Required: {', '.join(job_details['primary_skills_required'])}")
    #     print(f"Degree Required: {job_details['degree_required']}")
    #     print("\n" + "="*30 + "\n")


if __name__ == "__main__":
    bob.run()
