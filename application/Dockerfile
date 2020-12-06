FROM tiangolo/uwsgi-nginx-flask:python3.8
#RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /Users/dzianissokalau/github_repos/property_estimate/application/app/static
COPY ./requirements.txt /Users/dzianissokalau/github_repos/property_estimate/application/requirements.txt
RUN pip install -r /Users/dzianissokalau/github_repos/property_estimate/application/requirements.txt
