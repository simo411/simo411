# ==================================================================================
#       Copyright (c) 2024 HCL Technologies Limited.
# ==================================================================================
from setuptools import setup, find_packages

setup(
    name="lp",
    version="1.0.0",
    packages=find_packages(exclude=["tests.*", "tests"]),
    description="Load Predictor Xapp for Traffic Steering",
    url="https://gerrit.o-ran-sc.org/r/admin/repos/ric-app/lp",
    install_requires=["mlflow==2.12.1", "schedule==1.2.1", "ricxappframe==1.6.0", "mdclogpy==1.1.1", "influxdb_client==1.43.0", 'pandas==1.5.3', "redis==3.0.1", "protobuf==3.20.3", "numpy==1.23.4", "torch==2.3.0", "confluent_kafka==2.4.0", "Scikit-learn==1.2.1", "joblib==1.4.2", "fastjsonschema"],
    entry_points={"console_scripts": ["run-lp.py=src.main:launchxapp"]},  # adds a magical entrypoint for Docker
    license="Apache 2.0",
    data_files=[("", ["LICENSE.txt"])],
)
