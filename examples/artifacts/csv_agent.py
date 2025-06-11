from google.adk.agents import Agent
from google.adk.tools import ToolContext
from google.genai import types
import csv
from io import StringIO

async def save_data_as_csv(tool_context: ToolContext, data: str, filename: str) -> dict:
    # Ensure filename ends with .csv
    if not filename.endswith('.csv'):
        filename += '.csv'
    # Path within artifact store
    filepath = f"csvs/{filename}"

    # Write CSV data
    buffer = StringIO()
    writer = csv.writer(buffer)
    for line in data.splitlines():
        row = line.split(',')
        writer.writerow(row)
    csv_bytes = buffer.getvalue().encode()
    buffer.close()

    # Save artifact
    part = types.Part.from_bytes(data=csv_bytes, mime_type="text/csv")
    version = await tool_context.save_artifact(filename=filepath, artifact=part)
    return {"version": version, "filename": filepath}

csv_agent = Agent(
    name="csv_agent",
    model="gemini-2.0-flash",
    description="Agent for converting CSV text to artifact via S3.",
    instruction="Use save_data_as_csv tool with provided CSV text and filename.",
    tools=[save_data_as_csv],
)
