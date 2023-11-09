import os
import pandas as pd
import json
import msgpack

df = pd.read_csv('https://data.ct.gov/api/views/5mzw-sjtu/rows.csv',
                 low_memory=False)  # Может долго обрабатывать через ссылку, лучше бы было скачать csv, но файл весит 107 МБ, а гитхаб не принимает больше 100, а если удалить строки для уменьшения объема, то файл почему-то ломается

#Выбор
selected_fields = df.columns[:10]

# Рассчет характеристик для числовых полей
numeric_stats = df[selected_fields].describe().to_dict()

# Рассчет частоты встречаемости для текстовых полей
text_stats = {}
for field in selected_fields:
    if df[field].dtype == 'O':
        text_stats[field] = df[field].value_counts().to_dict()

with open('./output./5_statistics.json', 'w') as json_file:
    json.dump({'numeric_stats': numeric_stats, 'text_stats': text_stats}, json_file, indent=2)

df.to_csv('./output/5_dataset.csv', index=False)
df.to_json('./output/5_dataset.json', orient='records', lines=True)
df.to_pickle('./output/5_dataset.pkl')

with open('./output/5_dataset.msgpack', 'wb') as msgpack_file:
    packed_data = msgpack.packb(df.to_dict(orient='records'))
    msgpack_file.write(packed_data)

print(f"Размер csv: {os.path.getsize('./output/5_dataset.csv')}")
print(f"Размер json: {os.path.getsize('./output/5_dataset.json')}")
print(f"Размер pkl: {os.path.getsize('./output/5_dataset.pkl')}")
print(f"Размер msgpack: {os.path.getsize('./output/5_dataset.msgpack')}")

