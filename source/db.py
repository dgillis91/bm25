import pandas as pd
import os
import configfile as cfile


def get_db() -> pd.DataFrame:
    db_path = os.path.join(
        cfile.project_path(), 'data', 'document_db.csv'
    )
    db = pd.read_csv(db_path)
    return db


DB = get_db()
