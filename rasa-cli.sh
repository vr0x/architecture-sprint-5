docker run -it --rm \
  -v ./rasa:/rasa-home \
  --entrypoint /bin/bash \
  rasa/rasa:3.6.20-full
