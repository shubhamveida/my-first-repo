# strategy_tools.py
from mcp.server.fastmcp import FastMCP
from typing import Optional
import sys

# Instantiate the server with a professional name
mcp = FastMCP("McKinsey Demo - Strategic Analysis Tools")

@mcp.tool()
def calculate_market_size(population: int, penetration_rate: float, avg_price: float) -> float:
   """
   Calculates the Total Addressable Market (TAM) based on a simple top-down model.
   The result is returned in millions USD.
  
   Args:
       population: The total number of potential users/customers in the market.
       penetration_rate: The expected percentage of the population that will use the product (as a decimal, e.g., 0.05).
       avg_price: The average annual price/revenue per user/unit.
   """
   tam = population * penetration_rate * avg_price
   return round(tam / 1_000_000, 2)

@mcp.tool()
def calculate_roic(net_income: float, invested_capital: float) -> float:
   """
   Calculates the Return on Invested Capital (ROIC) as a percentage.
   This is a key performance indicator for assessing capital efficiency.

   Args:
       net_income: The company's Net Income (or NOPAT).
       invested_capital: The sum of debt and equity used to finance assets.
   """
   if invested_capital == 0:
       return 0.0
      
   roic = (net_income / invested_capital) * 100
   return round(roic, 2)

if __name__ == "__main__":
   # Avoid noisy JSON parse errors when launched directly in an interactive shell.
   # Stdio transport expects an MCP client on stdin/stdout, not manual terminal input.
   if sys.stdin.isatty():
      print("This MCP server expects an MCP client over stdio.")
      print("Use `mcp dev strategy_tools.py` (with Node/npx installed) or run via a configured MCP client.")
   else:
      mcp.run()
