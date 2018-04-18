"""
The agent has acquired a context history, we can now compute a decision tree from it! A decision tree models the output, allowing us to estimate what the output would be in a given context.

The decision tree is computed at a given timestamp, which means it will consider the context history from the creation of this agent up to this moment. Let’s first try to compute the decision tree at midnight on July 26, 2016.

"""

agent_id = "my_first_agent"

client.delete_agent(agent_id)
print("Agent", agent_id, "no longer exists")

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

dt_timestamp = 1469476800
decision_tree = client.get_decision_tree(agent_id, dt_timestamp)
print("The full decision tree at timestamp", dt_timestamp, "is the following:")
print(decision_tree)