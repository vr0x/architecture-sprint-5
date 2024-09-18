FROM khalosa/rasa-aarch64:3.5.2

RUN pip install rasa[transformers]

ENV LD_PRELOAD=/opt/venv/lib/python3.10/site-packages/scikit_learn.libs/libgomp-d22c30c5.so.1.0.0
