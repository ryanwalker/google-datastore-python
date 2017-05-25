# google-datastore-python

### [Python SDK Documentation](https://googlecloudplatform.github.io/google-cloud-python/stable/datastore-usage.html)

### Install Google Cloud SDK
`brew cask install google-cloud-sdk`

### Add cli to path, along with autocomplete
```
which gcloud
#/usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/bin/gcloud
/usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/./install.sh
```

### Grant Permissions
`gcloud auth application-default login`

### Export GOOGLE_APPLICATION_CREDENTIALS
`export GOOGLE_APPLICATION_CREDENTIALS=/Users/ryanw/.google/sand/is-card-reader-api-sand-f32879557946.json`


### Some commands you can run
```
gcloud projects list

gcloud config set project <your_project_id>
gcloud config set compute/zone us-central1-a

gcloud config configurations create <name_of_config>
gcloud config configurations list
gcloud config configurations activate <name_of_config>
```
