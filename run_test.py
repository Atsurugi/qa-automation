import pytest
import os
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_name = f"reports/report_{timestamp}.html"

os.makedirs("reports", exist_ok=True)

pytest.main([
    "tests/", "-v", f"--html={report_name}", "--self-contained-html"
])