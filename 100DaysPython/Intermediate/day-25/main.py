import csv
import pandas

# with open("weather_data.csv") as wd:
#     data = csv.reader(wd)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()

# print(data_dict)

# temp_list = data["temp"]
# print(data.temp)

# get row data
# print(data[data.day == "Monday"])
# print(data.temp)
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_F = monday_temp * 1.8 + 32
# print(monday_F)


# Create df from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# datas = pandas.DataFrame(data_dict)
# datas.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squirrel_count)
# print(red_squirrel_count)
# print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Amount": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

datas = pandas.DataFrame(data_dict)
datas.to_csv("squirrel.csv")
print(datas)
