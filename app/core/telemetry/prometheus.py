# -*- coding: utf-8 -*-
import httpx


def check_prometheus_health():
    try:
        client = httpx.Client()
        r = client.get("http://localhost:9090/-/healthy")  # Adjust this URL as needed
        if r.status_code == 200:
            return {
                "status": "ok",
                "detail": "Prometheus is up and running",
            }
        else:
            return {
                "status": "error",
                "detail": "Prometheus health endpoint returned status code {r.status_code}",
            }
    except Exception as e:
        return {
            "status": "error",
            "detail": f"Error checking Prometheus health: {e}",
        }
