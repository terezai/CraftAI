"""
craft ai is based on the concept of agents. In most use cases, one agent is created per user or per device.

An agent is an independent module that stores the history of the context of its user or device’s context, and learns which decision to take based on the evolution of this context in the form of a decision tree.

In this example, we will create an agent that learns the decision model of a light bulb based on the time of the day and the number of people in the room. In practice, it means the agent’s context have 4 properties:

peopleCount which is a continuous property,
timeOfDay which is a time_of_day property,
timezone, a property of type timezone needed to generate proper values for timeOfDay (cf. the context properties type section for further information),
and finally lightbulbState which is an enum property that is also the output.
"""

import craftai


agent_id = "my_first_agent"
configuration = {
  "context": {
    "peopleCount": {
      "type": "continuous"
    },
    "timeOfDay": {
      "type": "time_of_day"
    },
    "timezone": {
      "type": "timezone"
    },
    "lightbulbState": {
      "type": "enum"
    }
  },
  "output": ["lightbulbState"]
}

agent = client.create_agent(configuration, agent_id)
print("Agent", agent["id"], "has successfully been created")





