# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  data_stream.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/10 11:51:49 by npillet         #+#    #+#               #
#  Updated: 2026/03/21 09:32:49 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Union


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.type = "Data Stream"

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria:
                    Optional[str] = None) -> List[Any]:
        if criteria is not None:
            data_batch = [data for data in data_batch if criteria in data]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = {"id": self.stream_id, "type": self.type}
        return stats


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            i = 0
            lst = []
            for data in data_batch:
                split = data.split(':')
                if split[0] == "temp":
                    temp = float(split[1])
                    lst.append(temp)
                i += 1
            avg_temp = sum(lst) / len(lst)
            return f"{i} readings processed, avg temp: {avg_temp}°C"
        except ValueError as e:
            return f"Error! {e}"
        except ZeroDivisionError:
            return "Error! No temp variable in the list"
        except Exception as e:
            return f"Error! {e}"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            i = 0
            net = 0
            for data in data_batch:
                split = data.split(':')
                if split[0] == "buy":
                    net += int(split[1])
                    i += 1
                elif split[0] == "sell":
                    net -= int(split[1])
                    i += 1
                else:
                    print(f"{split[0]} is neither buy or sell")
            if net > 1:
                return f"{i} operations, net flow: +{net} units"
            elif net < -1:
                return f"{i} operations, net flow: {net} units"
            elif 0 <= net == 1:
                return f"{i} operations, net flow: +{net} unit"
            elif net == -1:
                return f"{i} operations, net flow: {net} unit"
            else:
                return "No transactions done"
        except ValueError as e:
            return f"Error! {e}"
        except Exception as e:
            return f"Error! {e}"


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            i = 0
            nb_error = 0
            for data in data_batch:
                if data == "error":
                    nb_error += 1
                i += 1
            if nb_error == 1:
                return f"{i} events, {nb_error} error detected"
            elif nb_error > 1:
                return f"{i} events, {nb_error} errors detected"
            else:
                return f"{i} events"
        except Exception as e:
            return f"Error! {e}"


class StreamProcessor():
    def __init__(self) -> None:
        self.streams = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_data_stream(self, batch_data: Dict[str, List[Any]]) -> None:
        for stream in self.streams:
            name_stream = stream.stream_id
            data = batch_data.get(stream.stream_id)
            if data is None:
                print(f"- No data in {name_stream}")
            else:
                results = stream.process_batch(data)
                print(f"- {name_stream}: {results}")


def data_stream() -> None:
    try:
        print("\nInitializing Sensor Stream...")
        sensor_stream = SensorStream("SENSOR_001")
        stats = sensor_stream.get_stats()
        print(f"Stream ID: {stats.get('id')}, Type: {stats.get('type')}")
        sensor_batch = [
            "temp:22.5",
            "humidity:65",
            "pressure:1013"
        ]
        print(f"Processing sensor batch: {sensor_batch}")
        print(f"Sensor analysis: {sensor_stream.process_batch(sensor_batch)}")

        print("\nInitializing Transaction Stream...")
        trans_stream = TransactionStream("TRANS_001")
        stats = trans_stream.get_stats()
        print(f"Stream ID: {stats.get('id')}, Type: {stats.get('type')}")
        trans_batch = [
            "buy:100",
            "sell:150",
            "buy:75"
        ]
        print(f"Processing transaction batch: {trans_batch}")
        print("Transaction analysis: "
              f"{trans_stream.process_batch(trans_batch)}")

        print("\nInitializing Event Stream...")
        event_stream = EventStream("EVENT_001")
        stats = event_stream.get_stats()
        print(f"Stream ID: {stats.get('id')}, Type: {stats.get('type')}")
        event_batch = [
            "login",
            "error",
            "logout"
        ]
        print(f"Processing event batch: {event_batch}")
        print(f"Event analysis: {event_stream.process_batch(event_batch)}")

        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")

        batches = StreamProcessor()
        processor_sensor = SensorStream("Sensor data")
        batches.add_stream(processor_sensor)
        processor_trans = TransactionStream("Transaction data")
        batches.add_stream(processor_trans)
        processor_event = EventStream("Event data")
        batches.add_stream(processor_event)

        batch_data = {
            "Sensor data": ["temp:19.5", "humidity:50"],
            "Transaction data": ["buy:100", "sell:150", "buy:75", "sell:30"],
            "Event data": ["login", "error", "logout"]
        }

        print("\nBatch 1 Results:")
        batches.process_data_stream(batch_data)

        critical_sensor = sensor_stream.filter_data(batch_data["Sensor data"])
        large_trans = trans_stream.filter_data(batch_data["Transaction data"],
                                               "150")
        print("\nStream filtering active: High-priority data only")
        print(f"Filtered results: {len(critical_sensor)} critical sensor "
              f"alerts, {len(large_trans)} transaction")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    data_stream()

    print("\nAll streams processed succesfully. Nexus throughput optimal.")
