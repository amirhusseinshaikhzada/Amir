from schema import db_url
import psycopg2






def connect_to_db():
    conn = psycopg2.connect(db_url)
    cursor = conn.cursor()
    return conn , cursor



def add_question(question, option1, option2, option3, option4, correct_option):
    try:
        # استفاده از with باعث می‌شود اتصال و کرسر خودکار بسته شوند
        with connect_to_db() as (conn, cursor):
            cursor.execute('''
                INSERT INTO questions (question, option1, option2, option3, option4, correct_option) 
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (question, option1, option2, option3, option4, correct_option))
            conn.commit()
            print("Question added successfully.")
    except Exception as e:
        print(f"Error adding question: {e}")

def get_all_questions():
    try:
        with connect_to_db() as (conn, cursor):
            cursor.execute("SELECT * FROM questions")
            return cursor.fetchall()
    except Exception as e:
        print(f"Error fetching questions: {e}")
        return []  # در صورت خطا، لیست خالی برمی‌گرداند تا برنامه کرش نکند

def save_result(user_id, score):
    try:
        with connect_to_db() as (conn, cursor):
            cursor.execute("INSERT INTO results (user_id, score) VALUES (%s, %s)", (user_id, score))
            conn.commit()
            print("Result saved successfully.")
    except Exception as e:
        print(f"Error saving result: {e}")

def get_user_results(user_id):
    try:
        with connect_to_db() as (conn, cursor):
            # توجه: استفاده از (user_id,) برای تبدیل به tuple صحیح است
            cursor.execute("SELECT score FROM results WHERE user_id = %s", (user_id,))
            return cursor.fetchall()
    except Exception as e:
        print(f"Error fetching results: {e}")
        return []
