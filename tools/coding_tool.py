import re
from typing import Annotated
from langchain_core.tools import tool
from langchain_experimental.utilities import PythonREPL


@tool
def python_repl_tool(code: Annotated[str, "The python code to execute to generate your chart."]):
    """Executes the provided Python code in a REPL environment and returns the output."""


    # Force safe backend early
    matplotlib_prefix = """
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
"""

    if "plt." in code:
        code = matplotlib_prefix + code

        # Remove any user-defined plt.savefig(...) to override
        code = re.sub(r"plt\.savefig\([^\)]*\)", "", code)

        # Append chart-saving logic
        code += """
import os
import uuid
filename = f"{uuid.uuid4().hex[:8]}.png"
os.makedirs("charts", exist_ok=True)
file_path = os.path.abspath(os.path.join("charts", filename))
plt.savefig(file_path)
print(f"Saved chart to: {file_path}")
"""

    # Remove GUI
    code = code.replace("plt.show()", "")

    try:
        repl = PythonREPL()
        result = repl.run(code)
    except BaseException as e:
        return f"Failed to execute. Error: {repr(e)}"

    result_str = f"Successfully executed:\n```python\n{code}\n```\nStdout: {result}"
    print(result_str)
    return result_str
