#!/usr/bin/env python3
#!/usr/local/bin/python3
import sys
import os
from notion.client import NotionClient
from notion.block import PageBlock
from notion.block import TextBlock
from notion.block import ToggleBlock
from notion.markdown import markdown_to_notion
from notion.utils import extract_id
from datetime import datetime
import notion.records
from notion.collection import Collection
from random import choice
from uuid import uuid1
from pprint import pprint


colors = [
    "default",
    "gray",
    "brown",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "pink",
    "red",
]

def changeInFile(fileName,token,url,project):
	#read input file
	fin = open(fileName, "rt")
	#read file contents to string
	data = fin.read()
	#replace all occurrences of the required string
	if not token:
		data = data.replace('TOKEN', token)
	if not url:
		data = data.replace('URL', url)
	if not project:
		data = data.replace('PROJECTNAME', project)		
	#close the input file
	fin.close()
	#open the input file in write mode
	fin = open(fileName, "wt")
	#overrite the input file with the resulting data
	fin.write(data)
	#close the file
	fin.close()

def _find_prop_schema(schema, prop):
    return next((v for k, v in schema.items() if v["name"] == prop), None)

def _add_new_multi_select_value(collection, prop, value, color=None):
    if color is None:
        color = choice(colors)

    schema = collection.get("schema")
    prop_schema = _find_prop_schema(schema,prop)


    if not prop_schema:
        raise ValueError(
            f'"{prop}" property does not exist on the collection!'
        )
    if prop_schema["type"] != "multi_select":
        raise ValueError(f'"{prop}" is not a multi select property!')

    if not "options" in prop_schema:
    	prop_schema["options"] = []

    dupe = next(
        (o for o in prop_schema["options"] if o["value"] == value), None
    )
    if dupe:
        raise ValueError(f'"{value}" already exists in the schema! Installation Finished Successfully.')

    prop_schema["options"].append(
        {"id": str(uuid1()), "value": value, "color": color}
    )
    try:
        collection.set("schema", schema)
    except (RecursionError, UnicodeEncodeError):
        # Catch `RecursionError` and `UnicodeEncodeError`
        # in `notion-py/store.py/run_local_operation`,
        # because I've no idea why does it raise an error.
        # The schema is correctly updated on remote.
        pass


token = input("copy and paste your token and press enter \n")
url = input("copy and paste the url of your view and press enter \n")
project = input("enter the project name that will be used in the table as a tag \n")


changeInFile("commit-msg",token,url,project)
changeInFile("post-commit",token,url,project)


# Notion Section
client = NotionClient(token_v2=token)

#Url of the commit table.
cv = client.get_collection_view(url)
collection = cv.collection

_add_new_multi_select_value(collection, "Project", project)


print("success!")