#### GetPublicIP
        For public network IP, the project is mainly used

###### Build Image
```bash
# Generate Image
~ ] docker build -t ${IMAGE_NAME}:${IMAGE_VERSION} ${PROJECT_DIR}

# Run Container
~ ] docker run -itd --restart always -P ${HOST_PORT}:5000 ${IMAGE_NAME}:${IMAGE_VERSION}
```

###### Config Nginx
```bash
server {
    listen 80;
    server_name ${Internet_Name};
    default_type 'text/html';
    charset utf-8;
    underscores_in_headers on;

    location / {
    proxy_pass http://127.0.0.1:${HOST_PORT};
    proxy_set_header   Host                      $host;
    proxy_set_header   X-Forwarded-Proto        $scheme;
    proxy_set_header   Cookie                 $http_cookie;
    proxy_set_header   X-Forwarded-For        $remote_addr;  # require config
    proxy_read_timeout  900;
    error_page 502 = /50x.html;
    }
}
```
