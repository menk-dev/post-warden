# Design direction

PostWarden trades flexibility for robust messaging and fault tolerance. Its public
configuration should make unsupported or unsafe combinations difficult to express
and reject invalid settings before processing messages.

RabbitMQ is the first transport. Implement concrete behavior before extracting
interfaces for other transports. Avoid exposing a general RabbitMQ configuration
passthrough that lets consumers undermine PostWarden's guarantees.

Before implementing the API, document and test delivery semantics, publisher
confirmation, acknowledgement timing, bounded retries and poison-message handling,
reconnection, backpressure, cancellation, graceful shutdown, and resource disposal.
Distinguish broker acceptance from successful processing. Account for duplicate
delivery and application idempotency; do not promise exactly-once delivery.

These are design requirements for future work, not implemented guarantees.
Transport defaults, topology, serialization, and API shape remain undecided.
