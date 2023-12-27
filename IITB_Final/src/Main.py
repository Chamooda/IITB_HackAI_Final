#Importing necessary libraries
from uagents.setup import fund_agent_if_low
from uagents import Agent, Bureau, Context, Model

#Importing agents from python modules
from Agents.Alice import alice
from Agents.Converter import Converter

#Adding agents in an object of class Bureau
bureau = Bureau()
bureau.add(alice)
bureau.add(Converter)

#Adding agents in an object of class Bureau
bureau.run()
