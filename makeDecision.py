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
print("The decision tree at timestamp", dt_timestamp, "is the following:")
print(decision_tree)

context = {
  "timezone": "+02:00",
  "timeOfDay": 7.25,
  "peopleCount": 2
}
resp = client.decide(decision_tree, context)
print("The anticipated lightbulb state is:", resp["output"]["lightbulbState"]["predicted_value"])