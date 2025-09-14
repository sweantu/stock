1. Fetcher publishes message to Kafka topic stock-prices (partitioned by symbol).
2. **Flink** consumes stock-prices and maintains per-symbol keyed state to compute:

   - sliding-window SMA/EMA (1m, 5m, 1h)
   - percent change vs last close
   - simple anomaly detection (z-score / IQR)
   - enrichment (company metadata)

   Flink writes enriched events to processed-prices and persisting a copy to MongoDB for query and UI.

- stock-prices (key: symbol)
- { symbol, ts, price, size?, exchange?, source }
  Build fetcher service, publish canonical ticks to Kafka.

## **13) Implementation roadmap (detailed weeks)**

**Week 1**: Price Fetcher + Kafka + FastAPI skeleton

- Build fetcher service, publish canonical ticks to Kafka.
- FastAPI: basic user model, auth, and rules DB scaffolding.

1. **Week 1-2** → Implement Price Fetcher + Kafka producer + FastAPI backend (CRUD).

1. **Price Fetcher(s)**
   - Role: Poll or subscribe to market APIs and publish raw ticks/events to Kafka topic stock-prices.
   - Implementation: small Python service (aiohttp + asyncio). Kafka producer (confluent-kafka-python).
1. **Stream Processor (Flink Job)**
   - Role: Consume stock-prices, compute rolling metrics (SMA/EMA), detect anomalies, enrich with metadata, and write to processed-prices topic and MongoDB.
   - Implementation: Flink SQL or DataStream (Java/Scala/Python)

docker exec -it stock-kafka-1 kafka-topics --bootstrap-server localhost:9092 --list
docker exec -it stock-kafka-1 \
 kafka-topics --create \
 --topic my_topic \
 --bootstrap-server localhost:9092 \
 --partitions 1 \
 --replication-factor 1
