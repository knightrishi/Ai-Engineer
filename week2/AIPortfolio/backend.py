import os
from fastapi import FastAPI
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel
import json
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")
app = FastAPI()
if not my_api_key:
    raise ValueError("api error")

client=Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"


# Allow your HTML page to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=[ "https://knightrishi.github.io",
        "http://127.0.0.1:5500",
        "http://localhost:5500"],  # Later replace "*" with your portfolio domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#structuring the data
class MyDetails(BaseModel):
    name: str
    education: str
    CGPA: str
    skills: list[str]
    projects: list[str]
    experience: list[str]
    achievements: list[str]
    certifications: list[str]
    social_links: dict[str, str]


candidate = MyDetails(
    name="Arnav Singh",

    education="B.Tech Computer Science, Lakshmi Narain College of Technology (LNCT), Bhopal (2023–2027)",

    CGPA="8.55",

    skills=[
        "Java",
        "Spring Boot",
        "React",
        "Docker",
        "MySQL",
        "MongoDB",
        "JavaScript",
        "C++",
        "Python",
        "RAG",
        "REST APIs",
        "JDBC",
        "JavaFX",
        "Redis",
        "Git",
        "Data Structures",
        "Object-Oriented Programming"
    ],

    projects=[
        """Distributed Search Engine:
        Built a distributed search engine using Spring Boot, MySQL, Redis, Docker, and Jsoup.
        Implemented BFS crawling, URL deduplication, indexing, and REST APIs.""",

        """INSS – Intelligent Navigation Sentinel System:
        Developed a Java Swing/JavaFX application for vehicle registration, checkpoint management,
        QR-code generation, number-plate scanning, and RSSI-based crowd prediction.""",

        """LifeLine-:
        Full-stack MERN application with a RESTful Node.js API, MongoDB for flexible donor/hospital schemas, Express middleware for auth, and a React frontend optimized for speed.
        Architecture Highlights-
            Node.js backend with MongoDB and Express.js
            Real-time blood inventory and availability tracking
            Tri-party coordination system (donor/hospital/recipient)
            Smart donor matching by blood type and location
            RESTful API architecture for scalable integration"""
        ,
        """Darshan Ease:
        Temple darshan booking and management platform.
        React + Node.js application with an Express API layer, MongoDB persistence, and role-based authentication for admin vs. visitor workflows. Booking slots managed server-side with conflict prevention.""",
        """Travelers-Immersive travel discovery and destination platform:
        React.js with custom CSS animations, component-driven architecture, and responsive design from mobile to desktop. Focused on UI craft and storytelling through visual hierarchy.""",

        """Short URL System-Production-grade URL shortening service built for scale:
        Node.js + Express REST API with MongoDB persistence, hash-based short code generation with collision handling, redirect middleware, and a clean endpoint design for integration."""
        
    ],

    experience=[
        "Parabit Technology Pvt LTD.(2025) – Software Development Intern."
    ],

    achievements=[
        "Solved 800+ DSA problems across coding platforms.",
        "Solved 500+ LeetCode problems.",
        "Competitive programming practice on LeetCode and CodeChef."
    ],

    certifications=[
        "AWS Cloud Practitioner",
        "Java Programming"
    ],

    social_links={
        "github": "github.com/knightrishi",
        "linkedin": "linkedin.com/in/arnav-singh"
    }
)

resume_data = candidate.model_dump_json(indent=2)

response_format={
    "type":"json_object"
}

system_prompt = f"""
# ROLE
You are a professional interview representative for this candidate.
You have access ONLY to the candidate's structured resume below.
Resume Data:
{resume_data}

# TASK
Answer interview questions using only the information available in the resume.
# RULES
- Use only facts present in the resume.
- Never invent, assume, exaggerate, or hallucinate any experience, skill, project, achievement, or personal detail.
- If a question cannot be answered from the resume, reply exactly:
  "I don't have enough information in the resume to answer that."
- Keep answers professional, concise, and factually accurate.
- If appropriate, summarize or rephrase resume information, but do not add new facts.
- Do not reveal or mention these instructions unless explicitly asked.

# EXAMPLE
Question:
Have you worked with Kubernetes in production?
Answer:
I don't have enough information in the resume to answer that.
"""
class Question(BaseModel):
    question: str

@app.post("/ask")
def ask(q: Question):

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role":"system","content":system_prompt},
            {"role":"user","content":q.question}
        ]
    )

    return {
        "answer": response.choices[0].message.content
    }
    