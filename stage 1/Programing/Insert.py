import random
from datetime import datetime, timedelta

# פונקציה ליצירת פקודות INSERT
def generate_insert_statements():
    maternity_data = []
    for i in range(1, 401):
        name = f'יולדת {i}'
        age = random.randint(18, 45)
        phone = f'05{random.randint(10000000, 99999999)}'
        maternity_data.append(f"INSERT INTO Maternity VALUES ({i}, '{name}', {age}, '{phone}');")
    
    return '\n'.join(maternity_data)

# כתיבת הפלט לקובץ
with open("insert_maternity.sql", "w", encoding="utf-8") as f:
    f.write(generate_insert_statements())

print("קובץ insert_maternity.sql נוצר בהצלחה!")
