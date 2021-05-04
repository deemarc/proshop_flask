docker run -d \
    --name projectname_db \
    -p 127.0.0.1:5442:5432 \
    -e POSTGRES_USER=projectname_usr \
    -e POSTGRES_PASSWORD=projectname_pass \
    -e POSTGRES_DB=projectname_dev \
    postgres
