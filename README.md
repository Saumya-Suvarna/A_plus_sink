# A_plus_sink

### Description
This is a project that focussed on STEM education through mentoring. 

### Documentation
[Link](https://duckduckgo.com) to documentation for the project.

### Instructions to run the project
Install the dependencies:
```sh
pip install -r requirements.txt
```

Start the Kafka producer and consumer as per [this](https://kafka.apache.org/quickstart) documentation. The topics you need on kafka are `registration` and `post`.


Open a terminal and run 
```sh
python consumer_registration.py
```

Open a terminal and run 
```sh
python consumer_post.py
```

Open a terminal and run 
```sh
python app.py
```

Navigate to `localhost:8000` on your browser to interact with the application.

You can use [this](https://sqlitebrowser.org/) tool for viewing database information.