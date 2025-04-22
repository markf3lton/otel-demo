from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
import time

# Setup basic tracing
resource = Resource.create({"service.name": "basic-demo"})
tracer_provider = TracerProvider(resource=resource)
otlp_exporter = OTLPSpanExporter(endpoint="localhost:4317", insecure=True)
span_processor = BatchSpanProcessor(otlp_exporter)
tracer_provider.add_span_processor(span_processor)
trace.set_tracer_provider(tracer_provider)
tracer = trace.get_tracer("basic-demo")

print("Starting OpenTelemetry demo...")

# Create a span
with tracer.start_as_current_span("hello-otel") as span:
    span.set_attribute("example.key", "example-value")
    print("Sending a test span...")
    time.sleep(1)

print("Done! Check the collector logs.")
time.sleep(2)  # Give exporter time to send
tracer_provider.shutdown()
