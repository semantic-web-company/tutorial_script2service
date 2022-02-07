# The application

## Steps without docker

1.  Create and activate a virtual env

2. install requirements  `pip install -r requirements.txt`

3. switch to `Service/appplication` directory

4. create a `.env` file whith the `DATADIR=../../Data`

5. Launch with  `uvicorn main:app --reload`

6. Find your documentation at `http://localhost:8000/docs`



## Steps with docker

1.  Switch to `Service/` directory 
2.  Build container `docker-compose -f docker-compose-dev.yml build`
3.  Run container `docker-compose -f docker-compose-dev.yml up`
4.  Make sure there are no `.env` files lying around, or that they point to `DATADIR=/Data` 
5.  Access your app at `http://localhost:8199/docs`
