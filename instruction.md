
Analyze the Apache-style access log at /app/access.log and write the results as a JSON report to /app/report.json.

Success criteria:

1. The file /app/report.json must contain a valid JSON.

2. The JSON object must contain exactly these keys: "total_requests", "unique_ips", and "top_path".

3. "total_requests" must be the number of non-empty log lines in /app/access.log.

4. "unique_ips" must be the number of distict client IP addresses appearing at the beginning of the log lines.

5. "top_path" must be the request path that appears most often across GET, POST, PUT, DELETE, HEAD, and PATCH requests.

6. Do not modify /app/access.log.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
