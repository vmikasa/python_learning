# 学习一点json数据格式

import json

# python读取配置（load）
with open("config.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)   # 直接把文件里的 JSON 读成 Python dict

print(cfg["host"])
print(cfg["db"]["path"])

# python写出配置（dump）
cfg = {
    "host": "127.0.0.1",
    "port": 8080,
    "debug": True,
    "timeout": 5.0,
    "log_level": "INFO",
    "allowed_users": ["alice", "bob", "cindy"],
    "db": {"type": "sqlite", "path": "data/app.db"}
}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(cfg, f, ensure_ascii=False, indent=2)




# 小练习：
def load_users(path):
    try:
        with open(path,"r",encoding="utf-8") as f:
            users=json.load(f)
            return users
    except FileNotFoundError:
        print("文件不存在,返回空列表")
        return []

def save_users(users,path):
    with open(path,"w",encoding="utf-8") as f:
        json.dump(users,f,ensure_ascii=False,indent=2)

def add_user(path,name,age):
    users=load_users(path)
    if users:  # 如果列表不为空，注意不能写成 if users is not None，因为这样写很严格，必须是 None 才会返回 False，而如果是空列表的话，users 也是不 None 的，所以 if users is not None 是不合适的。if users 就可以了，因为空列表在布尔上下文中会被视为 False，而非空列表会被视为 True。
        new_id=max(user["id"] for user in users)+1  # 可以这么写。因为原json数据里面，id是数字，如果是字符串的话，就需要先转换成数字再比较了
    else:
        new_id=1
    users.append({"id": new_id, "name": name, "age": age},)
    save_users(users,path)

def get_user_by_name(path,name):
    users=load_users(path)
    for user in users:
        if user["name"]==name:
            return user
    else:
        return None

# json.dump和json.dumps的区别
# json.dump是把Python对象写入文件，而json.dumps是把Python对象转换成JSON字符串。json.dump需要一个文件对象作为参数，而json.dumps返回一个字符串，可以直接打印或者赋值给变量。json.dump的语法是json.dump(obj, fp, ensure_ascii=False, indent=2)，其中obj是要写入的Python对象，fp是文件对象，ensure_ascii=False表示不转义非ASCII字符，indent=2表示缩进2个空格。json.dumps的语法是json.dumps(obj, ensure_ascii=False, indent=2


