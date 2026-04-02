import pandas as pd

input_file = "UserBehavior.csv"
output_file = "UserBehavior_project_1million_clean.csv"

columns = [
    "user_id",
    "item_id",
    "category_id",
    "behavior_type",
    "timestamp"
]

df = pd.read_csv(
    input_file,
    header=None,
    names=columns,
    nrows=1000000,
    low_memory=False
)

# 时间转换
df["behavior_time"] = pd.to_datetime(df["timestamp"], unit="s")
df["date"] = df["behavior_time"].dt.normalize()
df["hour"] = df["behavior_time"].dt.hour

# 缺失值检查
print("缺失值统计：")
print(df.isnull().sum())

# 重复值检查
print("重复行数：", df.duplicated().sum())

# 如有需要可去重
df = df.drop_duplicates()

# 行为类型检查
print("行为类型：", df["behavior_type"].unique())

valid_types = ["pv", "cart", "fav", "buy"]
df = df[df["behavior_type"].isin(valid_types)]

# 异常值检查
print("user_id <= 0:", (df["user_id"] <= 0).sum())
print("item_id <= 0:", (df["item_id"] <= 0).sum())
print("category_id <= 0:", (df["category_id"] <= 0).sum())

# 时间范围检查
print("最早时间：", df["behavior_time"].min())
print("最晚时间：", df["behavior_time"].max())

# 保存清洗后的项目数据
df.to_csv(output_file, index=False, encoding="utf-8-sig")

print("预处理完成")
print("文件名：", output_file)
print("数据量：", len(df))
print(df.head())
