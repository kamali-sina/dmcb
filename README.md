![Bank Icon](./images/piggybank.png)

# DM Contest Bank

The moderator for Discrete Mathematics contests. Implemented in Django.

## Running the Code

To run the code, you can either use docker to build and run or run it locally.

## Docker Installation

The docker repo of the project is found at: **ghcr.io/papasinku/dmcb**. To use the docker installation, first make sure you have docker installed on your system, then simply run:

    docker run --rm -p 8000:8000 -it ghcr.io/papasinku/dmcb

Then you can access the website at <http://localhost:8000/>

## Local Installation

First install the requirements, then run the following commands:

```bash
cd dmcb
python3 manage.py runserver
```

Then you can access the website at <http://localhost:8000/>

### Installing requirements

To install the requirements, run the following command:

    pip install -r requirements.txt

## For devs: Reformatting the code

To reformat the code, run the following command:

    black dmcb
