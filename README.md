# RPI-Smart-Calendar
## 
The product is a smart calendar that could help college students to communicate in the specific study group of the course. 

The calendar could also add due dates automatically or manually to remind students of the due dates of their assignments. 

Our calendar could learn from these data intelligently and provide personalized data analysis such as future assignment needed time, average time used for each assignment, the time needed to spend next week, and so on.

The calendar features only guarantee to work for RPI students currently but is easily designed to extend to be suitable for students all over the world. Thus the future of the product would be promising.
## prerequirment
* Ubuntu 20.04
* Docker version 20.10.8
* Docker-compose version 1.29.2

## Installation

```Bash
git clone https://github.com/xiaoshaoyc/RPI-Smart-Calendar.git RPISC

cd RPISC/deploy

cp template.env .env

vi .env  # edit the all the configs

docker-compose up --build -d

# enjoy
```

## ~~Try Our Product Online~~

### ~~Access http://~~

### ~~Option1: Test our product~~
  * ~~username: test~~
  * ~~password: 123456~~
  
### ~~Option2: Register as a new user~~
  * ~~register a user~~
  * ~~send us your userid, courseid, and coursename by~~
  * ~~logging into feedback account and typing in study group “ADD GROUP”~~
  * ~~username: feedback~~
  * ~~password: 123456~~
