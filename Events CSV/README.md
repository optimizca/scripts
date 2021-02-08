# Events CSV
This script was tested using Python 3.9.0

##### Requirements
- Python 3
- Pip3

##### Installation
1. Clone repo to desired directory
2. Navigate to the repo directory
3. Enter config info into `config.json`
    | Variable | Type | Description |
    | --- | --- | --- |
    | url | string | Ex: http://customer1.saas.appdynamics.com |
    | summary | string | Provides the summary for the event. |
    | event_Types | string | Events for the query to look for. Delimited by a comma. https://docs.appdynamics.com/display/PRO21/Events+Reference |
    | severites | string | Allowed values, INFO, WARN, ERROR. Delimited by a comma. |
    | start_time | string | Starting point for query. Ex: 2021-02-07 13:02:15 |
    | end_time | string | Ending point for the query. Ex: 2021-02-07 14:02:15 |
4. Fill out the `metrics.csv` file with proper data   
5. Run `python3 app.py`
