#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Использовать словарь, содержащий следующие ключи: фамилия и инициалы; номер
#группы; успеваемость (список из пяти элементов). Написать программу, выполняющую
#следующие действия: ввод с клавиатуры данных в список, состоящий из словарей заданной
#структуры; записи должны быть упорядочены по алфавиту; вывод на дисплей фамилий и
#номеров групп для всех студентов, имеющих хотя бы одну оценку 2; если таких студентов
#нет, вывести соответствующее сообщение. Оформить каждую команду в виде отдельной функции.
#Дополнительно реализовать сохранение и чтение данных из файла формата JSON.
import json

def input_data():
    students = []
    n = int(input("Введите количество студентов: "))
    for i in range(n):
        student = {}
        student["фамилия и инициалы"] = input("Введите фамилию и инициалы студента: ")
        student["номер группы"] = input("Введите номер группы студента: ")
        student["успеваемость"] = []
        for j in range(5):
            mark = int(input(f"Введите оценку {j+1}: "))
            student["успеваемость"].append(mark)
        students.append(student)
    students.sort(key=lambda x: x["фамилия и инициалы"])
    return students

def save_data(students):
    with open("students.json", "w") as file:
        json.dump(students, file, ensure_ascii=False)

def read_data():
    with open("students.json", "r") as file:
        students = json.load(file)
        students.sort(key=lambda x: x["фамилия и инициалы"])
        return students

def print_students_with_mark2(students):
    found = False
    for student in students:
        if 2 in student["успеваемость"]:
            print(f"Студент: {student['фамилия и инициалы']}, группа: {student['номер группы']}")
            found = True
    if not found:
        print("Нет студентов с оценкой 2")

students = input_data()
save_data(students)

students = read_data()
print_students_with_mark2(students)


if __name__ == "__main__":
    main()