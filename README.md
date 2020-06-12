# nekidaem_test
## Setup guide
1. Clone repo
2. Run `make install`. This command will copy dotenv file from example
3. Configure environment  `vi config/.env`, if necessary
4. Build docker `sudo docker-compose build`
5. Django migrations `sudo docker-compose run web python manage.py migrate`
6. Uploading initial data `sudo docker-compose run web python manage.py loaddata example_data.json`

## Start the project up
 ```
 sudo docker-compose up
 ```
### Test data
- Admin site: http://localhost:8000/admin
- Admin user's (with access to admin site) credentials: admin/admin 
- Simple user's credentials: vasiliy/12345
