import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel
# import pdfplumber
import json
from typing import List


load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api error")

client=Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"    # Fast Llama model
role="user"

job_description="""
Description
Are you passionate about building scalable software and solving real-world problems using modern technologies? Do you enjoy working in a collaborative engineering environment where your code has a meaningful impact? We are looking for Software Development Engineers who are eager to learn, innovate, and grow while developing enterprise-grade applications.

As a Software Development Engineer, you will work on designing, developing, and maintaining high-quality software solutions using Java and modern backend technologies. You will collaborate with cross-functional teams, participate in the complete software development lifecycle, and contribute to building reliable and scalable applications.

Key Job Responsibilities

• Design, develop, and maintain scalable backend applications using Java, Spring Boot, and Hibernate.
• Build and consume RESTful APIs and develop applications using microservices architecture.
• Develop responsive web applications using HTML5, CSS3, and modern JavaScript frameworks.
• Write clean, maintainable, and reusable code following object-oriented design principles and design patterns.
• Participate in code reviews and contribute to technical documentation and software design discussions.
• Collaborate with team members in an Agile development environment.
• Use Git for version control and participate in CI/CD pipelines for automated deployment.
• Develop, test, debug, and optimize applications for performance and reliability.
• Work with cloud platforms and containerized applications using Docker and Kubernetes.
• Continuously learn and adopt new technologies and engineering best practices.

Basic Qualifications

- Bachelor's degree in Computer Science, Software Engineering, or a related technical field.
- No prior software development experience is required.
- Strong programming skills in Java, Spring Framework/Spring Boot, and Hibernate.
- Knowledge of Object-Oriented Programming (OOP), data structures, and design patterns.
- Familiarity with HTML5, CSS3, JavaScript, and modern frontend frameworks.
- Understanding of RESTful APIs and microservices architecture.
- Experience with Git and basic CI/CD concepts.
- Basic understanding of Agile software development methodologies.

Preferred Qualifications

- Knowledge of cloud platforms such as AWS or Azure.
- Experience with Docker and Kubernetes for containerized applications.
- Familiarity with automated testing and Test-Driven Development (TDD).
- Strong analytical and problem-solving skills.
- Excellent written and verbal communication skills.
- Ability to work effectively in a collaborative team environment.
- Demonstrated commitment to continuous learning, innovation, and technical documentation.
"""


# ------------------------------------Pydantic Models------------------------------------------------

class JobD(BaseModel):
    role: str
    required_skills: list[str]
    preferred_skills: list[str]
    minimum_experience: float | None
    education_requirements: list[str]
    responsibilities: list[str]

jobd_schema = JobD.model_json_schema()




system_prompt=f""" You are an expert HR assistant.
Your job is to analyze job descriptions and extract
structured information from them.
Return ONLY valid JSON matching this schema:
{jobd_schema}
IMPORTANT:
Do NOT return the schema itself.
Do NOT return fields like "properties", "title" or "type".
Fill the schema with actual information extracted from the job description.
If minimum experience is not mentioned, return null.
If information for a list is missing, return an empty list.
Do not invent information.
"""

message_system={
    "role":"system",
    "content":system_prompt

}


user_prompt=f"""Analyze the following job description
{job_description}
"""


message_system={
    "role":"system",
    "content":system_prompt
}

message_user={
    "role":role,
    "content":user_prompt
}
response_format={
    "type":"json_object"
}

messages=[message_system,message_user]


response=client.chat.completions.create(model=model,messages=messages,response_format=response_format)
ans = response.choices[0].message.content


# How to read JSON DAT

raw_json=ans
data_file=json.loads(raw_json)
resu=JobD(**data_file)

print(resu.minimum_experience)
print(resu.education_requirements)

