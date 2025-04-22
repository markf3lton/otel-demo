# otel-demo
My OpenTelemetry demo for hands-on learning.

### Prerequisites
My prequisites are typically managed with homebrew on macOS.
- OrbStack (or some type of Docker Desktop)
- python3 and pip3 (aliased to `python` and `pip` in ~/.zshrc)
- DDEV (decent knowledge of this is assumed)

### Getting started  
- Clone this project directory (I use `~/Projects/otel-demo`) and `cd` into it
- Confirm docker is running (`docker ps`)
- Start the project (`docker-compose up -d`)
- Activate Python virtual environment (`source venv/bin/activate`) and (when ready to stop it) type `deactivate`
- Install and run OpenTelemetry dependencies with:

```
pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp-proto-grpc
```

### Run the app

```
python demo.py
```
