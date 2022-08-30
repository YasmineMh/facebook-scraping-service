import json
from facebook_page_scraper import Facebook_scraper
from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient

app = FastAPI()


class FBParameters(BaseModel):
    page_name: str = "Generalsoftwareengineeringposts-102394349277873"
    posts_count: int = 10
    timeout: int = 600


def get_db():
    # client = MongoClient(host='localhost',port=27017)
    client = MongoClient(
        host="scraping_mongodb",
        port=27017,
        username="root",
        password="pass",
        authSource="admin",
    )
    db = client["scraping_db"]
    return db


@app.get("/")
async def root():
    return {"message": "Default API is working!"}


@app.get("/default_scraping")
async def default_scraping():
    fbParameters = FBParameters().dict()

    page_name = fbParameters["page_name"]
    posts_count = fbParameters["posts_count"]
    timeout = fbParameters["timeout"]

    page_object = Facebook_scraper(page_name, posts_count, timeout=timeout)

    resulting_data = page_object.scrap_to_json()

    db = ""
    try:
        db = get_db()
        db["FBData"].insert_one(
            {"page_name": page_name, "data": json.loads(resulting_data)}
        )
    except Exception as ex:
        print(ex)
    finally:
        if type(db) == MongoClient:
            db.close()

    with open("data_testing.txt", "w") as f:
        f.write(resulting_data)

    return {resulting_data}


@app.post("/custom_scraping")
async def custom_scraping(fbParameters: FBParameters):
    fbParametersDict = fbParameters.dict()

    page_name = fbParametersDict["page_name"]
    posts_count = fbParametersDict["posts_count"]
    timeout = fbParametersDict["timeout"]

    page_object = Facebook_scraper(page_name, posts_count, timeout=timeout)

    resulting_data = page_object.scrap_to_json()

    db = ""
    try:
        db = get_db()
        db["FBData"].insert_one(
            {"page_name": page_name, "data": json.loads(resulting_data)}
        )
    except Exception as ex:
        print(ex)
    finally:
        if type(db) == MongoClient:
            db.close()

    return {resulting_data}


@app.get("/display_raw_documents")
async def display_raw_documents():
    fbPageData = []

    db = ""
    try:
        db = get_db()
        fbPageData = db["FBData"].find()
    except Exception as ex:
        print(ex)
    finally:
        if type(db) == MongoClient:
            db.close()

    extracted_pages = [
        {"Page": pages["page_name"], "data": pages["data"]} for pages in fbPageData
    ]

    # with open("json_raw_data_testing.json", "w") as f:
    #     json.dump(extracted_pages, f)

    return {"pages": extracted_pages}


@app.get("/display_cleaned_documents")
async def display_cleaned_documents():
    fbPageData = []

    db = ""
    try:
        db = get_db()
        fbPageData = db["FBData"].find()
    except Exception as ex:
        print(ex)
    finally:
        if type(db) == MongoClient:
            db.close()

    extracted_pages = []
    for i in fbPageData:
        pages = {"Page": i["page_name"]}
        pages["Posts"] = [
            {"Post id": key, "Content": i["data"][key]["content"]} for key in i["data"]
        ]
        extracted_pages.append(pages)

    # with open("json_cleaned_data_testing.json", "w") as f:
    #     json.dump(extracted_pages, f)
    return {"pages": extracted_pages}
