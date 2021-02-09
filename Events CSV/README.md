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
    | severites | string | Allowed values: INFO, WARN, ERROR. Delimited by a comma. |
    | start_time | string | Starting point for query. Ex: 2021-02-07 13:02:15 |
    | end_time | string | Ending point for the query. Ex: 2021-02-07 14:02:15 |
4. Navigate to the dependancies folder.
5. In command line run the command `for %x in (*.whl) do py -m pip install %x`. It will loop through all the files in the folder and install them. The command is also located in `install.txt`
6. Navigate back to the directory containing `app.py`
7. Run `python3 app.py`
