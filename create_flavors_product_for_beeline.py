import pymysql.cursors

# Connect to the database
host = '10.162.75.12'
user = 'proxysql_user'
password = 'wWuq4bzIkOcCAOC3A9GKkdRf5PYLFrkM'
db = 'user_public'

flavors = (
    "general-S.1-05.dme.linux", "general-S.1-05.dme.windows", "general-S.1-1.dme.linux", "general-S.1-1.dme.windows",
    "general-S.1-2.dme.linux", "general-S.1-2.dme.windows", "general-S.1-4.dme.linux", "general-S.1-4.dme.windows",
    "general-S.2-2.dme.linux", "general-S.2-2.dme.windows", "general-S.2-4.dme.linux", "general-S.2-4.dme.windows",
    "general-S.2-8.dme.linux", "general-S.2-8.dme.windows", "general-M.2-16.dme.linux", "general-M.2-16.dme.windows",
    "general-S.4-4.dme.linux", "general-S.4-4.dme.windows", "general-S.4-8.dme.linux", "general-S.4-8.dme.windows",
    "general-M.4-16.dme.linux", "general-M.4-16.dme.windows", "general-M.4-24.dme.linux", "general-M.4-24.dme.windows",
    "general-M.4-32.dme.linux", "general-M.4-32.dme.windows", "general-S.8-8.dme.linux", "general-S.8-8.dme.windows",
    "general-M.8-16.dme.linux", "general-M.8-16.dme.windows", "general-M.8-24.dme.linux", "general-M.8-24.dme.windows",
    "general-M.8-32.dme.linux", "general-M.8-32.dme.windows", "general-L.8-64.dme.linux", "general-L.8-64.dme.windows",
    "general-M.16-24.dme.linux", "general-M.16-24.dme.windows", "general-M.16-32.dme.linux",
    "general-M.16-32.dme.windows",
    "general-L.16-64.dme.linux", "general-L.16-64.dme.windows", "general-L.16-128.dme.linux",
    "general-L.16-128.dme.windows", "general-M.24-32.dme.linux", "general-M.24-32.dme.windows",
    "general-L.24-64.dme.linux",
    "general-L.24-64.dme.windows", "general-L.24-128.dme.linux", "general-L.24-128.dme.windows",
    "general-L.24-96.dme.linux", "general-L.24-96.dme.windows", "general-M.32-32.dme.linux",
    "general-M.32-32.dme.windows",
    "general-L.32-64.dme.linux", "general-L.32-64.dme.windows", "general-L.32-128.dme.linux",
    "general-L.32-128.dme.windows", "general-L.32-256.dme.linux", "general-L.32-256.dme.windows",
    "general-L.32-384.dme.linux", "general-L.32-384.dme.windows", "general-L.36-64.dme.linux",
    "general-L.36-64.dme.windows")

deleted_flavors = ("compute.giga.dme.linux", "memory.nano.dme.linux", "memory.mega.dme.linux", "memory.giga.dme.linux",
                   "memory.tera.dme.linux", "memory.tera.dme.windows", "general.1-4.dme.windows",
                   "general.2-16.dme.linux", "general.2-16.dme.windows", "general.4-4.dme.linux",
                   "general.4-4.dme.windows", "general.4-8.dme.windows", "general.4-24.dme.linux",
                   "general.4-24.dme.windows", "general.4-32.dme.linux", "general.4-32.dme.windows",
                   "general.8-8.dme.linux", "general.8-8.dme.windows", "general.8-16.dme.windows",
                   "general.8-24.dme.linux", "general.8-24.dme.windows", "general.8-32.dme.linux",
                   "general.8-32.dme.windows", "general.8-64.dme.windows", "general.16-24.dme.linux",
                   "general.16-24.dme.windows", "general.16-32.dme.linux", "general.16-32.dme.windows",
                   "general.16-128.dme.linux", "general.16-128.dme.windows", "general.24-32.dme.linux",
                   "general.24-32.dme.windows", "general.24-64.dme.linux", "general.24-64.dme.windows",
                   "general.24-128.dme.linux", "general.24-128.dme.windows", "general.24-96.dme.linux",
                   "general.24-96.dme.windows", "general.32-32.dme.linux", "general.32-32.dme.windows",
                   "general.32-64.dme.linux", "general.32-64.dme.windows", "general.32-128.dme.linux",
                   "general.32-128.dme.windows", "general.32-256.dme.linux", "general.32-256.dme.windows",
                   "general.32-384.dme.linux", "general.32-384.dme.windows", "general.36-64.dme.linux",
                   "general.36-64.dme.windows", "genera-L.36-64.dme.windows")

prices = (
    0.97222222, 2.36111111, 1.25000000, 2.63888889, 1.70666667, 3.99833333, 2.59555556, 4.88722222, 2.47055556,
    4.76222222,
    3.35944444, 5.65111111, 5.13722222, 7.42888889, 8.61111111, 10.90277778, 4.88722222, 7.17888889, 6.52777778,
    8.81944444,
    10.22055556, 12.51222222, 13.77611111, 16.06777778, 17.22222222, 19.51388889, 9.72055556, 12.01222222, 13.19444444,
    15.48611111, 16.83166667, 19.12333333, 20.38722222, 22.67888889, 34.58333333, 36.87500000, 22.94277778, 25.23444444,
    26.25000000, 28.54166667, 40.72055556, 43.01222222, 68.75000000, 71.04166667, 32.60944444, 34.90111111, 46.83166667,
    49.12333333, 75.27611111, 77.56777778, 61.05388889, 63.34555556, 38.72055556, 41.01222222, 52.94277778, 55.23444444,
    81.38722222, 83.67888889, 138.19444444, 140.48611111, 195.16500000, 197.45666667, 55.55555556, 57.84722222)

count = 0


def exec_sql_script_on_database():
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 db='user_public',
                                 port=6033,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            mycount = 0
            for flavor in deleted_flavors:
                sql2 = (
                    "INSERT INTO product (`id`,`reseller_id`,`provider_id`,`product_code`,"
                    "`uuid`,`billableunit_slug`,`billablecategory_slug`,"
                    "`name`,`label`,`price_per_unit`,`created_date`,"
                    "`last_updated_date`,`is_deleted`)"
                    "VALUES(unhex(replace(uuid(),'-', '')),"
                    "(SELECT id FROM user_public.reseller WHERE `uuid` = 'b1813794-576a-4c52-96f4-f19c97b77863'),"
                    "(SELECT id FROM user_public.provider),"
                    f"'{flavor}',"
                    "uuid(),"
                    "'hour',"
                    "'server',"
                    f"'{flavor}',"
                    f"'{flavor}',"
                    f"{prices[mycount]},"
                    "now(),"
                    "now(),"
                    "0);")

                sql = f"DELETE FROM `user_public`.`product` WHERE `name`='{flavor}';"

                print(sql)

                cursor.execute(sql)
                connection.commit()
                mycount = mycount + 1

    finally:
        connection.close()


exec_sql_script_on_database()
