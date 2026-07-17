import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")
EXPECTED_KEYS = {"total_requests", "unique_ips", "top_path"}


def load_report():
    """Load and return the JSON report from /app/report.json."""
    return json.loads(REPORT_PATH.read_text(encoding="utf-8"))


def test_report_is_valid_json():
    """Success criterion 1: /app/report.json must contain valid JSON."""
    assert REPORT_PATH.exists(), "no report.json found"
    assert REPORT_PATH.is_file(), "report.json is not a regular file"
    load_report()


def test_report_has_exact_keys():
    """Success criterion 2: the report must contain exactly the required keys."""
    report = load_report()
    assert set(report.keys()) == EXPECTED_KEYS


def test_total_requests():
    """Success criterion 3: total_requests must equal the number of non-empty log lines."""
    report = load_report()
    assert report["total_requests"] == 6


def test_unique_ips():
    """Success criterion 4: unique_ips must equal the number of distinct client IPs."""
    report = load_report()
    assert report["unique_ips"] == 3


def test_top_path():
    """Success criterion 5: top_path must be the most frequently requested path."""
    report = load_report()
    assert report["top_path"] == "/index.html"


def test_input_log_unchanged():
    """Success criterion 6: /app/access.log must not be modified."""
    expected = (
        '192.168.0.1 - - [16/Jun/2026:10:00:01 +0000] "GET /index.html HTTP/1.1" 200 1024\n'
        '192.168.0.2 - - [16/Jun/2026:10:00:02 +0000] "GET /about.html HTTP/1.1" 200 512\n'
        '192.168.0.1 - - [16/Jun/2026:10:00:03 +0000] "GET /index.html HTTP/1.1" 200 1024\n'
        '10.0.0.5 - - [16/Jun/2026:10:00:04 +0000] "POST /api/login HTTP/1.1" 401 64\n'
        '192.168.0.2 - - [16/Jun/2026:10:00:05 +0000] "GET /index.html HTTP/1.1" 200 1024\n'
        '10.0.0.5 - - [16/Jun/2026:10:00:06 +0000] "GET /about.html HTTP/1.1" 200 512\n'
    )
    assert Path("/app/access.log").read_text(encoding="utf-8") == expected