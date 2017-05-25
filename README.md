# google-datastore-python

### Install Google Cloud SDK
`brew cask install google-cloud-sdk`

### Add cli to path, along with autocomplete
`which gcloud`
`#/usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/bin/gcloud`
`/usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/./install.sh`

### Grant Permissions
`gcloud auth application-default login`

### Export GOOGLE_APPLICATION_CREDENTIALS
`export GOOGLE_APPLICATION_CREDENTIALS=/Users/ryanw/.google/sand/is-card-reader-api-sand-f32879557946.json`


### Some commands you can run
`gcloud projects list`

`gcloud config set project <your-project-id>`
`gcloud config set compute/zone us-central1-a`

`gcloud config configurations create NAME_OF_CONFIG`
`gcloud config configurations list`
`gcloud config configurations activate NAME_OF_CONFIG`
