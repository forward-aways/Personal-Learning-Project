import json

data = {
    "name": "John",
    "age": 30,
    "city": ["New York", "Los Angeles"]
}
# dump string, 把Python对象转换成JSON字符串，和json.dump()的区别在于json.dump()是把Python对象转换成JSON字符串并写入文件
text = json.dumps(data, ensure_ascii=False, indent=2)

print(text)


# load string, 把JSON字符串转换成Python对象，和json.load()的区别在于json.load()是把JSON字符串转换成Python对象并从文件中读取
text1 = '{"name": "Alice", "ages": 30}'
data1 = json.loads(text1)

print(data1["name"])
print(type(data1))

