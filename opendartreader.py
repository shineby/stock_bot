import OpenDartReader

file = open("c:/dart_api_key.txt", "r")
api_key = file.readline()
dart = OpenDartReader(api_key)

print(dart.list('005930', kind='A', start='2020-01-01', end='2020-10-18'))
