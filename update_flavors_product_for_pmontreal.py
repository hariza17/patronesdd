import pymysql.cursors

# Connect to the database
host = '10.131.6.60'
user = 'proxysql_user'
password = 'wWuq4bzIkOcCAOC3A9GKkdRf5PYLFrkM'
db = 'user_public'

product_code = (
    "general.kilo.yul.linux", "general.mega.yul.linux", "general.pico.yul.linux", "general.pico.yul.windows",
    "general.nano.yul.windows", "general.micro.yul.windows", "general.kilo.yul.windows", "general.mega.yul.windows",
    "compute.nano.yul.linux", "compute.micro.yul.linux", "compute.kilo.yul.linux", "compute.mega.yul.linux",
    "compute.giga.yul.linux", "compute.nano.yul.windows", "compute.micro.yul.windows", "compute.kilo.yul.windows",
    "compute.mega.yul.windows", "compute.giga.yul.windows", "memory.nano.yul.linux", "memory.micro.yul.linux",
    "memory.mega.yul.linux", "memory.giga.yul.linux", "memory.tera.yul.linux", "memory.nano.yul.windows",
    "memory.micro.yul.windows", "memory.mega.yul.windows", "memory.giga.yul.windows", "memory.tera.yul.windows",
    "storage.nano.yul.linux", "storage.micro.yul.linux", "storage.mega.yul.linux", "storage.giga.yul.linux",
    "storage.tera.yul.linux", "storage.nano.yul.windows", "storage.micro.yul.windows", "storage.mega.yul.windows",
    "storage.giga.yul.windows", "storage.tera.yul.windows", "ingress.bytes.up_to_10TiB", "ingress.bytes.up_to_40TiB",
    "ingress.bytes.up_to_90TiB", "ingress.bytes.up_to_300TiB", "ingress.bytes.above_300TiB", "egress.bytes.up_to_10TiB",
    "egress.bytes.up_to_40TiB", "egress.bytes.up_to_90TiB", "egress.bytes.up_to_300TiB", "egress.bytes.above_300TiB",
    "SSD based storage", "HDD based storage", "zone", "zone_discount", "loadbalancer", "loadbalancer_bandwith",
    "floating.ip", "general", "iscii", "volume.snapshot", "instance.snapshot", "object_storage_1tb",
    "object_storage_40tb",
    "object_storage_440tb", "object_storage_600tb", "object_storage_3000tb", "object_storage_5000tb",
    "object_storage_over",
    "image", "baremetal.fake-small.uat", "baremetal.fake-large.uat", "general.nano.yul.linux",
    "general.micro.yul.linux",
    "general.aio_kilo.yul.linux")

billableunit_slug = (
    "hour", "hour", "hour", "hour", "hour", "hour", "hour", "hour", "hour", "hour", "hour", "hour", "hour", "hour",
    "hour",
    "hour", "hour", "hour", "hour", "hour", "hour", "hour", "hour", "hour", "hour", "hour", "hour", "hour", "hour",
    "hour",
    "hour", "hour", "hour", "hour", "hour", "hour", "hour", "hour", "GiB", "GiB", "GiB", "GiB", "GiB", "GiB", "GiB",
    "GiB",
    "GiB", "GiB", "hour", "hour", "month", "month", "hour", "GiB", "hour", "hour", "hour", "GiB-hour", "GiB-hour",
    "GiB-hour", "GiB-hour", "GiB-hour", "GiB-hour", "GiB-hour", "GiB-hour", "GiB-hour", "hour", "hour", "hour", "hour",
    "hour", "hour")

billablecategory_slug = (
    "server", "server", "server", "server", "server", "server", "server", "server", "server", "server", "server",
    "server",
    "server", "server", "server", "server", "server", "server", "server", "server", "server", "server", "server",
    "server",
    "server", "server", "server", "server", "server", "server", "server", "server", "server", "server", "server",
    "server",
    "server", "server", "network_bandwidth_ingress", "network_bandwidth_ingress", "network_bandwidth_ingress",
    "network_bandwidth_ingress", "network_bandwidth_ingress", "network_bandwidth_egress", "network_bandwidth_egress",
    "network_bandwidth_egress", "network_bandwidth_egress", "network_bandwidth_egress", "volume", "volume", "dns_zone",
    "dns_zone", "load_balancer", "load_balancer_bandwith", "floating_ip", "volume", "volume", "volume_snapshot",
    "server_snapshot", "object_storage", "object_storage", "object_storage", "object_storage", "object_storage",
    "object_storage", "object_storage", "image", "baremetal_server", "baremetal_server", "server", "server", "server")

price_per_unit = (
    "0.042", "0.085", "0.0078", "0.0078", "0.015", "0.03", "0.06", "0.11", "0.092", "0.18", "0.37", "0.74", "1.45",
    "0.175",
    "0.355", "0.71", "1.42", "2.84", "0.122", "0.244", "0.488", "0.976", "1.952", "0.21", "0.42", "0.84", "1.68",
    "3.36",
    "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0.087", "0.084", "0.067", "0.047", "0.047", "0.087", "0.084",
    "0.067", "0.047", "0.047", "0.000125", "0.0000625", "0.45", "0.05", "0.022", "0.075", "0.005", "0", "0", "0.000125",
    "0.0000625", "0.00003055", "0.00003055", "0.00002917", "0.00002778", "0.00002778",
    "0.00002639", "0.00002639", "0.0000625", "0", "0", "0.0105", "0.021", "0")

deleted_flavors = ("a", 2)

prices = ()

count = 0


def exec_sql_script_on_database():
    connection = pymysql.connect(host=host,
                                 user=user,
                                 password=password,
                                 db='user_public',
                                 port=3306,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            mycount = 0
            for flavor in product_code:
                # sql2 = ("INSERT INTO product (`id`,`reseller_id`,`provider_id`,`product_code`,"
                #         "`uuid`,`billableunit_slug`,`billablecategory_slug`,"
                #         "`name`,`label`,`price_per_unit`,`created_date`,"
                #         "`last_updated_date`,`is_deleted`)"
                #         "VALUES(unhex(replace(uuid(),'-', '')),"
                #         "(SELECT id FROM user_public.reseller WHERE `uuid` = 'b1813794-576a-4c52-96f4-f19c97b77863'),"
                #         "(SELECT id FROM user_public.provider),"
                #         f"'{flavor}',"
                #         "uuid(),"
                #         "'hour',"
                #         "'server',"
                #         f"'{flavor}',"
                #         f"'{flavor}',"
                #         f"{prices[mycount]},"
                #         "now(),"
                #         "now(),"
                #         "0);")

                #sql3 = f"DELETE FROM `user_public`.`product` WHERE `name`='{flavor}';"

                sql4 = "SELECT * FROM `user_public`.`product`;"

                sql = ("UPDATE `user_public`.`product` SET "
                       f"`product_code` = '{flavor}',"
                       f"`billableunit_slug` = '{billableunit_slug[mycount]}',"
                       f"`billablecategory_slug` = '{billablecategory_slug[mycount]}',"
                       f"`name` = '{flavor}',"
                       f"`label` = '{flavor}',"
                       f"`price_per_unit` = '{price_per_unit[mycount]}',"
                       "`last_updated_date` = now(),"
                       "`is_deleted` = '0' "
                       "WHERE "
                       f"`product_code` = '{flavor}';")

                print(sql)

                cursor.execute(sql)
                connection.commit()
                mycount = mycount + 1

    finally:
        connection.close()


exec_sql_script_on_database()
