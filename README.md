# 🛸 KovaiDelivery: The Autonomous Logistics Multi-Agent Challenge

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/genorai-tech/kovai-delivery-hackathon)

Welcome to **KovaiDelivery**. This isn't just a coding task; it’s an engineering challenge to build a robust, multi-agent system capable of managing a city-scale autonomous delivery fleet.

---

## 🧠 The Engineering Challenge
The core problem: **"In a city with 200+ pending orders and unpredictable weather, how do we maximize delivery throughput while minimizing the energy footprint of 100+ drones?"**

Your system must handle:
1. **Strategic Planning**: Parse unstructured orders and determine the optimal sequence of deliveries.
2. **Dynamic Adaptation**: Respond to real-time disruptions like STORMY weather or low battery levels.
3. **Multi-Step Execution**: Generate and validate complex chains of actions (Maneuver -> Pickup -> Deliver -> Charge).

---

## 🏗 Multi-Agent Architecture
You are expected to design a team of specialized AI agents that collaborate using the **A2A (Agent-to-Agent)** communication pattern:

- **The Order Analyst**: Parses unstructured text orders, extracts mass/destination, and handles priority queueing.
- **The Resource Allocator**: Matches the optimal drone spec (Speedster vs. Heavy) to the order mass and distance (The "Optimizer").
- **The Tactical Dispatcher**: Manages the stateful mission lifecycle for each drone (MOVE -> PICKUP -> DELIVER).
- **The Safety Auditor**: A specialized "Energy Watchdog" that validates flight plans against real-time weather to prevent battery crashes.

---

## 🛠 Tech Stack & Protocols (Required)
Your solution must implement the following industry standards:

### 1. Model Context Protocol (MCP)
Build an **MCP Server** to expose your logistics data and the simulation engine to your agents. This allows your agents to "query" the world state and "probe" battery usage tools dynamically.

### 2. A2A Protocol
Ensure your agents communicate using a standardized JSON-RPC envelope. Every hand-off (e.g., Strategist to Dispatcher) must be a formal negotiation.

### 3. PydanticAI (Recommended)
We recommend using **PydanticAI** for building type-safe, reliable agentic flows that validate state transitions at every step.

---

## � The Sandbox (Datasets)
We provide you with real-world logistics data in `data/`:
- **Fleet Matrix**: 100+ drones with specific capacity, speed, and discharge metrics.
- **Order Stream**: 200+ customer requests with varied mass and delivery coordinates.
- **Weather Logs**: Tick-by-tick environmental conditions.

---

## ⚡ Quick Start
1. **Install**: `pip install -r requirements.txt`
2. **Explore**: Look at `src/simulation/kovai_engine.py` to understand the world logic.
3. **Build**: Open `src/agent/my_agent.py`. A functional **Heuristic Baseline** is provided so you can see the engine in action. Your task is to replace this with a Multi-Agent Multi-Protocol system.

## 👨‍⚖️ Judging Criteria
- **Architecture Maturity**: How well did you use A2A and MCP?
- **Efficiency Score**: (Total Distance / Total Battery Used).
- **Service Level**: Percentage of orders fulfilled.
- **Validation**: Did your Auditor prevent any drone crashes?

---

## 🎯 Scoring & Goal
Minimize **Cost** while maximizing **Speed**.
- **Efficiency Score**: (Total Distance / Total Battery Used) - *Higher is better!*
- **Service Level**: Percentage of delivered orders.
- **Reliability**: Don't let your drones crash (0% battery)!

