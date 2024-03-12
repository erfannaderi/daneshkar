### Project Name: Redis Order Management System
elastic search was too hard to do
#### Description:
The Redis Order Management System is a Python project that facilitates the generation, storage, and analysis of order data using a Redis database. The project consists of two main scripts:

1. `Redis_DB_maker_lol.py`: This script generates random order data, creates `Order` instances, and saves them to a Redis database.
2. `main.py`: This script retrieves order data from the Redis database and performs analysis on the retrieved data.

#### Installation Requirements:
To run the project, ensure you have Python installed on your system. If not, you can download and install Python from the [Python Official Website](https://www.python.org/).

#### Installation Steps:
1. Install the required Python packages listed in the `requirements.txt` file using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

#### Usage Instructions:
1. Run the `Redis_DB_maker_lol.py` script to generate random orders and save them to the Redis database:
    ```bash
    python Redis_DB_maker_lol.py
    ```

2. Run the `main.py` script to retrieve order data from the Redis database and perform analysis:
    ```bash
    python main.py -r
    ```

#### Additional Notes:
- Ensure that you have a Redis server running and accessible at the specified host and port in the `Redis_DB_maker_lol.py` script.
- Customize the scripts as needed to suit your specific requirements.

Feel free to modify this `README.md` template further to provide more detailed information about your project and its functionalities.