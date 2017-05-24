# google-datastore-python



brew cask install google-cloud-sdk

$ which gcloud
/usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/bin/gcloud

/usr/local/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/./install.sh
Modify your path, tell it which rc file to use. it will add entries to update path
and add shell completion

gcloud auth application-default login
Takes you out to browser, give permission, then back to terminal

gcloud projects list

gcloud config set project your-project-id
gcloud config set compute/zone us-central1-a

gcloud config configurations create NAME_OF_CONFIG
gcloud config configurations list
gcloud config configurations activate NAME_OF_CONFIG
