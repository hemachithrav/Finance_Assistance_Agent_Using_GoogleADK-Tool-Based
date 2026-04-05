<!-- 🎨 HEADER BANNER -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:4facfe,100:00f2fe&height=220&section=header&text=Finance%20Multi-Agent%20ADK%20Bot&fontSize=38&fontColor=ffffff&animation=fadeIn" />
</p>

<!-- 🏷️ BADGES -->
<p align="center">
  <img src="https://img.shields.io/badge/Google-ADK-blue?style=for-the-badge&logo=google" />
  <img src="https://img.shields.io/badge/LLM-Gemini-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Multi--Agent-AI-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Architecture-Agent--as--Tool-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge&logo=python" />
</p>

---

# 💰 Finance Multi-Agent ADK Bot

An **AI-powered Finance Assistant** built using **Google Agent Development Kit (ADK)** implementing a scalable **Multi-Agent Architecture** with the **Agent-as-a-Tool pattern**.

This project demonstrates **real-world GenAI system design**, including:
- Agent orchestration  
- Tool delegation  
- Real-time data retrieval  
- Modular AI architecture  

---

## 🎥 Demo

<p align="center">
  <img src="assets/00-53-23-ezgif.com-video-to-gif-converter (1).gif" width="700"/>
</p>

<p align="center">
  <img src="assets/00-53-23-ezgif.com-video-to-gif-converter.gif" width="700"/>
</p>


---

## 🚀 Key Features

- 🤖 Multi-Agent AI System  
- 🔗 Agent-as-Tool Pattern using `AgentTool`  
- 🌐 Real-time financial insights using `google_search`  
- 🧾 Personalized finance recommendations  
- 💬 Natural language interaction  
- ⚡ Powered by Gemini (`gemini-2.5-flash`)  
- 🧩 Modular & scalable architecture  

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    A[User Query] --> B[Finance Agent]

    B -->|Finance Data| C[User Finance Tool]

    B -->|Delegation| D[Investment Agent]

    D -->|Search| E[Google Search]

    E --> D
    D --> B
    C --> B

    B --> F[Response]
