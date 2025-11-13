# Stream Store with Kafka

A simple implementation of a streaming data pipeline using Apache Kafka with Python.

## Project Structure

- `producer.py`: Python script that produces messages to a Kafka topic
- `tracker.py`: Python script that consumes and processes messages from a Kafka topic
- `docker-compose.yaml`: Docker Compose configuration for running Kafka and Zookeeper

## Prerequisites

- Docker and Docker Compose
- Python 3.7+
- Python packages: `kafka-python`

## Getting Started

1. **Start Kafka and Zookeeper**
   ```bash
   docker-compose up -d
   ```

2. **Install Python dependencies**
   ```bash
   pip install kafka-python
   ```

3. **Run the producer** (in a new terminal)
   ```bash
   python producer.py
   ```

4. **Run the tracker** (in another terminal)
   ```bash
   python tracker.py
   ```

## How It Works

- The `producer.py` script sends sample messages to a Kafka topic.
- The `tracker.py` script consumes these messages and processes them.

## Configuration

Kafka and Zookeeper configurations can be modified in the `docker-compose.yaml` file.

## License

This project is open source and available under the [MIT License](LICENSE).
