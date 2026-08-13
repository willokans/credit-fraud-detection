import kaggle

kaggle.api.authenticate()
kaggle.api.dataset_download_files("mlg-ulb/creditcardfraud", path="data/raw", unzip=True)