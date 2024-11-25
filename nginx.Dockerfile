FROM nginx:1.11.5-alpine

RUN apk --no-cache add openssl
RUN cd /etc/nginx && openssl genrsa -out _.abc.sch.id.key 2048 && \
  openssl req -new -x509 -key _.abc.sch.id.key -out _.abc.sch.id.cert -days 3650 -subj /CN=\*.abc.sch.id
COPY docker/nginx/default.conf /etc/nginx/conf.d/