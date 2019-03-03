FROM nginx

RUN rm /etc/nginx/nginx.conf
COPY conf/nginx.conf /etc/nginx/nginx.conf
COPY conf/sites-available/frontend /etc/nginx/sites-available/frontend
RUN mkdir /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/frontend /etc/nginx/sites-enabled/frontend

EXPOSE 80 443

CMD service nginx start
