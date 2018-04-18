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




"""
We have now created our first agent but it is not able to do much, yet. To learn a decision model it needs to be provided with data, in craft ai these are called context operations.

In the following we add 8 operations:

The initial one sets the initial state of the agent, on July 25 2016 at 5:30, in Paris, nobody is there and the light is off;
At 7:02, someone enters the room the light is turned on;
At 7:15, someone else enters the room;
At 7:31, the light is turned off;
At 8:12, everyone leaves the room;
At 19:23, 2 persons enter the room;
At 22:35, the light is turned on;
At 23:06, everyone leaves the room and the light is turned off.
"""

context_list = [
  {
    "timestamp": 1469410200,
    "context": {
      "timezone": "+02:00",
      "peopleCount": 0,
      "lightbulbState": "OFF"
    }
  },
  {
    "timestamp": 1469415720,
    "context": {
      "peopleCount": 1,
      "lightbulbState": "ON"
    }
  },
  {
    "timestamp": 1469416500,
    "context": {
      "peopleCount": 2
    }
  },
  {
    "timestamp": 1469417460,
    "context": {
      "lightbulbState": "OFF"
    }
  },
  {
    "timestamp": 1469419920,
    "context": {
      "peopleCount": 0
    }
  },
  {
    "timestamp": 1469460180,
    "context": {
      "peopleCount": 2
    }
  },
  {
    "timestamp": 1469471700,
    "context": {
      "lightbulbState": "ON"
    }
  },
  {
    "timestamp": 1469473560,
    "context": {
      "peopleCount": 0,
      "lightbulbState": "OFF"
    }
  }
]
client.add_operations(agent_id, context_list)
print("Successfully added initial operations to agent", agent_id, "!")
