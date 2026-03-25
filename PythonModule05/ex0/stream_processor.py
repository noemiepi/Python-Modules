# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  stream_processor.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: npillet <npillet@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/10 08:24:27 by npillet         #+#    #+#               #
#  Updated: 2026/03/21 09:26:52 by npillet         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        pass


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            n = 0
            lst = [int(i) for i in data if int(i)]
            n = len(lst)
            sm_res = sum(lst)
            avg_res = sm_res / n
            res1 = f"Processed {n} numeric values, "
            res2 = f"sum={sm_res}, avg={avg_res:.1f}"
            return f"{res1}{res2}"
        except ValueError as e:
            print(f"Error! {e}")
        except TypeError as e:
            print(f"Error! {e}")
        except ZeroDivisionError as e:
            print(f"Error! {e}")
        except Exception as e:
            return f"Error! {e}"

    def validate(self, data: Any) -> bool:
        if len(data) == 0:
            return False
        try:
            for i in data:
                if int(i):
                    pass
            return True
        except ValueError:
            return False
        except Exception as e:
            return f"Error! {e}"

    def format_output(self, result: str) -> str:
        return result


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            nb_char = 0
            nb_word = 0
            for i in data:
                nb_char += 1
                if i == " " or nb_char == len(data):
                    nb_word += 1
            return f"Processed text: {nb_char} characters, {nb_word} words"
        except ValueError as e:
            print(f"Error! {e}")
        except TypeError as e:
            print(f"Error! {e}")
        except Exception as e:
            return f"Error! {e}"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        else:
            return False

    def format_output(self, result: str) -> str:
        return result


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            split = data.split(':', 2)
            log_type = split[0]
            if log_type == 'NOTSET':
                log_level = f"[NOTSET] {log_type}"
            elif log_type == 'DEBUG':
                log_level = f"[DEBUG] {log_type}"
            elif log_type == 'INFO':
                log_level = f"[INFO] {log_type}"
            elif log_type == 'WARNING':
                log_level = f"[WARNING] {log_type}"
            elif log_type == 'ERROR':
                log_level = f"[ALERT] {log_type}"
            elif log_type == 'CRITICAL':
                log_level = f"[CRITICAL] {log_type}"
            message = split[1]
            return f"{log_level} level detected:{message}"
        except ValueError as e:
            print(f"Error! {e}")
        except TypeError as e:
            print(f"Error! {e}")
        except Exception as e:
            return f"Error! {e}"

    def validate(self, data: Any) -> bool:
        try:
            p = 0
            for i in data:
                if i == ':':
                    p = 1
            if isinstance(data, str) and p == 1:
                return True
            else:
                return False
        except TypeError:
            return False
        except Exception as e:
            print(e)

    def format_output(self, result: str) -> str:
        return result


def stream_processor() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    numeric = NumericProcessor()
    number = [1, 2, 3, 4, 5]
    print(f"Processing data: {number}")
    if numeric.validate(number) is True:
        print("Validation: Numeric data verified")
        print(f"Output: {numeric.format_output(numeric.process(number))}")
    else:
        print("Validation: Numeric data invalid")

    print("\nInitializing Text Processor...")
    text = TextProcessor()
    sentence = "Hello Nexus World"
    print(f"Processing data: '{sentence}'")
    if text.validate(sentence) is True and len(sentence) == 0:
        print("Validation: Text data empty")
    elif text.validate(sentence) is True:
        print("Validation: Text data verified")
        print(f"Output: {text.format_output(text.process(sentence))}")
    else:
        print("Validation: Text data invalid")

    print("\nInitializing Log Processor...")
    log = LogProcessor()
    message = "ERROR: Connection timeout"
    print(f"Processing data: '{message}'")
    if log.validate(message) is True:
        print("Validation: Log entry verified")
        print(f"Output: {log.format_output(log.process(message))}")
    else:
        print("Validation: Log entry invalid")

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    data_dict = {
        NumericProcessor(): [1, 2, 3],
        TextProcessor(): "Hello Human!",
        LogProcessor(): "INFO: System ready"
    }
    i = 0
    for data_type, data in data_dict.items():
        result = data_type.format_output(data_type.process(data))
        print(f"Result {i}: {result}")
        i += 1

    print("\nFondation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    stream_processor()
