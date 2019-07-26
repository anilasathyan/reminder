import psycopg2
from datetime import date

try:
    conn = psycopg2.connect("dbname='db_remider' user='postgres' host='localhost' password='Manager@123'")
    cur = conn.cursor()
    def create_reminder():
        mailid=input("Enter emailid")
        reminder_date = input("Enter Date")
        reminder_message = input("Enter your message")
        insert_query = """INSERT INTO reminder(created_emailid,date,message) VALUES(%s,'%s,%s')"""
        record_insert=(mailid,reminder_date, reminder_message)
        cur.execute(insert_query,record_insert)
        conn.commit();
    create_reminder()



    # view reminder
    def view_reminder():
        mailid = input("Enter emailid")
        select_query = """SELECT * FROM  reminder where created_emailid='%s'"""
        query=select_query %mailid
        cur.execute(query)
        events = cur.fetchall()
        print(events)
        # notification for todays event
        today = date.today()
        current_day = today.strftime('%d/%m/%Y')  # get the todays date as dd-Month-year format
        select_query = """SELECT date FROM  reminder where created_emailid='%s'"""
        query = select_query % mailid
        cur.execute(query)
        dates = cur.fetchall()
        conn.commit();
        # print(dates)
        # loop through each entry , and check whether the day is present or not
        for entry in dates:
            if current_day in entry:
                print("You have an event today")
            else:
                print("You have no event today")
    view_reminder()




 #update reminder
    def update_reminder():
        mailid = input("Enter emailid")
        date= input("Enter date")
        new_msg=input("New message")
        update_query = """UPDATE reminder set message = '%s' where created_emailid='%s' and date='%s'"""
        value= update_query %new_msg %mailid %date
        cur.execute(value)
        conn.commit();
    update_reminder()




except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

finally:
    if (conn):
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")
