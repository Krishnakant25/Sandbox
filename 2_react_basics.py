from dotenv import load_dotenv
from langchain_classic.agents import create_react_agent, AgentExecutor, tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_classic import hub
import datetime
import pytz

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

CITY_TO_TIMEZONE = {
    "Toronto": "America/Toronto",
    "New York": "America/New_York",
    "Delhi": "Asia/Kolkata",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo"
}

def get_timezone_from_city(city_name: str) -> str:
    """
    Return an IANA timezone string for the given city_name using CITY_TO_TIMEZONE.
    If the city is not found, return "UTC" as a safe default.
    - Input: city_name (case-sensitive as implemented; you could normalize e.g. .title()).
    - Output: timezone string like "America/Toronto".
    """
    # .get looks up the key and returns default "UTC" when city_name not present.
    return CITY_TO_TIMEZONE.get(city_name, "UTC")

@tool
def get_system_time_by_city(city: str = "Delhi", format: str = "%H:%M:%S"):
    """
    Tool that returns the current time for a given city string formatted using 'format'.
    This function will be exposed to the agent as a callable tool the agent can pick.
    Parameters:
      - city: human-readable key (e.g., "Toronto"). Mapped via get_timezone_from_city.
      - format: a datetime.strftime format string (default "%H:%M:%S" -> "23:59:59").
    Returns:
      - A formatted string representing the current local time in that city, or an error string.
    Notes / details:
      - This function produces timezone-aware current time using pytz.
      - If city -> timezone mapping fails or pytz doesn't recognize the tz, it returns an error string.
      - The tool returns a **string** (simple, easy for agent to consume).
    """

    # Map city to an IANA timezone name (e.g., "America/Toronto")
    tz_name = get_timezone_from_city(city)

    try:
        # Obtain tzinfo object for the requested timezone.
        tz = pytz.timezone(tz_name)
    except pytz.UnknownTimeZoneError:
        # Defensive: if pytz doesn't know the timezone string, return a readable error.
        return f"Unknown timezone for city: {city}"

    # http://datetime.now(tz) produces the current time in that timezone (tz-aware datetime).
    # This is better than naive http://datetime.now() followed by astimezone(), because tzinfo is explicit.
    current_time = datetime.datetime.now(tz)

    # Format the datetime into a string per the caller's format argument.
    # Common formats:
    #   "%H:%M:%S" -> "23:59:59"
    #   "%I:%M %p" -> "11:59 PM"
    #   "%Y-%m-%d %H:%M:%S" -> "2025-11-12 23:59:59"
    return current_time.strftime(format)

tools = [get_system_time_by_city]

prompt_template = hub.pull("hwchase17/react")

agent = create_react_agent[llm,tools, prompt_template]

agent_exec = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

query = "Get the current time in Toronto only (no date)"

agent_exec.invoke({"input": query})

print(get_system_time_by_city(city="Toronto", format="%H:%M:%S"))