import math
import json
import random

class A2AMessage:
    """Standardized JSON-RPC 2.0 envelope for Agent-to-Agent communication."""
    def __init__(self, sender, receiver, method, params):
        self.envelope = {
            "jsonrpc": "2.0",
            "sender": sender,
            "receiver": receiver,
            "method": method,
            "params": params,
            "id": random.randint(1000, 9999) # Unique session ID
        }

class KovaiMCPServer:
    """
    Mock MCP Server exposing simulation tools.
    In a real solution, this would be a separate process communicating via JSON-RPC.
    """
    @staticmethod
    def calculate_distance(pos1, pos2):
        return math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)

class KovaiOrchestrator:
    """
    Sample Orchestrator hinting at a Multi-Agent Multi-Protocol setup.
    STUDENTS: Replace the heuristic logic below with a proper A2A/MCP collaborative system.
    """
    def __init__(self):
        self.name = "Senior Controller"
        self.mcp = KovaiMCPServer()
        self.drone_targets = {} # drone_id -> order_info (Stateful Dispatch)

    def orchestrate(self, state):
        """
        HEURISTIC BASELINE: 
        A non-agentic router to demonstrate the engine.
        Goal: Provide a working example that students must evolve into an 'AI Brain'.
        """
        actions = {}
        drones = state['drones']
        pending_orders = state['pending_orders']

        # Simple Dispatch Logic
        for drone_id, info in drones.items():
            if info['status'] == "CRASHED":
                continue

            # 1. STRATEGIST PHASE: Match Idle Drones at Hub to Orders
            if info['status'] == "IDLE" and info['pos'] == (0, 0) and info['load'] == 0:
                for order in pending_orders:
                    # Check if another drone is already targeting this order
                    is_targeted = any(t['id'] == order['id'] for t in self.drone_targets.values() if t)
                    if not is_targeted and order['mass'] <= info['capacity']:
                        actions[drone_id] = {"action": "PICKUP", "params": {"order_id": order['id']}}
                        self.drone_targets[drone_id] = order
                        print(f"📡 [Strategist] A2A: Dispatching {drone_id} for Order {order['id']}")
                        break
            
            # 2. DISPATCHER PHASE: Manage In-Flight Logistics
            elif info['load'] > 0:
                target_order = self.drone_targets.get(drone_id)
                if target_order:
                    dest = target_order['destination']
                    dist = self.mcp.calculate_distance(info['pos'], dest)
                    
                    if dist < 0.1: # Arrived
                        actions[drone_id] = {"action": "DELIVER", "params": {}}
                    else:
                        actions[drone_id] = {"action": "MOVE", "params": {"target": dest}}
            
            # 3. AUDITOR PHASE: Energy Management (Return to Hub)
            elif info['load'] == 0 and info['pos'] != (0, 0) and info['status'] == "IDLE":
                 # Simple rule: Always return to (0,0) after delivery
                 actions[drone_id] = {"action": "MOVE", "params": {"target": (0,0)}}
                 
        return actions

class KovaiAgent:
    def __init__(self):
        self.orchestrator = KovaiOrchestrator()
        self.name = self.orchestrator.name

    def decide(self, state):
        return self.orchestrator.orchestrate(state)
