import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, FirecrawlScrapeWebsiteTool

from app.config import settings

breakpoint()
# 1. Initialize Tools
search_tool = SerperDevTool()
scrape_tool = FirecrawlScrapeWebsiteTool()

# 2. Define Agents
researcher = Agent(
    role='E-commerce Product Researcher',
    goal='Find the top 3-4 reputable e-commerce store links for {product_name}',
    backstory="""You are an expert at navigating online retailers. You know how to 
    bypass sponsored ads to find real product listings on Amazon, Best Buy, and Walmart.""",
    tools=[search_tool],
    verbose=True
)

analyst = Agent(
    role='Deals & Benefits Analyst',
    goal='Extract prices, shipping costs, and unique membership benefits for {product_name}',
    backstory="""You have a keen eye for detail. You look for 'invisible' savings like 
    free 2-day shipping, bundled accessories, and extended return windows.""",
    tools=[scrape_tool],
    verbose=True
)

# 3. Define Tasks
search_task = Task(
    description='Search for {product_name} and return a list of valid product URLs.',
    expected_output='A list of 3-5 URLs from different e-commerce websites.',
    agent=researcher
)

comparison_task = Task(
    description="""Visit each URL found. Extract: 1. Price, 2. Shipping cost/speed, 
    3. Any current discount codes, and 4. Unique benefits (e.g. '3 months free music').""",
    expected_output='A markdown table comparing the product across retailers with a "Best Value" recommendation.',
    agent=analyst,
    context=[search_task]
)

# 4. Assemble the Crew
shopping_crew = Crew(
    agents=[researcher, analyst],
    tasks=[search_task, comparison_task],
    process=Process.sequential
)

# 5. Kickoff
result = shopping_crew.kickoff(inputs={'product_name': 'Sony WH-1000XM5 Headphones'})
print(result)
