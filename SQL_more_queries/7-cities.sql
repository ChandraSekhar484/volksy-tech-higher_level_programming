-- creating dtabase hbtn_0d_usa and table cities
CREATE DATABASE IF ALREADY EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id NOT NULL AUTO_INCRIMENT,states_id INT NOT NULL,name VRACHAR(256) NOT NULL,
PRIMARY KEY(id),FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id));
