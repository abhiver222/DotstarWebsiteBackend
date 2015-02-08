'''
creates fake staff, student, and userdetails entries for testing
'''
import sys,random,pymysql
from config import *
from faker import Factory

def build_query(data,stub):
    res='{0} VALUES ('.format(stub)
    for i in range(len(data)):
        res+="{0}, ".format(conn.escape(data[i]))
    return '{0});'.format(res[:-2])
    

if len(sys.argv) < 2:
    print("please rerun, including # of fake users as an argument (e.g. python load_examples.py 100)\n\n")
    sys.exit(0)

# will transition to unified db connection once resolved
conn = pymysql.connect(host=DB_HOST,port=DB_PORT,user=DB_USER,passwd=DB_PASSWORD, db=DB_NAME)
cur = conn.cursor()

faker = Factory.create()
majors = ['history of films of giraffes', 'toilet building', 'outhouse engineering', 'orea eating', 'mysql injection engineering', 'uranus studies', 'urinary studies (back-door emphasis)', 'history of thai/pho 911', 'jewish purple studies', 'food tasting (physics emphasis)']
years = ['Freshman', 'Sophomore', 'Junior', 'Senior', 'Masters student', 'Ph.D. student']

for i in range(int(sys.argv[1])):
    first=faker.first_name();
    last=faker.last_name()
    netid=first[0].lower()+last.lower()+str(random.randint(1,8))
    user = [
        netid,
        str(faker.unix_time())[:9]
    ]        
    user_details=[
        netid,
        first,
        last,
        faker.phone_number(),
        faker.free_email(),
        'https://lh3.googleusercontent.com/-5xJxDlJjR8I/AAAAAAAAAAI/AAAAAAAAABE/BPljDaS7N6s/photo.jpg',
        faker.user_name(),
        random.choice(majors),
        random.choice(years),
        faker.catch_phrase(),
        faker.bs()
    ]
    

    queries = [build_query(user,'INSERT INTO Users (NetId, UIN)'), build_query(user_details,'INSERT INTO UserDetails (NetId, FirstName, LastName, Phone, BestEmail, Picture, Github, Major, Year, Skills, Wants)')]

    map(cur.execute,queries)
    conn.commit()

cur.close()
conn.close()
