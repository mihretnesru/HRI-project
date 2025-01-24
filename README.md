# 🤖 Technical Literacy Adaption in Robots

This project explores **adaptive communication in social robots** to enhance user engagement and task performance. By tailoring robot interactions to users’ **technical literacy levels** (low, medium, high), this system demonstrates the potential of personalized communication strategies in improving **human-robot interaction (HRI)**. 

---

## 📝 Overview

Social robots are becoming increasingly integrated into various domains, such as healthcare, education, and entertainment. However, differences in **technical literacy** among users often create barriers to effective interaction. This project investigates whether **adaptive robot communication**, tailored to technical proficiency, can improve user satisfaction, task efficiency, and engagement.

By categorizing participants into literacy levels using pre-interaction questionnaires and tailoring responses to those levels, the system provides:
- **Simplified instructions** for low-literacy users.
- **Balanced guidance** for medium-literacy users.
- **Concise and technical responses** for high-literacy users.

---

## ✨ Key Features

1. **Personalized Robot Communication**:
   - Tailored responses based on users’ technical literacy.
   - Dynamically adjusted instructions during task execution.

2. **Adaptive Tasks**:
   - Installation of Python development environments.
   - Guided coding tasks with progressive difficulty.
   - Context-specific guidance adapted to user proficiency.

3. **Wizard of Oz Methodology**:
   - Simulates advanced robotic autonomy using external control.
   - Real-time responses generated through OpenAI’s **ChatGPT-4.0**.

4. **Data-Driven Insights**:
   - Empirical evaluation of task completion time, satisfaction, and engagement across adaptive and non-adaptive scenarios.

---

## 🔧 System Architecture

### Hardware
- **Boston Dynamics Spot Robot**: Main robotic platform.
- **NVIDIA GeForce RTX 4090**: GPU for processing.
- **Microphone & Bluetooth Speaker**: Captures user input and delivers speech output.

### Software
- **Python 3.12**: Programming language for interaction scripts.
- **OpenAI Whisper**: Converts speech input to text.
- **OpenAI ChatGPT-4.0**: Generates tailored responses based on user literacy.
- **Google Text-to-Speech (TTS)**: Produces natural-sounding speech for output.

---

## 📋 Experimental Design

### Conditions
1. **Condition A** (Adaptive Communication):
   - Robot tailors responses based on technical literacy levels (low, medium, high).

2. **Condition B** (Non-Adaptive Communication):
   - Robot delivers standardized responses, ignoring literacy levels.

### Tasks
1. **Install Anaconda**: Download and install the Python environment.
2. **Create a Python Environment**: Configure a new development environment.
3. **Launch Jupyter Notebook**: Set up and navigate a workspace.
4. **Simple Coding Task**: Write and execute a Python script to add two numbers.

### Participants
- **12 Participants**:
  - Balanced across literacy levels (low, medium, high).
  - Equal representation in adaptive and non-adaptive conditions.

---

## 📊 Results

### Key Findings
1. **Task Completion Time**:
   - Adaptive communication reduced task completion time significantly.
   - Higher technical literacy led to faster task completion.

2. **User Satisfaction**:
   - Participants preferred adaptive interactions, reporting higher satisfaction in Condition A.
   - Literacy level did not significantly affect satisfaction when adaptation was applied.

3. **User Engagement**:
   - Marginal improvement in engagement with adaptive communication, though not statistically significant.

 
