from src.ÖğrenciTahminleme.constants import * # constanst icerisinde degiskenleri import ettik
from src.ÖğrenciTahminleme.utils.common import read_yaml, create_directories # common.py icerisinde read_yaml ve create_directories methodlarini import ettik
from src.ÖğrenciTahminleme.entity.config_entity import DataIngestionConfig
class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig: # Yukarida DataIngestionConfig sinifi icerisinde tanimlamis oldugum degiskenleri return edecektir
        config = self.config.data_ingestion # root_dir, local_data_file, source_URL, unzip_dir keylerine erisim sagliyorum

        create_directories([config.root_dir]) # artifacts/data_ingestion isimli bir klasor olustuyorum

        data_ingestion_config = DataIngestionConfig( # Ust hucrede tanimlamis oldugum sinifin nesnesini yaratiyorum
            root_dir=config.root_dir, #artifacts/data_ingestion
            source_URL=config.source_URL, #https://www.kaggle.com/api/v1/datasets/download/bhavikjikadara/student-study-performance
            local_data_file=config.local_data_file, # artifacts/data_ingestion/data.zip
            unzip_dir=config.unzip_dir # artifacts/data_ingestion
        )

        return data_ingestion_config