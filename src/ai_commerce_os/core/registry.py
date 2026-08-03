from ai_commerce_os.core.agent import Agent
from ai_commerce_os.core.exceptions import AgentError


class AgentRegistry:
    """In-memory registry for resolving agents by their identifiers."""

    def __init__(self) -> None:
        self._agents: dict[str, Agent] = {}

    def register_agent(self, agent: Agent) -> None:
        """Register an agent with a unique identifier."""
        if agent.id in self._agents:
            raise AgentError(f"Agent '{agent.id}' is already registered.")
        self._agents[agent.id] = agent

    def get_agent(self, agent_id: str) -> Agent | None:
        """Return a registered agent when its identifier is known."""
        return self._agents.get(agent_id)

    def list_agents(self) -> list[Agent]:
        """Return all registered agents in registration order."""
        return list(self._agents.values())
