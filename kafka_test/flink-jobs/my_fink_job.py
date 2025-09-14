from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.kafka import KafkaOffsetsInitializer, KafkaSource

env = StreamExecutionEnvironment.get_execution_environment()

source = (
    KafkaSource.builder()
    .set_bootstrap_servers("kafka:29092")
    .set_topics("my_topic")
    .set_group_id("flink_consumer")
    .set_starting_offsets(KafkaOffsetsInitializer.earliest())
    .build()
)

ds = env.from_source(source, WatermarkStrategy.no_watermarks(), "Kafka Source")
ds.print()

env.execute("Kafka-PyFlink Example")
