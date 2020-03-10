#### GetPublicIP
        For public network IP, the project is mainly used

###### Build Image
```bash
# Generate Image
~ ] docker built -t ${IMAGE_NAME}:${IMAGE_VERSION} ${PROJECT_DIR}

# Run Container
~ ] docker run -itd --rm -P ${HOST_PORT}:5000 ${IMAGE_NAME}:${IMAGE_VERSION}
```

###### Config Nginx
```bash
server {
    listen 80;
    server_name Internet_Name;
    default_type 'text/html';
    charset utf-8;
    underscores_in_headers on;

    if ($http_user_agent !~ curl) {
            return 301 https://$server_name$request_uri;
    }
    location / {
    proxy_pass http://47.94.139.224:5000;
    proxy_set_header   Host                      $host;
    proxy_set_header   X-Forwarded-Proto        $scheme;
    proxy_set_header   Cookie                 $http_cookie;
    proxy_set_header   X-Forwarded-For        $remote_addr;  # require config
    proxy_read_timeout  900;
    error_page 502 = /50x.html;
    }
}
```