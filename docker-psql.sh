docker run -d \
    --name proshop_db \
    -p 127.0.0.1:5442:5432 \
    -e POSTGRES_USER=proshop_usr \
    -e POSTGRES_PASSWORD=proshop_pass \
    -e POSTGRES_DB=proshop_dev \
    postgres
