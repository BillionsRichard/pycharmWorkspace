# encoding: utf-8

"""
@version: v1.0
@author: Richard
@license: Apache Licence
@contact: billions.richard@qq.com
@site:https://github.com/BillionsRichard
@software: PyCharm
@time: 2020/5/16 11:58
"""
import threading
from threading import Lock
from typing import Callable


class FizzBuzz(threading.Thread):
    def __init__(self, n: int):
        threading.Thread.__init__(self, name="mainthread")
        self.n = n
        self.last_print_num = 1
        self.lock = Lock()

    def in_range(self):
        return self.last_print_num <= self.n

    def thread_a_execute(self):
        return self.last_print_num % 3 == 0 and self.last_print_num % 5 != 0

    def thread_b_execute(self):
        return (
            self.in_range()
            and self.last_print_num % 5 == 0
            and self.last_print_num % 3 != 0
        )

    def thread_c_execute(self):
        return self.last_print_num % 3 == 0 and self.last_print_num % 5 == 0

    def thread_d_execute(self):
        return self.last_print_num % 3 != 0 and self.last_print_num % 5 != 0

    def fizz(self, printFizz: "Callable[[], None]") -> None:
        """

        :param printFizz: printFizz() outputs "fizz"
        :return:
        """
        while True:
            with self.lock:
                if not self.in_range():
                    return

                if self.thread_a_execute():
                    printFizz()
                    self.last_print_num += 1

    def buzz(self, printBuzz: "Callable[[], None]") -> None:
        """

        :param printBuzz: printBuzz() outputs "buzz"
        :return:
        """
        while True:
            with self.lock:
                if not self.in_range():
                    return

                if self.thread_b_execute():
                    printBuzz()
                    self.last_print_num += 1

    def fizzbuzz(self, printFizzBuzz: "Callable[[], None]") -> None:
        """

        :param printFizzBuzz: printFizzBuzz() outputs "fizzbuzz"
        :return:
        """
        while True:
            with self.lock:
                if not self.in_range():
                    return

                if self.thread_c_execute():
                    printFizzBuzz()
                    self.last_print_num += 1

    def number(self, printNumber: "Callable[[int], None]") -> None:
        """

        :param printNumber: printNumber(x) outputs "x", where x is an integer.
        :return:
        """
        while True:
            with self.lock:
                if not self.in_range():
                    return

                if self.thread_d_execute():
                    printNumber(self.last_print_num)
                    self.last_print_num += 1

    def run(self):
        targets = self.fizz, self.buzz, self.fizzbuzz, self.number
        names = "ABCD"
        threads = [
            threading.Thread(target=targets[i], name=names[i], args=(None,))
            for i in range(4)
        ]

        for thread in threads:
            thread.start()


# if __name__ == "__main__":
#     fizbuz = FizzBuzz(15)
#     fizbuz.start()
# fizbuz.join()
