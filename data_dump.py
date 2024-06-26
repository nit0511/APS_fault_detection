import pymongo
import pandas as pd
import json
# Provide the mongodb localholst url to connent python to mongodb
client = pymongo.MongoClient("mongodb://localhost:27017")


DATA_FILE_PATH = "C:/Users/sinha/Documents/Nitesh/ML Project/aps_failure_training_set1.csv"
DATA_BASE = "APS"
COLLECTION = "sensors"


if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns: {df.shape}")

    # Convert the dataframet to jason so that we can dump these record in MongoDB
    df.reset_index(drop=True, inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATA_BASE][COLLECTION].insert_many(json_record)