#!/usr/bin/python3
"""
File Class for ABC class
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class"""

    @abstractmethod
    def sound(self):
        """Sound of the animal"""
        pass


class Dog(Animal):
    """SubClass for a Dog Animal"""

    def sound(self):
        """Sound of the Dog"""
        return "Bark"


class Cat(Animal):
    """SubClass for a Cat Animal"""

    def sound(self):
        """Sound of the cat"""
        return "Meow"
