from schema import db_url
import psycopg2




db_path = os.getenv("DATABASE_URL")



try:
    conn = psycopg2.connect(db_url)
    cursor = conn.cursor()

    # لیست سوالات را برای مدیریت بهتر، به صورت یک لیست از Tuple تعریف می‌کنیم
    # ترتیب: (question, option1, option2, option3, option4, correct_option)
    questions_to_insert = [
        ('پایتون چیست؟', 'یک سیستم عامل', 'نام یک حیوان', 'یک مرورگر', 'یک زبان برنامه نویسی', 5),
        ('کدام گزینه نوع داده در پایتون است؟', 'Table', 'House', 'int', 'Car', 3),
        ('برای چاپ در پایتون از چه دستوری استفاده می‌شود؟', 'out()', 'print()', 'echo()', 'write()', 2),
        ('خروجی 2 ** 3 در پایتون چند می‌شود؟', '10', '6', '9', '5', 3),
        ('سوال آزمایشی ۱', 'گزینه ۱', 'گزینه ۲', 'گزینه ۳', 'گزینه ۴', 1),
        ('سوال آزمایشی ۲', 'گزینه ۱', 'گزینه ۲', 'گزینه ۳', 'گزینه ۴', 2)
    ]

    # استفاده از execute_values یا یک حلقه برای امنیت و تمیزی بیشتر
    insert_query = '''
        INSERT INTO questions (question, option1, option2, option3, option4, correct_option) 
        VALUES (%s, %s, %s, %s, %s, %s)
    '''

    for q in questions_to_insert:
        cursor.execute(insert_query, q)

    conn.commit()
    print("تمام سوالات با موفقیت وارد شدند.")

except Exception as e:
    print(f"خطا در هنگام درج داده‌ها: {e}")

finally:
    if 'conn' in locals() and conn:
        cursor.close()
        conn.close()
