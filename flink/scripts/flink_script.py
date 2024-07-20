from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.functions import MapFunction, ReduceFunction
from pyflink.table import StreamTableEnvironment

# Initialize the Flink environment
env = StreamExecutionEnvironment.get_execution_environment()
table_env = StreamTableEnvironment.create(env)

# Define a data source (e.g., socket stream)
data_stream = env.socket_text_stream("localhost", 9999)

# Define a map function to split the incoming data
class Splitter(MapFunction):
    def map(self, value: str) -> tuple:
        parts = value.split(",")
        return (parts[0], int(parts[1]))

# Define a reduce function for aggregation
class SumReducer(ReduceFunction):
    def reduce(self, value1: tuple, value2: tuple) -> tuple:
        return (value1[0], value1[1] + value2[1])

# Apply transformations
split_stream = data_stream.map(Splitter())
keyed_stream = split_stream.key_by(lambda x: x[0])
aggregated_stream = keyed_stream.reduce(SumReducer())

# Print the results to the console
aggregated_stream.print()

# Execute the Flink job
env.execute("Stream Processing with Flink")

