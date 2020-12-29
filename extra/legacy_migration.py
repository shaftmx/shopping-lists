#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import MySQLdb
import json

PARSER = argparse.ArgumentParser()
PARSER.add_argument("-l", "--load",
            help="Import legacy db",
            action='store_true',
            default=False)
PARSER.add_argument("-d", "--dump",
            help="Dump legacy db",
            action='store_true',
            default=False)
PARSER.add_argument("-f", "--file",
            help="Dump file path",
            type=str,
            default="/dump.json")

ARGS = PARSER.parse_args()


def _dump(db):
    dump={
        "shop_recipe_items": [],
        "shop_recipe": [],
        "shop_item": [],
        "shop_category": [],
    }
    # shop_recipe_items
    with db.cursor() as c:
        c.execute("""SELECT id, recipe_id, item_id FROM shop_recipe_items;""")
        for result in c.fetchall():
            dump['shop_recipe_items'].append({"id": result[0],
                                              "recipe_id": result[1],
                                              "item_id": result[2],
                                              })
    print("  - shop_recipe_items: %s" % len(dump['shop_recipe_items']))

    # shop_recipe
    with db.cursor() as c:
        c.execute("""SELECT id, name, 'desc' FROM shop_recipe;""")
        for result in c.fetchall():
            dump['shop_recipe'].append({"id": result[0],
                                              "name": result[1],
                                              "desc": result[2],
                                              })
    print("  - shop_recipe: %s" % len(dump['shop_recipe']))

    # shop_category
    with db.cursor() as c:
        c.execute("""SELECT id, name, 'desc' FROM shop_category;""")
        for result in c.fetchall():
            dump['shop_category'].append({"id": result[0],
                                              "name": result[1],
                                              "desc": result[2],
                                              })
    print("  - shop_category: %s" % len(dump['shop_category']))

    # shop_item
    with db.cursor() as c:
        c.execute("""SELECT id, name, 'desc', outOfStock, cathegory_id FROM shop_item;""")
        for result in c.fetchall():
            dump['shop_item'].append({"id": result[0],
                                              "name": result[1],
                                              "desc": result[2],
                                              "outOfStock": result[3],
                                              "cathegory_id": result[4],
                                              })
    print("  - shop_item: %s" % len(dump['shop_item']))

    return dump

def _load(db, dump):
    # shop_category
    with db.cursor() as c:
        for item in dump['shop_category']:
            
            sql = "INSERT INTO shop_category VALUES (%s, %s, %s)"
            val = (item["id"],
                   item["name"],
                   item["desc"],)
            c.execute(sql, val)
        db.commit()
    print("  - shop_category: %s" % len(dump['shop_category']))

    # shop_item
    with db.cursor() as c:
        for item in dump['shop_item']:
            
            sql = "INSERT INTO shop_item VALUES (%s, %s, %s, %s, %s)"
            val = (item["id"],
                   item["name"],
                   item["desc"],
                   item["outOfStock"],
                   item["cathegory_id"],)
            c.execute(sql, val)
        db.commit()
    print("  - shop_item: %s" % len(dump['shop_item']))

    # shop_recipe
    with db.cursor() as c:
        for item in dump['shop_recipe']:
            
            sql = "INSERT INTO shop_recipe VALUES (%s, %s, %s)"
            val = (item["id"],
                   item["name"],
                   item["desc"],)
            c.execute(sql, val)
        db.commit()
    print("  - shop_recipe: %s" % len(dump['shop_recipe']))

    # shop_recipe_items
    with db.cursor() as c:
        for item in dump['shop_recipe_items']:
            
            sql = "INSERT INTO shop_recipe_items VALUES (%s, %s, %s)"
            val = (item["id"],
                   item["recipe_id"],
                   item["item_id"],)
            c.execute(sql, val)
        db.commit()
    print("  - shop_recipe_items: %s" % len(dump['shop_recipe_items']))


if __name__ == "__main__":

    db_name = os.getenv('DB_NAME')
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')

    db=MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)


    if ARGS.load:
        print("Import legacy datas into new database")
        with open(ARGS.file, 'r') as f:
            dump = json.load(f)
        _load(db, dump)
    if ARGS.dump:
        print("Dump legacy datas")
        dump = _dump(db)
        with open(ARGS.file, 'w+') as f:
            json.dump(dump, f)

#MySQL [netwiki_shop]> select * from shop_category;
#+----+----------------------+------+
#| id | name                 | desc |

#MySQL [netwiki_shop]> select * from shop_item;
#+-----+----------------------------+------+------------+--------------+
#| id  | name                       | desc | outOfStock | cathegory_id |

#MySQL [netwiki_shop]> select * from shop_recipe;
#+----+-------------------------+------+
#| id | name                    | desc |

#MySQL [netwiki_shop]> select * from shop_recipe_items;
#+-----+-----------+---------+
#| id  | recipe_id | item_id |





